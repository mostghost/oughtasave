#
#  SPDX-License-Identifier: GPL-3.0-or-later
#

from krita import DockWidgetFactory, DockWidgetFactoryBase
from .oughtasave import AutosaveDocker


Application.addDockWidgetFactory(
    DockWidgetFactory("autosave_docker",
                      DockWidgetFactoryBase.DockRight,
                      AutosaveDocker))
