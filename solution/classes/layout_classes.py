from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

REMOVE_CSS_STYLE = _fromUtf8("background-color:TRANSPARENT;border:0;")
COUNTER_CSS_STYLE = _fromUtf8("background-color:transparent;border:0;\n"
                              "border-image: url(graphics/counter-{0}.png);\n"
                              "background-repeat:no-repeat;")
CURRENT_TURN_TEXT = _fromUtf8("Twoja kolej. Rzuć kostką!")
EMPTY_TEXT = _fromUtf8("")
WAIT_TURN_TEXT = _fromUtf8("Poczekaj na swoją kolej!")
PLAYER_COLOR_LABEL = _fromUtf8("Twój kolor:")


class LayoutMethodsInserter:
    @staticmethod
    def insert_methods(layout):
        layout.red_home_tile_0.clicked.connect(lambda: layout.tile_click(layout.red_home_tile_0))
        layout.red_home_tile_1.clicked.connect(lambda: layout.tile_click(layout.red_home_tile_1))
        layout.red_home_tile_2.clicked.connect(lambda: layout.tile_click(layout.red_home_tile_2))
        layout.red_home_tile_3.clicked.connect(lambda: layout.tile_click(layout.red_home_tile_3))
        layout.green_home_tile_0.clicked.connect(lambda: layout.tile_click(layout.green_home_tile_0))
        layout.green_home_tile_1.clicked.connect(lambda: layout.tile_click(layout.green_home_tile_1))
        layout.green_home_tile_2.clicked.connect(lambda: layout.tile_click(layout.green_home_tile_2))
        layout.green_home_tile_3.clicked.connect(lambda: layout.tile_click(layout.green_home_tile_3))
        layout.yellow_home_tile_0.clicked.connect(lambda: layout.tile_click(layout.yellow_home_tile_0))
        layout.yellow_home_tile_1.clicked.connect(lambda: layout.tile_click(layout.yellow_home_tile_1))
        layout.yellow_home_tile_2.clicked.connect(lambda: layout.tile_click(layout.yellow_home_tile_2))
        layout.yellow_home_tile_3.clicked.connect(lambda: layout.tile_click(layout.yellow_home_tile_3))
        layout.blue_home_tile_0.clicked.connect(lambda: layout.tile_click(layout.blue_home_tile_0))
        layout.blue_home_tile_1.clicked.connect(lambda: layout.tile_click(layout.blue_home_tile_1))
        layout.blue_home_tile_2.clicked.connect(lambda: layout.tile_click(layout.blue_home_tile_2))
        layout.blue_home_tile_3.clicked.connect(lambda: layout.tile_click(layout.blue_home_tile_3))
        layout.red_starting_tile_0.clicked.connect(lambda: layout.tile_click(layout.red_starting_tile_0))
        layout.red_starting_tile_1.clicked.connect(lambda: layout.tile_click(layout.red_starting_tile_1))
        layout.red_starting_tile_2.clicked.connect(lambda: layout.tile_click(layout.red_starting_tile_2))
        layout.red_starting_tile_3.clicked.connect(lambda: layout.tile_click(layout.red_starting_tile_3))
        layout.green_starting_tile_0.clicked.connect(lambda: layout.tile_click(layout.green_starting_tile_0))
        layout.green_starting_tile_1.clicked.connect(lambda: layout.tile_click(layout.green_starting_tile_1))
        layout.green_starting_tile_2.clicked.connect(lambda: layout.tile_click(layout.green_starting_tile_2))
        layout.green_starting_tile_3.clicked.connect(lambda: layout.tile_click(layout.green_starting_tile_3))
        layout.yellow_starting_tile_0.clicked.connect(lambda: layout.tile_click(layout.yellow_starting_tile_0))
        layout.yellow_starting_tile_1.clicked.connect(lambda: layout.tile_click(layout.yellow_starting_tile_1))
        layout.yellow_starting_tile_2.clicked.connect(lambda: layout.tile_click(layout.yellow_starting_tile_2))
        layout.yellow_starting_tile_3.clicked.connect(lambda: layout.tile_click(layout.yellow_starting_tile_3))
        layout.blue_starting_tile_0.clicked.connect(lambda: layout.tile_click(layout.blue_starting_tile_0))
        layout.blue_starting_tile_1.clicked.connect(lambda: layout.tile_click(layout.blue_starting_tile_1))
        layout.blue_starting_tile_2.clicked.connect(lambda: layout.tile_click(layout.blue_starting_tile_2))
        layout.blue_starting_tile_3.clicked.connect(lambda: layout.tile_click(layout.blue_starting_tile_3))

        layout.tile_0.clicked.connect(lambda: layout.tile_click(layout.tile_0))
        layout.tile_1.clicked.connect(lambda: layout.tile_click(layout.tile_1))
        layout.tile_2.clicked.connect(lambda: layout.tile_click(layout.tile_2))
        layout.tile_3.clicked.connect(lambda: layout.tile_click(layout.tile_3))
        layout.tile_4.clicked.connect(lambda: layout.tile_click(layout.tile_4))
        layout.tile_5.clicked.connect(lambda: layout.tile_click(layout.tile_5))
        layout.tile_6.clicked.connect(lambda: layout.tile_click(layout.tile_6))
        layout.tile_7.clicked.connect(lambda: layout.tile_click(layout.tile_7))
        layout.tile_8.clicked.connect(lambda: layout.tile_click(layout.tile_8))
        layout.tile_9.clicked.connect(lambda: layout.tile_click(layout.tile_9))
        layout.tile_10.clicked.connect(lambda: layout.tile_click(layout.tile_10))
        layout.tile_11.clicked.connect(lambda: layout.tile_click(layout.tile_11))
        layout.tile_12.clicked.connect(lambda: layout.tile_click(layout.tile_12))
        layout.tile_13.clicked.connect(lambda: layout.tile_click(layout.tile_13))
        layout.tile_14.clicked.connect(lambda: layout.tile_click(layout.tile_14))
        layout.tile_15.clicked.connect(lambda: layout.tile_click(layout.tile_15))
        layout.tile_16.clicked.connect(lambda: layout.tile_click(layout.tile_16))
        layout.tile_17.clicked.connect(lambda: layout.tile_click(layout.tile_17))
        layout.tile_18.clicked.connect(lambda: layout.tile_click(layout.tile_18))
        layout.tile_19.clicked.connect(lambda: layout.tile_click(layout.tile_19))
        layout.tile_20.clicked.connect(lambda: layout.tile_click(layout.tile_20))
        layout.tile_21.clicked.connect(lambda: layout.tile_click(layout.tile_21))
        layout.tile_22.clicked.connect(lambda: layout.tile_click(layout.tile_22))
        layout.tile_23.clicked.connect(lambda: layout.tile_click(layout.tile_23))
        layout.tile_24.clicked.connect(lambda: layout.tile_click(layout.tile_24))
        layout.tile_25.clicked.connect(lambda: layout.tile_click(layout.tile_25))
        layout.tile_26.clicked.connect(lambda: layout.tile_click(layout.tile_26))
        layout.tile_27.clicked.connect(lambda: layout.tile_click(layout.tile_27))
        layout.tile_28.clicked.connect(lambda: layout.tile_click(layout.tile_28))
        layout.tile_29.clicked.connect(lambda: layout.tile_click(layout.tile_29))
        layout.tile_30.clicked.connect(lambda: layout.tile_click(layout.tile_30))
        layout.tile_31.clicked.connect(lambda: layout.tile_click(layout.tile_31))
        layout.tile_32.clicked.connect(lambda: layout.tile_click(layout.tile_32))
        layout.tile_33.clicked.connect(lambda: layout.tile_click(layout.tile_33))
        layout.tile_34.clicked.connect(lambda: layout.tile_click(layout.tile_34))
        layout.tile_35.clicked.connect(lambda: layout.tile_click(layout.tile_35))
        layout.tile_36.clicked.connect(lambda: layout.tile_click(layout.tile_36))
        layout.tile_37.clicked.connect(lambda: layout.tile_click(layout.tile_37))
        layout.tile_38.clicked.connect(lambda: layout.tile_click(layout.tile_38))
        layout.tile_39.clicked.connect(lambda: layout.tile_click(layout.tile_39))


class LayoutControlsInserter:
    @staticmethod
    def insert_controls(layout, dialog):
        dialog.setObjectName(_fromUtf8("Dialog"))
        dialog.resize(1280, 720)
        size_policy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(dialog.sizePolicy().hasHeightForWidth())

        dialog.setSizePolicy(size_policy)
        dialog.setMinimumSize(QtCore.QSize(1280, 720))
        dialog.setMaximumSize(QtCore.QSize(1280, 720))

        layout.label = QtGui.QLabel(dialog)
        layout.label.setEnabled(True)
        layout.label.setGeometry(QtCore.QRect(-4, 0, 1280, 720))
        layout.label.setSizePolicy(size_policy)
        layout.label.setMinimumSize(QtCore.QSize(1280, 720))
        layout.label.setMaximumSize(QtCore.QSize(1280, 720))
        layout.label.setSizeIncrement(QtCore.QSize(1280, 720))
        layout.label.setBaseSize(QtCore.QSize(1280, 720))
        layout.label.setText(_fromUtf8(""))
        layout.label.setPixmap(QtGui.QPixmap(_fromUtf8("graphics/board.png")))
        layout.label.setScaledContents(True)
        layout.label.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        layout.label.setObjectName(_fromUtf8("label"))

        size_policy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(layout.label.sizePolicy().hasHeightForWidth())

        layout.blue_starting_tile_0 = QtGui.QPushButton(dialog)
        layout.blue_starting_tile_0.setGeometry(QtCore.QRect(191, 70, 41, 41))
        layout.blue_starting_tile_0.setStyleSheet(_fromUtf8("background-color:transparent;border:0;\n"
                                                            "border-image: url(graphics/counter-blue.png);\n"
                                                            "background-repeat:no-repeat;"))
        layout.blue_starting_tile_0.setText(_fromUtf8(""))
        layout.blue_starting_tile_0.setObjectName(_fromUtf8("blue_starting_tile_0"))
        layout.blue_starting_tile_1 = QtGui.QPushButton(dialog)
        layout.blue_starting_tile_1.setGeometry(QtCore.QRect(241, 70, 41, 41))
        layout.blue_starting_tile_1.setStyleSheet(_fromUtf8("background-color:transparent;border:0;\n"
                                                            "background-image: url(graphics/counter-blue.png);\n"
                                                            "background-repeat:no-repeat;"))
        layout.blue_starting_tile_1.setText(_fromUtf8(""))
        layout.blue_starting_tile_1.setObjectName(_fromUtf8("blue_starting_tile_1"))
        layout.blue_starting_tile_2 = QtGui.QPushButton(dialog)
        layout.blue_starting_tile_2.setGeometry(QtCore.QRect(191, 121, 41, 41))
        layout.blue_starting_tile_2.setStyleSheet(_fromUtf8("background-color:transparent;border:0;\n"
                                                            "border-image: url(graphics/counter-blue.png);\n"
                                                            "background-repeat:no-repeat;"))
        layout.blue_starting_tile_2.setText(_fromUtf8(""))
        layout.blue_starting_tile_2.setObjectName(_fromUtf8("blue_starting_tile_2"))
        layout.blue_starting_tile_3 = QtGui.QPushButton(dialog)
        layout.blue_starting_tile_3.setGeometry(QtCore.QRect(241, 121, 41, 41))
        layout.blue_starting_tile_3.setStyleSheet(_fromUtf8("background-color:transparent;border:0;\n"
                                                            "border-image: url(graphics/counter-blue.png);\n"
                                                            "background-repeat:no-repeat;"))
        layout.blue_starting_tile_3.setText(_fromUtf8(""))
        layout.blue_starting_tile_3.setObjectName(_fromUtf8("blue_starting_tile_3"))
        layout.yellow_starting_tile_0 = QtGui.QPushButton(dialog)
        layout.yellow_starting_tile_0.setGeometry(QtCore.QRect(191, 548, 42, 43))
        layout.yellow_starting_tile_0.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        layout.yellow_starting_tile_0.setAutoFillBackground(False)
        layout.yellow_starting_tile_0.setStyleSheet(_fromUtf8("background-color:transparent;border:0;\n"
                                                              "background-image: url(graphics/counter-yellow.png);\n"
                                                              "background-repeat:no-repeat;"))
        layout.yellow_starting_tile_0.setText(_fromUtf8(""))
        layout.yellow_starting_tile_0.setObjectName(_fromUtf8("yellow_starting_tile_0"))
        layout.yellow_starting_tile_1 = QtGui.QPushButton(dialog)
        layout.yellow_starting_tile_1.setGeometry(QtCore.QRect(241, 548, 43, 43))
        layout.yellow_starting_tile_1.setStyleSheet(_fromUtf8("background-color:transparent;border:0;\n"
                                                              "background-image: url(graphics/counter-yellow.png);\n"
                                                              "background-repeat:no-repeat;"))
        layout.yellow_starting_tile_1.setText(_fromUtf8(""))
        layout.yellow_starting_tile_1.setObjectName(_fromUtf8("yellow_starting_tile_1"))
        layout.yellow_starting_tile_2 = QtGui.QPushButton(dialog)
        layout.yellow_starting_tile_2.setGeometry(QtCore.QRect(191, 598, 43, 43))
        layout.yellow_starting_tile_2.setStyleSheet(_fromUtf8("background-color:transparent;border:0;\n"
                                                              "background-image: url(graphics/counter-yellow.png);\n"
                                                              "background-repeat:no-repeat;"))
        layout.yellow_starting_tile_2.setText(_fromUtf8(""))
        layout.yellow_starting_tile_2.setObjectName(_fromUtf8("yellow_starting_tile_2"))
        layout.yellow_starting_tile_3 = QtGui.QPushButton(dialog)
        layout.yellow_starting_tile_3.setGeometry(QtCore.QRect(241, 598, 43, 45))
        layout.yellow_starting_tile_3.setStyleSheet(_fromUtf8("background-color:transparent;border:0;\n"
                                                              "background-image: url(graphics/counter-yellow.png);\n"
                                                              "background-repeat:no-repeat;"))
        layout.yellow_starting_tile_3.setText(_fromUtf8(""))
        layout.yellow_starting_tile_3.setObjectName(_fromUtf8("yellow_starting_tile_3"))
        layout.green_starting_tile_0 = QtGui.QPushButton(dialog)
        layout.green_starting_tile_0.setGeometry(QtCore.QRect(673, 548, 43, 44))
        layout.green_starting_tile_0.setStyleSheet(_fromUtf8("background-color:transparent;border:0;\n"
                                                             "background-image: url(graphics/counter-green.png);\n"
                                                             "background-repeat:no-repeat;"))
        layout.green_starting_tile_0.setText(_fromUtf8(""))
        layout.green_starting_tile_0.setObjectName(_fromUtf8("green_starting_tile_0"))
        layout.green_starting_tile_1 = QtGui.QPushButton(dialog)
        layout.green_starting_tile_1.setGeometry(QtCore.QRect(723, 548, 43, 44))
        layout.green_starting_tile_1.setStyleSheet(_fromUtf8("background-color:transparent;border:0;\n"
                                                             "background-image: url(graphics/counter-green.png);\n"
                                                             "background-repeat:no-repeat;"))
        layout.green_starting_tile_1.setText(_fromUtf8(""))
        layout.green_starting_tile_1.setObjectName(_fromUtf8("green_starting_tile_1"))
        layout.green_starting_tile_2 = QtGui.QPushButton(dialog)
        layout.green_starting_tile_2.setGeometry(QtCore.QRect(672, 598, 43, 44))
        layout.green_starting_tile_2.setStyleSheet(_fromUtf8("background-color:transparent;border:0;\n"
                                                             "background-image: url(graphics/counter-green.png);\n"
                                                             "background-repeat:no-repeat;"))
        layout.green_starting_tile_2.setText(_fromUtf8(""))
        layout.green_starting_tile_2.setObjectName(_fromUtf8("green_starting_tile_2"))
        layout.green_starting_tile_3 = QtGui.QPushButton(dialog)
        layout.green_starting_tile_3.setGeometry(QtCore.QRect(723, 598, 43, 44))
        layout.green_starting_tile_3.setStyleSheet(_fromUtf8("background-color:transparent;border:0;\n"
                                                             "background-image: url(graphics/counter-green.png);\n"
                                                             "background-repeat:no-repeat;"))
        layout.green_starting_tile_3.setText(_fromUtf8(""))
        layout.green_starting_tile_3.setObjectName(_fromUtf8("green_starting_tile_3"))
        layout.red_starting_tile_0 = QtGui.QPushButton(dialog)
        layout.red_starting_tile_0.setGeometry(QtCore.QRect(673, 70, 43, 44))
        layout.red_starting_tile_0.setStyleSheet(_fromUtf8("background-color:transparent;border:0;\n"
                                                           "background-image: url(graphics/counter-red.png);\n"
                                                           "background-repeat:no-repeat;"))
        layout.red_starting_tile_0.setText(_fromUtf8(""))
        layout.red_starting_tile_0.setObjectName(_fromUtf8("red_starting_tile_0"))
        layout.red_starting_tile_1 = QtGui.QPushButton(dialog)
        layout.red_starting_tile_1.setGeometry(QtCore.QRect(723, 70, 43, 44))
        layout.red_starting_tile_1.setStyleSheet(_fromUtf8("background-color:transparent;border:0;\n"
                                                           "background-image: url(graphics/counter-red.png);\n"
                                                           "background-repeat:no-repeat;"))
        layout.red_starting_tile_1.setText(_fromUtf8(""))
        layout.red_starting_tile_1.setObjectName(_fromUtf8("red_starting_tile_1"))
        layout.red_starting_tile_2 = QtGui.QPushButton(dialog)
        layout.red_starting_tile_2.setGeometry(QtCore.QRect(673, 120, 43, 44))
        layout.red_starting_tile_2.setStyleSheet(_fromUtf8("background-color:transparent;border:0;\n"
                                                           "background-image: url(graphics/counter-red.png);\n"
                                                           "background-repeat:no-repeat;"))
        layout.red_starting_tile_2.setText(_fromUtf8(""))
        layout.red_starting_tile_2.setObjectName(_fromUtf8("red_starting_tile_2"))
        layout.red_starting_tile_3 = QtGui.QPushButton(dialog)
        layout.red_starting_tile_3.setGeometry(QtCore.QRect(723, 120, 43, 44))
        layout.red_starting_tile_3.setStyleSheet(_fromUtf8("background-color:transparent;border:0;\n"
                                                           "background-image: url(graphics/counter-red.png);\n"
                                                           "background-repeat:no-repeat;"))
        layout.red_starting_tile_3.setText(_fromUtf8(""))
        layout.red_starting_tile_3.setObjectName(_fromUtf8("red_starting_tile_3"))

        layout.tile_0 = QtGui.QPushButton(dialog)
        layout.tile_0.setGeometry(QtCore.QRect(172, 294, 43, 44))
        layout.tile_0.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.tile_0.setText(_fromUtf8(""))
        layout.tile_0.setObjectName(_fromUtf8("tile_0"))
        layout.tile_1 = QtGui.QPushButton(dialog)
        layout.tile_1.setGeometry(QtCore.QRect(227, 294, 43, 43))
        layout.tile_1.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.tile_1.setText(_fromUtf8(""))
        layout.tile_1.setObjectName(_fromUtf8("tile_1"))
        layout.tile_2 = QtGui.QPushButton(dialog)
        layout.tile_2.setGeometry(QtCore.QRect(281, 294, 43, 43))
        layout.tile_2.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.tile_2.setText(_fromUtf8(""))
        layout.tile_2.setObjectName(_fromUtf8("tile_2"))
        layout.tile_3 = QtGui.QPushButton(dialog)
        layout.tile_3.setGeometry(QtCore.QRect(336, 294, 43, 43))
        layout.tile_3.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.tile_3.setText(_fromUtf8(""))
        layout.tile_3.setObjectName(_fromUtf8("tile_3"))
        layout.tile_4 = QtGui.QPushButton(dialog)
        layout.tile_4.setGeometry(QtCore.QRect(394, 294, 43, 43))
        layout.tile_4.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.tile_4.setText(_fromUtf8(""))
        layout.tile_4.setObjectName(_fromUtf8("tile_4"))
        layout.tile_5 = QtGui.QPushButton(dialog)
        layout.tile_5.setGeometry(QtCore.QRect(394, 240, 43, 43))
        layout.tile_5.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.tile_5.setText(_fromUtf8(""))
        layout.tile_5.setObjectName(_fromUtf8("tile_5"))
        layout.tile_6 = QtGui.QPushButton(dialog)
        layout.tile_6.setGeometry(QtCore.QRect(394, 186, 43, 43))
        layout.tile_6.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.tile_6.setText(_fromUtf8(""))
        layout.tile_6.setObjectName(_fromUtf8("tile_6"))
        layout.tile_7 = QtGui.QPushButton(dialog)
        layout.tile_7.setGeometry(QtCore.QRect(394, 132, 43, 43))
        layout.tile_7.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.tile_7.setText(_fromUtf8(""))
        layout.tile_7.setObjectName(_fromUtf8("tile_7"))
        layout.tile_8 = QtGui.QPushButton(dialog)
        layout.tile_8.setGeometry(QtCore.QRect(394, 78, 43, 43))
        layout.tile_8.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.tile_8.setText(_fromUtf8(""))
        layout.tile_8.setObjectName(_fromUtf8("tile_8"))
        layout.tile_9 = QtGui.QPushButton(dialog)
        layout.tile_9.setGeometry(QtCore.QRect(452, 78, 43, 43))
        layout.tile_9.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.tile_9.setText(_fromUtf8(""))
        layout.tile_9.setObjectName(_fromUtf8("tile_9"))
        layout.tile_10 = QtGui.QPushButton(dialog)
        layout.tile_10.setGeometry(QtCore.QRect(510, 78, 43, 43))
        layout.tile_10.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.tile_10.setText(_fromUtf8(""))
        layout.tile_10.setObjectName(_fromUtf8("tile_10"))
        layout.tile_11 = QtGui.QPushButton(dialog)
        layout.tile_11.setGeometry(QtCore.QRect(510, 132, 43, 43))
        layout.tile_11.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.tile_11.setText(_fromUtf8(""))
        layout.tile_11.setObjectName(_fromUtf8("tile_11"))
        layout.tile_12 = QtGui.QPushButton(dialog)
        layout.tile_12.setGeometry(QtCore.QRect(510, 186, 43, 43))
        layout.tile_12.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.tile_12.setText(_fromUtf8(""))
        layout.tile_12.setObjectName(_fromUtf8("tile_12"))
        layout.tile_13 = QtGui.QPushButton(dialog)
        layout.tile_13.setGeometry(QtCore.QRect(510, 240, 43, 43))
        layout.tile_13.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.tile_13.setText(_fromUtf8(""))
        layout.tile_13.setObjectName(_fromUtf8("tile_13"))
        layout.tile_14 = QtGui.QPushButton(dialog)
        layout.tile_14.setGeometry(QtCore.QRect(510, 294, 43, 43))
        layout.tile_14.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.tile_14.setText(_fromUtf8(""))
        layout.tile_14.setObjectName(_fromUtf8("tile_14"))
        layout.tile_15 = QtGui.QPushButton(dialog)
        layout.tile_15.setGeometry(QtCore.QRect(568, 294, 43, 43))
        layout.tile_15.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.tile_15.setText(_fromUtf8(""))
        layout.tile_15.setObjectName(_fromUtf8("tile_15"))
        layout.tile_16 = QtGui.QPushButton(dialog)
        layout.tile_16.setGeometry(QtCore.QRect(626, 294, 43, 43))
        layout.tile_16.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.tile_16.setText(_fromUtf8(""))
        layout.tile_16.setObjectName(_fromUtf8("tile_16"))
        layout.tile_17 = QtGui.QPushButton(dialog)
        layout.tile_17.setGeometry(QtCore.QRect(684, 294, 43, 43))
        layout.tile_17.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.tile_17.setText(_fromUtf8(""))
        layout.tile_17.setObjectName(_fromUtf8("tile_17"))
        layout.tile_18 = QtGui.QPushButton(dialog)
        layout.tile_18.setGeometry(QtCore.QRect(742, 294, 43, 43))
        layout.tile_18.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.tile_18.setText(_fromUtf8(""))
        layout.tile_18.setObjectName(_fromUtf8("tile_18"))
        layout.tile_19 = QtGui.QPushButton(dialog)
        layout.tile_19.setGeometry(QtCore.QRect(742, 348, 43, 43))
        layout.tile_19.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.tile_19.setText(_fromUtf8(""))
        layout.tile_19.setObjectName(_fromUtf8("tile_19"))
        layout.tile_20 = QtGui.QPushButton(dialog)
        layout.tile_20.setGeometry(QtCore.QRect(742, 402, 43, 43))
        layout.tile_20.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.tile_20.setText(_fromUtf8(""))
        layout.tile_20.setObjectName(_fromUtf8("tile_20"))
        layout.tile_21 = QtGui.QPushButton(dialog)
        layout.tile_21.setGeometry(QtCore.QRect(684, 402, 43, 43))
        layout.tile_21.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.tile_21.setText(_fromUtf8(""))
        layout.tile_21.setObjectName(_fromUtf8("tile_21"))
        layout.tile_22 = QtGui.QPushButton(dialog)
        layout.tile_22.setGeometry(QtCore.QRect(626, 402, 43, 43))
        layout.tile_22.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.tile_22.setText(_fromUtf8(""))
        layout.tile_22.setObjectName(_fromUtf8("tile_22"))
        layout.tile_23 = QtGui.QPushButton(dialog)
        layout.tile_23.setGeometry(QtCore.QRect(568, 402, 43, 43))
        layout.tile_23.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.tile_23.setText(_fromUtf8(""))
        layout.tile_23.setObjectName(_fromUtf8("tile_23"))
        layout.tile_24 = QtGui.QPushButton(dialog)
        layout.tile_24.setGeometry(QtCore.QRect(510, 402, 43, 43))
        layout.tile_24.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.tile_24.setText(_fromUtf8(""))
        layout.tile_24.setObjectName(_fromUtf8("tile_24"))
        layout.tile_25 = QtGui.QPushButton(dialog)
        layout.tile_25.setGeometry(QtCore.QRect(510, 456, 43, 43))
        layout.tile_25.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.tile_25.setText(_fromUtf8(""))
        layout.tile_25.setObjectName(_fromUtf8("tile_25"))
        layout.tile_26 = QtGui.QPushButton(dialog)
        layout.tile_26.setGeometry(QtCore.QRect(510, 510, 43, 43))
        layout.tile_26.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.tile_26.setText(_fromUtf8(""))
        layout.tile_26.setObjectName(_fromUtf8("tile_26"))
        layout.tile_27 = QtGui.QPushButton(dialog)
        layout.tile_27.setGeometry(QtCore.QRect(510, 563, 43, 43))
        layout.tile_27.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.tile_27.setText(_fromUtf8(""))
        layout.tile_27.setObjectName(_fromUtf8("tile_27"))
        layout.tile_28 = QtGui.QPushButton(dialog)
        layout.tile_28.setGeometry(QtCore.QRect(510, 619, 43, 43))
        layout.tile_28.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.tile_28.setText(_fromUtf8(""))
        layout.tile_28.setObjectName(_fromUtf8("tile_28"))
        layout.tile_29 = QtGui.QPushButton(dialog)
        layout.tile_29.setGeometry(QtCore.QRect(452, 619, 43, 43))
        layout.tile_29.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.tile_29.setText(_fromUtf8(""))
        layout.tile_29.setObjectName(_fromUtf8("tile_29"))
        layout.tile_30 = QtGui.QPushButton(dialog)
        layout.tile_30.setGeometry(QtCore.QRect(394, 619, 43, 43))
        layout.tile_30.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.tile_30.setText(_fromUtf8(""))
        layout.tile_30.setObjectName(_fromUtf8("tile_30"))
        layout.tile_31 = QtGui.QPushButton(dialog)
        layout.tile_31.setGeometry(QtCore.QRect(394, 563, 43, 43))
        layout.tile_31.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.tile_31.setText(_fromUtf8(""))
        layout.tile_31.setObjectName(_fromUtf8("tile_31"))
        layout.tile_32 = QtGui.QPushButton(dialog)
        layout.tile_32.setGeometry(QtCore.QRect(394, 510, 43, 43))
        layout.tile_32.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.tile_32.setText(_fromUtf8(""))
        layout.tile_32.setObjectName(_fromUtf8("tile_32"))
        layout.tile_33 = QtGui.QPushButton(dialog)
        layout.tile_33.setGeometry(QtCore.QRect(394, 456, 43, 43))
        layout.tile_33.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.tile_33.setText(_fromUtf8(""))
        layout.tile_33.setObjectName(_fromUtf8("tile_33"))
        layout.tile_34 = QtGui.QPushButton(dialog)
        layout.tile_34.setGeometry(QtCore.QRect(394, 402, 43, 43))
        layout.tile_34.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.tile_34.setText(_fromUtf8(""))
        layout.tile_34.setObjectName(_fromUtf8("tile_34"))
        layout.tile_35 = QtGui.QPushButton(dialog)
        layout.tile_35.setGeometry(QtCore.QRect(336, 402, 43, 43))
        layout.tile_35.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.tile_35.setText(_fromUtf8(""))
        layout.tile_35.setObjectName(_fromUtf8("tile_35"))
        layout.tile_36 = QtGui.QPushButton(dialog)
        layout.tile_36.setGeometry(QtCore.QRect(281, 402, 43, 43))
        layout.tile_36.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.tile_36.setText(_fromUtf8(""))
        layout.tile_36.setObjectName(_fromUtf8("tile_36"))
        layout.tile_37 = QtGui.QPushButton(dialog)
        layout.tile_37.setGeometry(QtCore.QRect(227, 402, 43, 43))
        layout.tile_37.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.tile_37.setText(_fromUtf8(""))
        layout.tile_37.setObjectName(_fromUtf8("tile_37"))
        layout.tile_38 = QtGui.QPushButton(dialog)
        layout.tile_38.setGeometry(QtCore.QRect(172, 402, 43, 43))
        layout.tile_38.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.tile_38.setText(_fromUtf8(""))
        layout.tile_38.setObjectName(_fromUtf8("tile_38"))
        layout.tile_39 = QtGui.QPushButton(dialog)
        layout.tile_39.setGeometry(QtCore.QRect(172, 348, 43, 43))
        layout.tile_39.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.tile_39.setText(_fromUtf8(""))
        layout.tile_39.setObjectName(_fromUtf8("tile_39"))
        layout.blue_home_tile_1 = QtGui.QPushButton(dialog)
        layout.blue_home_tile_1.setGeometry(QtCore.QRect(281, 348, 43, 43))
        layout.blue_home_tile_1.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.blue_home_tile_1.setText(_fromUtf8(""))
        layout.blue_home_tile_1.setObjectName(_fromUtf8("blue_home_tile_1"))
        layout.blue_home_tile_2 = QtGui.QPushButton(dialog)
        layout.blue_home_tile_2.setGeometry(QtCore.QRect(336, 348, 43, 43))
        layout.blue_home_tile_2.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.blue_home_tile_2.setText(_fromUtf8(""))
        layout.blue_home_tile_2.setObjectName(_fromUtf8("blue_home_tile_2"))
        layout.blue_home_tile_3 = QtGui.QPushButton(dialog)
        layout.blue_home_tile_3.setGeometry(QtCore.QRect(394, 348, 43, 43))
        layout.blue_home_tile_3.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.blue_home_tile_3.setText(_fromUtf8(""))
        layout.blue_home_tile_3.setObjectName(_fromUtf8("blue_home_tile_3"))
        layout.red_home_tile_0 = QtGui.QPushButton(dialog)
        layout.red_home_tile_0.setGeometry(QtCore.QRect(452, 132, 43, 43))
        layout.red_home_tile_0.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.red_home_tile_0.setText(_fromUtf8(""))
        layout.red_home_tile_0.setObjectName(_fromUtf8("red_home_tile_0"))
        layout.red_home_tile_1 = QtGui.QPushButton(dialog)
        layout.red_home_tile_1.setGeometry(QtCore.QRect(452, 186, 43, 43))
        layout.red_home_tile_1.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.red_home_tile_1.setText(_fromUtf8(""))
        layout.red_home_tile_1.setObjectName(_fromUtf8("red_home_tile_1"))
        layout.red_home_tile_2 = QtGui.QPushButton(dialog)
        layout.red_home_tile_2.setGeometry(QtCore.QRect(452, 240, 43, 43))
        layout.red_home_tile_2.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.red_home_tile_2.setText(_fromUtf8(""))
        layout.red_home_tile_2.setObjectName(_fromUtf8("red_home_tile_2"))
        layout.red_home_tile_3 = QtGui.QPushButton(dialog)
        layout.red_home_tile_3.setGeometry(QtCore.QRect(452, 294, 43, 43))
        layout.red_home_tile_3.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.red_home_tile_3.setText(_fromUtf8(""))
        layout.red_home_tile_3.setObjectName(_fromUtf8("red_home_tile_3"))
        layout.green_home_tile_0 = QtGui.QPushButton(dialog)
        layout.green_home_tile_0.setGeometry(QtCore.QRect(684, 348, 43, 43))
        layout.green_home_tile_0.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.green_home_tile_0.setText(_fromUtf8(""))
        layout.green_home_tile_0.setObjectName(_fromUtf8("green_home_tile_0"))
        layout.green_home_tile_1 = QtGui.QPushButton(dialog)
        layout.green_home_tile_1.setGeometry(QtCore.QRect(626, 348, 43, 43))
        layout.green_home_tile_1.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.green_home_tile_1.setText(_fromUtf8(""))
        layout.green_home_tile_1.setObjectName(_fromUtf8("green_home_tile_1"))
        layout.green_home_tile_2 = QtGui.QPushButton(dialog)
        layout.green_home_tile_2.setGeometry(QtCore.QRect(568, 348, 43, 43))
        layout.green_home_tile_2.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.green_home_tile_2.setText(_fromUtf8(""))
        layout.green_home_tile_2.setObjectName(_fromUtf8("green_home_tile_2"))
        layout.green_home_tile_3 = QtGui.QPushButton(dialog)
        layout.green_home_tile_3.setGeometry(QtCore.QRect(510, 348, 43, 43))
        layout.green_home_tile_3.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.green_home_tile_3.setText(_fromUtf8(""))
        layout.green_home_tile_3.setObjectName(_fromUtf8("green_home_tile_3"))
        layout.yellow_home_tile_3 = QtGui.QPushButton(dialog)
        layout.yellow_home_tile_3.setGeometry(QtCore.QRect(452, 402, 43, 43))
        layout.yellow_home_tile_3.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.yellow_home_tile_3.setText(_fromUtf8(""))
        layout.yellow_home_tile_3.setObjectName(_fromUtf8("yellow_home_tile_3"))
        layout.yellow_home_tile_2 = QtGui.QPushButton(dialog)
        layout.yellow_home_tile_2.setGeometry(QtCore.QRect(452, 456, 43, 43))
        layout.yellow_home_tile_2.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.yellow_home_tile_2.setText(_fromUtf8(""))
        layout.yellow_home_tile_2.setObjectName(_fromUtf8("yellow_home_tile_2"))
        layout.yellow_home_tile_1 = QtGui.QPushButton(dialog)
        layout.yellow_home_tile_1.setGeometry(QtCore.QRect(452, 510, 43, 43))
        layout.yellow_home_tile_1.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.yellow_home_tile_1.setText(_fromUtf8(""))
        layout.yellow_home_tile_1.setObjectName(_fromUtf8("yellow_home_tile_1"))
        layout.yellow_home_tile_0 = QtGui.QPushButton(dialog)
        layout.yellow_home_tile_0.setGeometry(QtCore.QRect(452, 563, 43, 43))
        layout.yellow_home_tile_0.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.yellow_home_tile_0.setText(_fromUtf8(""))
        layout.yellow_home_tile_0.setObjectName(_fromUtf8("yellow_home_tile_0"))
        layout.blue_home_tile_0 = QtGui.QPushButton(dialog)
        layout.blue_home_tile_0.setGeometry(QtCore.QRect(227, 348, 43, 43))
        layout.blue_home_tile_0.setStyleSheet(_fromUtf8("background-color:TRANSPARENT;border:0;"))
        layout.blue_home_tile_0.setText(_fromUtf8(""))
        layout.blue_home_tile_0.setObjectName(_fromUtf8("blue_home_tile_0"))

        layout.title = QtGui.QLabel(dialog)
        layout.title.setGeometry(QtCore.QRect(840, 50, 381, 51))
        layout.title.setStyleSheet(
            _fromUtf8("background-image:url(graphics/title.png); background-repeat:no-repeat;"))
        layout.title.setText(_fromUtf8(""))
        layout.title.setObjectName(_fromUtf8("title"))
        layout.start_button = QtGui.QPushButton(dialog)
        layout.start_button.setGeometry(QtCore.QRect(900, 140, 248, 73))
        layout.start_button.setStyleSheet(_fromUtf8("background-color:transparent;border:0;\n"
                                                   "background-image: url(graphics/start.png);\n"
                                                   "background-repeat:no-repeat;"))
        layout.start_button.setText(_fromUtf8(""))
        layout.start_button.setObjectName(_fromUtf8("startbutton"))
        layout.dice = QtGui.QPushButton(dialog)
        layout.dice.setGeometry(QtCore.QRect(939, 430, 171, 171))
        layout.dice.setStyleSheet(_fromUtf8("background-color:transparent;border:0;\n"
                                            "background-image: url(graphics/dice1.png);\n"
                                            "background-repeat:no-repeat;"))
        layout.dice.setText(_fromUtf8(""))
        layout.dice.setObjectName(_fromUtf8("dice"))
        layout.turn_alert_label = QtGui.QLabel(dialog)
        layout.turn_alert_label.setGeometry(QtCore.QRect(920, 390, 221, 31))
        layout.turn_alert_label.setStyleSheet(_fromUtf8("font-size:19px"))
        layout.turn_alert_label.setObjectName(_fromUtf8("label_2"))
        layout.player_color_label = QtGui.QLabel(dialog)
        layout.player_color_label.setGeometry(QtCore.QRect(950, 240, 111, 41))
        layout.player_color_label.setStyleSheet(_fromUtf8("font-size:20px"))
        layout.player_color_label.setObjectName(_fromUtf8("label_4"))
        layout.player_color_placeholder = QtGui.QLabel(dialog)
        layout.player_color_placeholder.setGeometry(QtCore.QRect(1060, 240, 43, 44))
        layout.player_color_placeholder.setStyleSheet(REMOVE_CSS_STYLE)
        layout.player_color_placeholder.setText(_fromUtf8(""))
        layout.player_color_placeholder.setObjectName(_fromUtf8("label_5"))
        layout.player_color_label.setText(_translate("dialog", EMPTY_TEXT, None))
        layout.turn_alert_label.setText(_translate("dialog", EMPTY_TEXT, None))
