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

"""
Handles add-on configuration
"""

from typing import TYPE_CHECKING, NamedTuple

if TYPE_CHECKING:
    from aqt.addons import AddonManager


class AddonConfig(NamedTuple):
    hotkey_reveal_one: str
    hotkey_reveal_all: str


def get_config(addon_manager: "AddonManager") -> AddonConfig:
    config = addon_manager.getConfig(__name__) or {}
    hotkey_reveal_one = config.get("hotkey_reveal_one")
    hotkey_reveal_all = config.get("hotkey_reveal_all")

    if not hotkey_reveal_one or not hotkey_reveal_all:
        print("Hint Hotkeys Error: Invalid config")
        return AddonConfig(hotkey_reveal_one="H", hotkey_reveal_all="G")

    return AddonConfig(
        hotkey_reveal_one=hotkey_reveal_one,
        hotkey_reveal_all=hotkey_reveal_all,
    )
