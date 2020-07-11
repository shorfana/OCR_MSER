from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Preprocessing")
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
        self.groupBox.setGeometry(QtCore.QRect(20, 50, 871, 521))
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 30, 391, 471))
        self.groupBox_2.setObjectName("groupBox_2")
        self.btn_PilihFile = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_PilihFile.setGeometry(QtCore.QRect(20, 30, 75, 23))
        self.btn_PilihFile.setObjectName("btn_PilihFile")
        self.vPreview = QtWidgets.QGroupBox(self.groupBox_2)
        self.vPreview.setGeometry(QtCore.QRect(20, 60, 361, 371))
        self.vPreview.setObjectName("vPreview")
        self.btnProses = QtWidgets.QPushButton(self.groupBox_2)
        self.btnProses.setGeometry(QtCore.QRect(20, 440, 75, 23))
        self.btnProses.setObjectName("btnProses")
        self.vHasil = QtWidgets.QGroupBox(self.groupBox)
        self.vHasil.setGeometry(QtCore.QRect(420, 30, 441, 471))
        self.vHasil.setObjectName("vHasil")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Preprocessing"))
        self.btnKembali.setText(_translate("Dialog", "Kembali"))
        self.groupBox.setTitle(_translate("Dialog", "Preprocessing"))
        self.groupBox_2.setTitle(_translate("Dialog", "Gambar"))
        self.btn_PilihFile.setText(_translate("Dialog", "Pilih File"))
        self.vPreview.setTitle(_translate("Dialog", "Preview"))
        self.btnProses.setText(_translate("Dialog", "Proses"))
        self.vHasil.setTitle(_translate("Dialog", "Hasil"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
