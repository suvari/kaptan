from PyQt5.QtWidgets import QWizardPage, QLabel, QGroupBox, QRadioButton, QHBoxLayout, QVBoxLayout, QCheckBox, \
    QSpacerItem, QSizePolicy, QButtonGroup
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import *

from os.path import join

Description = "<p><strong>Tıklama Biçimi</strong> dosya açarken simgelere kaç kere tıklamanız gerektiğini belirlemenize yardımcı olur. \
Eğer <strong>sol elinizi</strong> kullanıyorsanız, fare butonlarının yerini değiştirerek farenizi daha rahat kullanabilirsiniz.</p>"

class MouseWidget(QWizardPage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSubTitle(self.tr("<h2>Fare Tıklama Davranışını Belirleyin</h2>"))


        vlayout = QVBoxLayout(self)

        labelLayout = QHBoxLayout()
        imageLabel = QLabel()
        imageLabel.setPixmap(QPixmap(":/data/images/preferences-desktop-peripherals.png"))
        imageLabel.setMaximumSize(64, 64)
        labelLayout.addWidget(imageLabel)

        mouseLabel = QLabel(self)
        mouseLabel.setText(self.tr(Description))
        mouseLabel.setWordWrap(True)
        labelLayout.addWidget(mouseLabel)
        vlayout.addLayout(labelLayout)

        vlayout.addItem(QSpacerItem(20, 100, QSizePolicy.Preferred, QSizePolicy.Preferred))

        hlayout = QHBoxLayout()
        vlayout.addLayout(hlayout)

        self.createGroupBox(hlayout)

        vlayout.addItem(QSpacerItem(20, 40, QSizePolicy.Preferred, QSizePolicy.Preferred))

        self.folderSingleClick = False
        self.mouseButtonMap = "RightHanded"
        self.reverseScrollPolarity = False


    def createGroupBox(self, layout):
        group1 = QGroupBox(self)
        group1.setTitle(self.tr("Tıklama Biçimi"))
        group1.setMinimumHeight(150)
        group1.setMaximumWidth(300)
        layout.addWidget(group1)

        vlayout1 = QVBoxLayout(group1)
        buttonGroup = QButtonGroup(group1)

        self.radiobutton1 = QRadioButton(group1)
        self.radiobutton1.setText(self.tr("Dosya ve dizinleri açmak için çift tıkla."))
        self.radiobutton1.setChecked(True)
        vlayout1.addWidget(self.radiobutton1)

        self.radiobutton2 = QRadioButton(group1)
        self.radiobutton2.setText(self.tr("Dosya ve dizinleri açmak için tek tıkla."))
        vlayout1.addWidget(self.radiobutton2)

        buttonGroup.addButton(self.radiobutton1)
        buttonGroup.addButton(self.radiobutton2)

        buttonGroup.buttonClicked.connect(self.folderClick)

        group2 = QGroupBox(self)
        group2.setTitle(self.tr("Düğme Sırası"))
        group2.setMinimumHeight(150)
        group2.setMaximumWidth(300)
        layout.addWidget(group2)

        vlayout2 = QVBoxLayout(group2)
        buttonGroup2 = QButtonGroup(group2)

        self.radiobutton3 = QRadioButton(group2)
        self.radiobutton3.setText(self.tr("Sağ el."))
        self.radiobutton3.setChecked(True)
        vlayout2.addWidget(self.radiobutton3)

        self.radiobutton4 = QRadioButton(group2)
        self.radiobutton4.setText(self.tr("Sol el."))
        vlayout2.addWidget(self.radiobutton4)

        buttonGroup2.addButton(self.radiobutton3)
        buttonGroup2.addButton(self.radiobutton4)

        buttonGroup2.buttonClicked.connect(self.mouseButton)

        self.checkbox = QCheckBox(group2)
        self.checkbox.setText(self.tr("Tekerlek ters kaydırsın."))
        self.checkbox.clicked.connect(self.reverseScroll)
        vlayout2.addWidget(self.checkbox)

    def folderClick(self, button):
        if button == self.radiobutton1:
            self.folderSingleClick = False
        else:
            self.folderSingleClick = True

    def mouseButton(self, button):
        if button == self.radiobutton3:
            self.mouseButtonMap = "RightHanded"
        else:
            self.mouseButtonMap = "LeftHanded"

    def reverseScroll(self):
        if self.checkbox.isChecked():
            self.reverseScrollPolarity = True
        else:
            self.reverseScrollPolarity = False

    def execute(self):
        settings1 = QSettings(join(QDir.homePath(), ".config5", "kcminputrc"), QSettings.IniFormat)
        settings2 = QSettings(join(QDir.homePath(), ".config5", "kdeglobals"), QSettings.IniFormat)

        settings1.setValue("Mouse/MouseButtonMapping", self.mouseButtonMap)
        settings1.setValue("Mouse/ReverseScrollPolarity", self.reverseScrollPolarity)
        settings1.sync()

        settings2.setValue("KDE/SingleClick", self.folderSingleClick)
        settings2.sync()