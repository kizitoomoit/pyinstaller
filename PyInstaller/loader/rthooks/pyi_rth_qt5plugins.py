#-----------------------------------------------------------------------------
# Copyright (c) 2013, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------


# Qt4 plugins are bundled as data files (see hooks/hook-PyQt4*),
# within a "qt4_plugins" directory.
# We add a runtime hook to tell Qt4 where to find them.

import os
import sys

d = "qt5_plugins"
d = os.path.join(sys._MEIPASS, d)


# We remove QT_PLUGIN_PATH variable, beasuse we want Qt4 to load
# plugins only from one path.
if 'QT_PLUGIN_PATH' in os.environ:
    del os.environ['QT_PLUGIN_PATH']


# We cannot use QT_PLUGIN_PATH here, because it would not work when
# PyQt5 is compiled with a different CRT from Python (eg: it happens
# with Riverbank's GPL package).
from PyQt5.QtCore import QCoreApplication
# We set "qt5_plugins" as only one path for Qt5 plugins
QCoreApplication.setLibraryPaths([os.path.abspath(d)])
