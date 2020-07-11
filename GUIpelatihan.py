# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pelatihan.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Pelatihan")
        Dialog.resize(906, 585)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 901, 581))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btnKembali = QtWidgets.QPushButton(self.frame)
        self.btnKembali.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.btnKembali.setObjectName("btnKembali")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(10, 40, 881, 531))
        self.groupBox.setObjectName("groupBox")
        self.btnProses = QtWidgets.QPushButton(self.groupBox)
        self.btnProses.setGeometry(QtCore.QRect(10, 30, 75, 23))
        self.btnProses.setObjectName("btnProses")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Pelatihan"))
        self.btnKembali.setText(_translate("Dialog", "Kembali"))
        self.groupBox.setTitle(_translate("Dialog", "Pelatihan"))
        self.btnProses.setText(_translate("Dialog", "Proses"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
