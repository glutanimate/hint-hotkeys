# -*- coding: utf-8 -*-

# Hint Hotkeys Add-on for Anki
#
# Copyright (C) 2016-2023  Aristotelis P. <https://glutanimate.com/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version, with the additions
# listed at the end of the license file that accompanied this program.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# NOTE: This program is subject to certain additional terms pursuant to
# Section 7 of the GNU Affero General Public License.  You should have
# received a copy of these additional terms immediately following the
# terms and conditions of the GNU Affero General Public License that
# accompanied this program.
#
# If not, please request a copy through one of the means of contact
# listed here: <https://glutanimate.com/contact/>.
#
# Any modifications to this file must keep this entire header intact.

import json
from pathlib import Path
from typing import TYPE_CHECKING, Callable, List, Tuple

from aqt import mw
from aqt.gui_hooks import state_shortcuts_will_change

from .config import get_config

if TYPE_CHECKING:
    assert mw is not None
    from aqt.main import AnkiQt, MainWindowState


with (Path(__file__).parent / "web" / "reveal_hint.js").open(
    "r", encoding="utf-8"
) as f:
    HINT_REVEAL_SCRIPT = f.read()


def create_hint_revealer(main_window: "AnkiQt", reveal_all: bool = False) -> Callable:
    reveal_command = f"hintHotkeysRevealHints({json.dumps(reveal_all)});"

    def reveal_hint():
        main_window.web.eval(
            f"""
{HINT_REVEAL_SCRIPT}
{reveal_command}
"""
        )

    return reveal_hint


def create_shortcut_adder(main_window: "AnkiQt") -> Callable:
    def maybe_add_hint_shortcuts(
        state: "MainWindowState", shortcuts: List[Tuple[str, Callable]]
    ):
        if state != "review":
            return
        addon_config = get_config(main_window.addonManager)

        shortcuts.extend(
            (
                (
                    addon_config.hotkey_reveal_one,
                    create_hint_revealer(main_window, reveal_all=False),
                ),
                (
                    addon_config.hotkey_reveal_all,
                    create_hint_revealer(main_window, reveal_all=True),
                ),
            )
        )

    return maybe_add_hint_shortcuts


shortcut_adder = create_shortcut_adder(main_window=mw)
state_shortcuts_will_change.append(shortcut_adder)
