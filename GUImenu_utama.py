from PyQt5 import QtCore, QtGui, QtWidgets
import GUIpelatihan
import GUIpengujian
import GUIpreprocessing

class Ui_OCR_Sertifikat(object):
    def setupUi(self, OCR_Sertifikat):
        OCR_Sertifikat.setObjectName("OCR_Sertifikat")
        OCR_Sertifikat.resize(452, 344)
        self.frame1 = QtWidgets.QFrame(OCR_Sertifikat)
        self.frame1.setGeometry(QtCore.QRect(0, 0, 451, 341))
        self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1.setObjectName("frame1")
        self.label = QtWidgets.QLabel(self.frame1)
        self.label.setGeometry(QtCore.QRect(160, 80, 141, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame1)
        self.label_2.setGeometry(QtCore.QRect(130, 120, 221, 16))
        self.label_2.setObjectName("label_2")
        self.btnPelatihan = QtWidgets.QPushButton(self.frame1)
        self.btnPelatihan.setGeometry(QtCore.QRect(230, 170, 75, 23))
        self.btnPelatihan.setObjectName("btnPelatihan")
        self.btnPengujian = QtWidgets.QPushButton(self.frame1)
        self.btnPengujian.setGeometry(QtCore.QRect(310, 170, 75, 23))
        self.btnPengujian.setObjectName("btnPengujian")
        self.btnPreprocessing = QtWidgets.QPushButton(self.frame1)
        self.btnPreprocessing.setGeometry(QtCore.QRect(70, 170, 151, 23))
        self.btnPreprocessing.setObjectName("btnPreprocessing")
        self.label_3 = QtWidgets.QLabel(self.frame1)
        self.label_3.setGeometry(QtCore.QRect(260, 320, 191, 20))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(OCR_Sertifikat)
        QtCore.QMetaObject.connectSlotsByName(OCR_Sertifikat)
        self.btnPelatihan.clicked.connect(self.launchPelatihan)
        self.btnPengujian.clicked.connect(self.launchPengujian)
        self.btnPreprocessing.clicked.connect(self.launchPreprocessing)

    def retranslateUi(self, OCR_Sertifikat):
        _translate = QtCore.QCoreApplication.translate
        OCR_Sertifikat.setWindowTitle(_translate("OCR_Sertifikat", "OCR Sertifikat"))
        self.label.setText(_translate("OCR_Sertifikat", "Program OCR Pada Sertifikat"))
        self.label_2.setText(_translate("OCR_Sertifikat", "Maximally Stable Extremal Regions dan SVM"))
        self.btnPelatihan.setText(_translate("OCR_Sertifikat", "Pelatihan"))
        self.btnPengujian.setText(_translate("OCR_Sertifikat", "Pengujian"))
        self.btnPreprocessing.setText(_translate("OCR_Sertifikat", "Preprocessing / olah data"))
        self.label_3.setText(_translate("OCR_Sertifikat", "10116465 - Muhammad Iqbal Shorfana"))

    def launchPelatihan(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = GUIpelatihan.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint)
        self.window.show()

    def launchPengujian(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = GUIpengujian.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint)
        self.window.show()

    def launchPreprocessing(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = GUIpreprocessing.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint)
        self.window.show()    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OCR_Sertifikat = QtWidgets.QDialog()
    ui = Ui_OCR_Sertifikat()
    ui.setupUi(OCR_Sertifikat)
    OCR_Sertifikat.show()
    sys.exit(app.exec_())
