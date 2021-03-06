# -*- coding: utf-8 -*-
"""
/***************************************************************************
Name                 : MapBiomas Collection
Description          : This plugin lets you get collection of mapping from MapBiomas Project(http://mapbiomas.org/).
Date                 : August, 2020
copyright            : (C) 2019 by Luiz Motta, Updated by Luiz Cortinhas (2020)
email                : motta.luiz@gmail.com, luiz.cortinhas@solved.eco.br

 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
__author__ = 'Luiz Cortinhas, Luiz Motta'
__date__ = '2020-10-28'
__copyright__ = '(C) 2020, Luiz Cortinhas and Luiz Motta'
__revision__ = '$Format:%H$'

import os

from qgis.PyQt.QtCore import QObject, pyqtSlot 
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction

from .mapbiomascollection import MapBiomasCollection

def classFactory(iface):
  return MapbiomasCollectionPlugin( iface )

class MapbiomasCollectionPlugin(QObject):
  def __init__(self, iface=None):
    super().__init__()
    self.iface = iface
    self.name = u"&MapbiomasCollection"
    self.mbc = MapBiomasCollection( iface )

  def initGui(self):
    name = "Mapbiomas Collection"
    about = 'Add a MapBiomas collection'
    icon = QIcon( os.path.join( os.path.dirname(__file__), 'mapbiomas.svg' ) )
    self.action = QAction( icon, name, self.iface.mainWindow() )
    self.action.setObjectName( name.replace(' ', '') )
    self.action.setWhatsThis( about )
    self.action.setStatusTip( about )
    self.action.triggered.connect( self.run )

    self.iface.addToolBarIcon( self.action )
    self.iface.addPluginToMenu( self.name, self.action )

    self.mbc.register()

  def unload(self):
    self.iface.removeToolBarIcon( self.action )
    self.iface.removePluginMenu( self.name, self.action )
    del self.action
    if not self.mbc:
      del self.mbc

  @pyqtSlot()
  def run(self):
      self.mbc.run()
 