import sys
import os
from PyQt5.QtWidgets import QWidget,QApplication,QRadioButton,QLabel,QPushButton,QVBoxLayout,QTextEdit,QFileDialog,QHBoxLayout
from PyQt5.QtWidgets import QAction,qApp,QMainWindow
class NotePad(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.yaziAlani= QTextEdit()
        self.temizle= QPushButton("Temizle")
        self.ac= QPushButton("Aç")
        self.kaydet= QPushButton("Kaydet")

        h_box= QHBoxLayout()
        h_box.addWidget(self.temizle)
        h_box.addWidget(self.ac)
        h_box.addWidget(self.kaydet)

        v_box= QVBoxLayout()
        v_box.addWidget(self.yaziAlani)
        v_box.addLayout(h_box)

        self.setLayout(v_box)
        self.setWindowTitle("NotePad")
        self.temizle.clicked.connect(self.yaziTemizle)
        self.ac.clicked.connect(self.dosyaAc)
        self.kaydet.clicked.connect(self.dosyaKaydet)
       
    def yaziTemizle(self):
        self.yaziAlani.clear()
    def dosyaAc(self):
        
        dosya_ismi = QFileDialog.getOpenFileName(self,"Dosya Aç",os.getenv("HOME"))

        with open(dosya_ismi[0],"r") as file:

            self.yaziAlani.setText(file.read())

    def dosyaKaydet(self):
        dosya_ismi = QFileDialog.getSaveFileName(self,"Dosya Kaydet",os.getenv("HOME"))

        with open(dosya_ismi[0],"w") as file:

            file.write(self.yaziAlani.toPlainText()) 
class Menu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.pencere=NotePad()
        self.setCentralWidget(self.pencere)
        self.menuleriOlustur()
    
    def menuleriOlustur(self):

        menubar= self.menuBar()
        dosya= menubar.addMenu("Dosya")

        dosya_ac= QAction("Dosya Aç",self)
        dosya_ac.setShortcut("Ctrl+O")

        dosya_kaydet=QAction("Dosya Kaydet",self)
        dosya_kaydet.setShortcut("Ctrl+S")

        temizle= QAction("Temizle",self)
        temizle.setShortcut("Ctrl+D")

        cikis= QAction("Çıkış",self)
        cikis.setShortcut("Ctrl+Q")

        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(temizle)
        dosya.addAction(cikis)

        dosya.triggered.connect(self.response)

        self.setWindowTitle("Metin Editörü")

        self.show()

    def response(self,action):

            if action.text() == "Dosya Aç":
                self.pencere.dosyaAc()
            elif action.text() == "Dosya Kaydet":
                self.pencere.dosyaKaydet()
            elif action.text() == "Temizle":
                self.pencere.yaziTemizle()
            elif action.text() == "Çıkış":
                qApp.quit()




app = QApplication(sys.argv)
menu= Menu()
sys.exit(app.exec_())