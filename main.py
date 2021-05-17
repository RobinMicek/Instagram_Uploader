from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from instabot import Bot

from notifypy import Notify

import os
import sys
import time

bot = Bot()

class Uploader(QFrame):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Instagram Uploader")
        self.setBaseSize(500, 100)

        #Login
        self.lausername = QLabel(self)
        self.lausername.setText("Username:")
        self.lapassword = QLabel(self)
        self.lapassword.setText("Password:")

        self.inputusername = QLineEdit(self)
        self.inputpassword = QLineEdit(self)
        self.inputpassword.setEchoMode(QLineEdit.Password)

        self.loginbutton = QPushButton(self)
        self.loginbutton.setText("Log In")
        self.loginbutton.clicked.connect(self.Login)

        #Label
        self.label = QLabel(self)
        self.label.setText("Waiting to inicialize...\n")

        #TextInput
        self.textinput = QLineEdit(self)
        self.textinput.setText("Write here your comment or leave blank")


        #Button
        self.button = QPushButton()
        self.button.setText("Upload")
        self.button.clicked.connect(self.Upload)

        self.ui()
        self.Update_File_Status()

    def ui(self):
        layout = QVBoxLayout()

        layout.addWidget(self.label)

        layout.addWidget(self.textinput)
        layout.addWidget(self.button)

        layout.addWidget(self.lausername)
        layout.addWidget(self.inputusername)
        layout.addWidget(self.lapassword)
        layout.addWidget(self.inputpassword)
        layout.addWidget(self.loginbutton)

        self.setLayout(layout)
        self.show()

    def Update_File_Status(self):
        if os.path.isfile("image.jpeg"):
            self.label.setText("image.jpeg was found successfully...")

        else:
            self.label.setText("image.jpeg is missing!")

    def Login(self):
        bot.login(username=str(self.inputusername.text()),
                      password=str(self.inputpassword.text()))

        self.Notification("Instagram Uploader", "You have been successfully logged in.")
        self.loginbutton.setText("You Are Logged In")

    def Upload(self):
        if os.path.isfile("image.jpeg"):
            bot.upload_photo("image.jpeg", caption=str(self.textinput.text()))
            os.rename("image.jpeg.REMOVE_ME", "image.jpeg")

        else:
            self.button.setText("No image found...")


        self.Notification("Instagram Uploader", "Picture has been uploaded successfully.")

    def Notification(self, Title, Message):
        notification = Notify()
        notification.title = str(Title)
        notification.message = str(Message)
        notification.audio = "notify.wav"

        notification.send()



while __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Uploader()
    sys.exit(app.exec())
