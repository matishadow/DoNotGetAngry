from time import sleep

from PyQt4 import QtCore, QtGui
from classes.layout_classes import *
from classes.tile_button_decoder import TileButtonDecoder
from classes.tcpclient import TcpClient


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
        tcp_client.send_user_decision(0 if is_starting_tile else 1)
        tcp_client.send_counter_chosen((tile_index, is_home_tile))

    def remove_counter(self, tile):
        tile.setStyleSheet(REMOVE_CSS_STYLE)

    def put_counter(self, tile, color):
        style = str.format(COUNTER_CSS_STYLE, color.lower())
        tile.setStyleSheet(style)

    def set_text(self, control, text):
        control.setText(_translate("dialog", text, None))

    def set_dice(self, number):
        self.dice.setStyleSheet(REMOVE_CSS_STYLE)
        sleep(0.3)

        style = str.format(DICE_CSS_STYLE, number)
        self.dice.setStyleSheet(style)

    def set_player_color(self, color):
        self.put_counter(self.player_color_placeholder, color)
        self.set_text(self.player_color_label, PLAYER_COLOR_LABEL)

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

    tcp_client = TcpClient(game_window=ui)
    ui.start_button.clicked.connect(tcp_client.cset_ready)
    ui.dice.clicked.connect(tcp_client.send_dice_confirm)

    sys.exit(app.exec_())

