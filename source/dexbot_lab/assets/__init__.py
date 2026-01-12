# Copyright (c) 2022-2025, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# Copyright (c) 2025, Fabio Amadio (fabioamadio93@gmail.com).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""Package containing asset and sensor configurations."""

import os

# Conveniences to other module directories via relative paths
DEXBOT_ASSETS_EXT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))
"""Path to the extension source directory."""

DEXBOT_ASSETS_DATA_DIR = os.path.join(DEXBOT_ASSETS_EXT_DIR, "data")
"""Path to the extension data directory."""

from .dexbot import *
