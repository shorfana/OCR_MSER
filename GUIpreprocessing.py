from PyQt5 import QtCore, QtGui, QtWidgets
import cv2 
import mysql.connector
import matplotlib.pyplot as plt
from matrix.Preprocessing import Preprocessing
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1103, 585)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1101, 581))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btnKembali = QtWidgets.QPushButton(self.frame)
        self.btnKembali.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.btnKembali.setObjectName("btnKembali")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(20, 50, 1081, 521))
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
        self.lblPreview = QtWidgets.QLabel(self.vPreview)
        self.lblPreview.setGeometry(QtCore.QRect(10, 10, 341, 351))
        self.lblPreview.setObjectName("lblPreview")
        self.btnProses = QtWidgets.QPushButton(self.groupBox_2)
        self.btnProses.setGeometry(QtCore.QRect(20, 440, 75, 23))
        self.btnProses.setObjectName("btnProses")
        self.vHasil = QtWidgets.QGroupBox(self.groupBox)
        self.vHasil.setGeometry(QtCore.QRect(420, 30, 651, 471))
        self.vHasil.setObjectName("vHasil")
        self.lblGrayscale = QtWidgets.QLabel(self.vHasil)
        self.lblGrayscale.setGeometry(QtCore.QRect(50, 50, 211, 171))
        self.lblGrayscale.setFrameShape(QtWidgets.QFrame.Panel)
        self.lblGrayscale.setObjectName("lblGrayscale")
        self.lblThresholding = QtWidgets.QLabel(self.vHasil)
        self.lblThresholding.setGeometry(QtCore.QRect(360, 50, 211, 171))
        self.lblThresholding.setFrameShape(QtWidgets.QFrame.Panel)
        self.lblThresholding.setObjectName("lblThresholding")
        self.lblThinning = QtWidgets.QLabel(self.vHasil)
        self.lblThinning.setGeometry(QtCore.QRect(210, 280, 211, 171))
        self.lblThinning.setFrameShape(QtWidgets.QFrame.Panel)
        self.lblThinning.setObjectName("lblThinning")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.btn_PilihFile.clicked.connect(self.clickFile)
        self.btnProses.clicked.connect(self.pengolahanData)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btnKembali.setText(_translate("Dialog", "Kembali"))
        self.groupBox.setTitle(_translate("Dialog", "Preprocessing"))
        self.groupBox_2.setTitle(_translate("Dialog", "Gambar"))
        self.btn_PilihFile.setText(_translate("Dialog", "Pilih File"))
        self.vPreview.setTitle(_translate("Dialog", "Preview"))
        self.lblPreview.setText(_translate("Dialog", "Preview Image"))
        self.btnProses.setText(_translate("Dialog", "Proses"))
        self.vHasil.setTitle(_translate("Dialog", "Hasil"))
        self.lblGrayscale.setText(_translate("Dialog", "Grayscale"))
        self.lblThresholding.setText(_translate("Dialog", "Sauvola Thresholding"))
        self.lblThinning.setText(_translate("Dialog", "Zhang Suen Thinning"))

    def clickFile(self):
        global fileName
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "Image File (*.png *.jpg *.jpeg)")
        if fileName:
            self.lblPreview.setText(fileName)
            pixmap = QtGui.QPixmap(fileName)
            pixmap = pixmap.scaled(self.lblPreview.width(), self.lblPreview.height(), QtCore.Qt.KeepAspectRatio)
            self.lblPreview.setPixmap(pixmap)
            self.lblPreview.setAlignment(QtCore.Qt.AlignCenter) 
            # image = cv2.imread(fileName)
            # grayImg = grayscale(image)
            # thresImge        = thresholding(grayImg)
            # # zero            = padding_zeros(thresImge)
            # thinnImg        = zhangSuen(thresImge)
            # segmnImg        = segmentasi(thinnImg,grayImage) 
            # plt.figure()
            # plt.imshow(grayImg, cmap=plt.cm.gray)
            # plt.title('deteksi MSER')
            # plt.axis('off')
            # plt.show()
            

    def pengolahanData(self):
        image = cv2.imread(fileName)
        grayImg     = grayscale(image)
        thresImg    = thresholding(grayImg)
        thinnImg    = zhangSuen(thresImg)
        #grayscale
        cv2.imwrite("hasil_proses/Grayscale.jpg", grayImg)
        pixmap = QtGui.QPixmap("hasil_proses/Grayscale.jpg")
        pixmap = pixmap.scaled(self.lblGrayscale.width(), self.lblGrayscale.height(), QtCore.Qt.KeepAspectRatio)
        self.lblGrayscale.setPixmap(pixmap)
        self.lblGrayscale.setAlignment(QtCore.Qt.AlignCenter) 

        # thresholding
        cv2.imwrite("hasil_proses/Thresholding.jpg", thresImg)
        pixmap = QtGui.QPixmap("hasil_proses/Thresholding.jpg")
        pixmap = QtGui.QPixmap(fileName)
        pixmap = pixmap.scaled(self.lblThresholding.width(), self.lblThresholding.height(), QtCore.Qt.KeepAspectRatio)
        self.lblThresholding.setPixmap(pixmap)
        self.lblThresholding.setAlignment(QtCore.Qt.AlignCenter) 

        # Thinning
        cv2.imwrite("hasil_proses/Thinning.jpg", thresImg)
        pixmap = QtGui.QPixmap("hasil_proses/Thinning.jpg")
        pixmap = QtGui.QPixmap(fileName)
        pixmap = pixmap.scaled(self.lblThinning.width(), self.lblThinning.height(), QtCore.Qt.KeepAspectRatio)
        self.lblThinning.setPixmap(pixmap)
        self.lblThinning.setAlignment(QtCore.Qt.AlignCenter) 




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
