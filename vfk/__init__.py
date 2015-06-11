# -*- coding: utf-8 -*-
"""
/***************************************************************************
 vfk
                                 A QGIS plugin
 Plugin umoznujici praci s daty katastru nemovitosti
                             -------------------
        begin                : 2015-05-13
        copyright            : (C) 2015 by Stepan Bambula, Adam Dlesk, Jaroslav Urik
        email                : stepan.bambula@fsv.cvut.cz, adam.dlesk@fsv.cvut.cz, jaroslav.urik@fsv.cvut.cz
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load vfk class from file vfk.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .vfkPlugin import vfk
    return vfk(iface)
