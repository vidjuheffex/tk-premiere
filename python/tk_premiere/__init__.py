# Copyright (c) 2019 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

import sys
import sgtk


adobe_bridge = sgtk.platform.import_framework(
    "tk-framework-adobe", "tk_framework_adobe.adobe_bridge"
)


AdobeBridge = adobe_bridge.AdobeBridge


shotgun_data = sgtk.platform.import_framework(
    "tk-framework-shotgunutils", "shotgun_data"
)


shotgun_globals = sgtk.platform.import_framework(
    "tk-framework-shotgunutils", "shotgun_globals"
)


shotgun_settings = sgtk.platform.import_framework(
    "tk-framework-shotgunutils", "settings"
)


if sgtk.util.is_windows():
    win_32_api = sgtk.platform.import_framework(
        "tk-framework-adobe", "tk_framework_adobe_utils.win_32_api"
    )


class AdobeItemTypes:
    """
    This class stores some constants in order to expose certain important
    adobe premierepro internal class names within python
    """

    #: :obj:`str`
    #: The adobe.ProjectItem's internal typename
    PROJECT_ITEM = "ProjectItem"

    # TODO: Determing Types needed here
    # The Premiere API differs from After Effects here.
    # In Premiere all of these type are the same: ProjectItem
    # Differing only in their .type being CLIP BIN ROOT or FILE

    # #: :obj:`str`
    # #: The adobe.FolderItem's internal typename
    # FOLDER_ITEM = "FolderItem"

    # #: :obj:`str`
    # #: The adobe.FootageItem's internal typename
    # #FOOTAGE_ITEM = "FootageItem"
