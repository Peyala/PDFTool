# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/frames/tree.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class TreeWidget(QTreeWidget):
    def __init__(self,Form):
        super().__init__(Form)
        self.setDragDropMode(QTreeWidget.InternalMove)

    def dragMoveEvent(self, event):
        if self.canDrop(event):
            super().dragMoveEvent(event)
        else:
            event.ignore()

    def dropEvent(self, event):
        if self.canDrop(event):
            super().dropEvent(event)
        else:
            event.ignore()

    def canDrop(self, event):
        target = self.itemAt(event.pos())
        current = self.currentItem()
        if target is not None and target.parent() is current.parent():
            index = self.indexFromItem(target)
            indicator = self.dragIndicator(
                event.pos(), self.visualItemRect(target), index)
            return (indicator == QAbstractItemView.AboveItem or
                    indicator == QAbstractItemView.BelowItem)
        return False

    def dragIndicator(self, pos, rect, index):
        indicator = QAbstractItemView.OnViewport
        if not self.dragDropOverwriteMode():
            margin = int(max(2, min(rect.height() / 5.5, 12)))
            if pos.y() - rect.top() < margin:
                indicator = QAbstractItemView.AboveItem
            elif rect.bottom() - pos.y() < margin:
                indicator = QAbstractItemView.BelowItem
            elif rect.contains(pos, True):
                indicator = QAbstractItemView.OnItem
        else:
            touching = rect.adjust(-1, -1, 1, 1)
            if touching.contains(pos, False):
                indicator = QAbstractItemView.OnItem
        if (indicator == QAbstractItemView.OnItem and
            not self.model().flags(index) & Qt.ItemIsDropEnabled):
            if pos.y() < rect.center().y():
                indicator = QAbstractItemView.AboveItem
            else:
                indicator = QAbstractItemView.BelowItem
        return indicator
