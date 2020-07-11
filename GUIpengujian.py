# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pengujian.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Pengujian")
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
        self.groupBox.setGeometry(QtCore.QRect(10, 40, 881, 541))
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 20, 391, 501))
        self.groupBox_2.setObjectName("groupBox_2")
        self.btnPilihFile = QtWidgets.QPushButton(self.groupBox_2)
        self.btnPilihFile.setGeometry(QtCore.QRect(10, 20, 75, 23))
        self.btnPilihFile.setObjectName("btnPilihFile")
        self.vPreview = QtWidgets.QFrame(self.groupBox_2)
        self.vPreview.setGeometry(QtCore.QRect(10, 50, 371, 411))
        self.vPreview.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.vPreview.setFrameShadow(QtWidgets.QFrame.Raised)
        self.vPreview.setObjectName("vPreview")
        self.btnProses = QtWidgets.QPushButton(self.groupBox_2)
        self.btnProses.setGeometry(QtCore.QRect(10, 470, 75, 23))
        self.btnProses.setObjectName("btnProses")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(410, 20, 461, 491))
        self.groupBox_3.setObjectName("groupBox_3")
        self.vHasilPengujian = QtWidgets.QFrame(self.groupBox_3)
        self.vHasilPengujian.setGeometry(QtCore.QRect(10, 50, 441, 411))
        self.vHasilPengujian.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.vHasilPengujian.setFrameShadow(QtWidgets.QFrame.Raised)
        self.vHasilPengujian.setObjectName("vHasilPengujian")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Pengujian"))
        self.btnKembali.setText(_translate("Dialog", "Kembali"))
        self.groupBox.setTitle(_translate("Dialog", "Pengujian"))
        self.groupBox_2.setTitle(_translate("Dialog", "Gambar"))
        self.btnPilihFile.setText(_translate("Dialog", "Pilih File"))
        self.btnProses.setText(_translate("Dialog", "Proses"))
        self.groupBox_3.setTitle(_translate("Dialog", "Hasil"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
