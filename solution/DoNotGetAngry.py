from PyQt4 import QtCore, QtGui
from classes.layout_classes import LayoutMethodsInserter, LayoutControlsInserter
from classes.tile_button_decoder import TileButtonDecoder


try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Dialog(object):
    def tile_click(self, button):
        button_name = button.objectName()
        tile_index, color, is_home_tile, is_starting_tile = TileButtonDecoder.decode_button_name(button_name)
        a = 5

    def setupUi(self, Dialog):

        LayoutControlsInserter.insert_controls(self, Dialog)
        LayoutMethodsInserter.insert_methods(self)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Do Not Get Angry", None))


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
