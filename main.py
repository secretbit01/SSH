import sys
import os
import pygetwindow as gw
from pynput.keyboard import Key, Controller
from PyQt6 import uic, QtWidgets
from time import sleep

from config import *

cd_history = []

class Ui(QtWidgets.QDialog):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('app.ui', self)

        self.Norma_usdt_closeButton.clicked.connect(lambda: self.close_connection('Norma_usdt'))
        self.Norma_usdt_connectButton.clicked.connect(lambda: self.connect(ssh_Norma_usdt_host, ssh_Norma_usdt_user, ssh_Norma_usdt_pwd, 'Norma_usdt'))
        self.Norma_usdt_killButton.clicked.connect(lambda: self.send(command_Norma_usdt_killBotton, 'Norma_usdt'))
        self.Norma_usdt_startButton.clicked.connect(lambda: self.send(command_Norma_usdt_startBotton, 'Norma_usdt'))
        self.Norma_usdt_stopButton.clicked.connect(lambda: self.send(command_Norma_usdt_stopBotton, 'Norma_usdt'))

        self.Norma_btc_closeButton.clicked.connect(lambda: self.close_connection('Norma_btc'))
        self.Norma_btc_connectButton.clicked.connect(lambda: self.connect(ssh_Norma_btc_host, ssh_Norma_btc_user, ssh_Norma_btc_pwd, 'Norma_btc'))
        self.Norma_btc_killButton.clicked.connect(lambda: self.send(command_Norma_btc_killBotton, 'Norma_btc'))
        self.Norma_btc_startButton.clicked.connect(lambda: self.send(command_Norma_btc_startBotton, 'Norma_btc'))
        self.Norma_btc_stopButton.clicked.connect(lambda: self.send(command_Norma_btc_stopBotton, 'Norma_btc'))

        self.Kuoter_closeButton.clicked.connect(lambda: self.close_connection('Kuoter'))
        self.Kuoter_connectButton.clicked.connect(lambda: self.connect(ssh_Kuoter_host, ssh_Kuoter_user, ssh_Kuoter_pwd, 'Kuoter'))
        self.Kuoter_killButton.clicked.connect(lambda: self.send(command_Kuoter_killBotton, 'Kuoter'))
        self.Kuoter_startButton.clicked.connect(lambda: self.send(command_Kuoter_startBotton, 'Kuoter'))
        self.Kuoter_stopButton.clicked.connect(lambda: self.send(command_Kuoter_stopBotton, 'Kuoter'))

        self.Lettore_closeButton.clicked.connect(lambda: self.close_connection('Lettore'))
        self.Lettore_connectButton.clicked.connect(lambda: self.connect(ssh_Lettore_host, ssh_Lettore_user, ssh_Lettore_pwd, 'Lettore'))
        self.Lettore_startButton.clicked.connect(lambda: self.send(command_Lettore_startBotton, 'Lettore'))
        self.Lettore_stopButton.clicked.connect(lambda: self.send(command_Lettore_stopBotton, 'Lettore'))

        self.Glmr_closeButton.clicked.connect(lambda: self.close_connection('Glmr'))
        self.Glmr_connectButton.clicked.connect(lambda: self.connect(ssh_Glmr_host, ssh_Glmr_user, ssh_Glmr_pwd, 'Glmr'))
        self.Glmr_startButton.clicked.connect(lambda: self.send(command_Glmr_startBotton, 'Glmr'))
        self.Glmr_stopButton.clicked.connect(lambda: self.send(command_Glmr_stopBotton, 'Glmr'))

        self.show()

    def send_command_to_cmd(self, command):
        try:
            win = gw.getWindowsWithTitle('cmd.exe')[0]
        except:
            win = gw.getWindowsWithTitle('root')[0]

        win.activate()
        sleep(1)
        keyboard = Controller()
        keyboard.type(command)
        keyboard.press(Key.enter)

    def connect(self, host, user, pwd, server):
        try:
            os.system('start')
            sleep(1)

            self.send_command_to_cmd(f'ssh {user}@{host}')
            sleep(5)
            self.send_command_to_cmd(pwd)

            if server == 'Norma_usdt':
                self.Norma_usdt_closeButton.setEnabled(True)
                self.Norma_usdt_connectButton.setEnabled(False)
                self.Norma_usdt_killButton.setEnabled(True)
                self.Norma_usdt_startButton.setEnabled(True)
                self.Norma_usdt_stopButton.setEnabled(True)

            if server == 'Norma_btc':
                self.Norma_btc_closeButton.setEnabled(True)
                self.Norma_btc_connectButton.setEnabled(False)
                self.Norma_btc_killButton.setEnabled(True)
                self.Norma_btc_startButton.setEnabled(True)
                self.Norma_btc_stopButton.setEnabled(True)

            if server == 'Kuoter':
                self.Kuoter_closeButton.setEnabled(True)
                self.Kuoter_connectButton.setEnabled(False)
                self.Kuoter_killButton.setEnabled(True)
                self.Kuoter_startButton.setEnabled(True)
                self.Kuoter_stopButton.setEnabled(True)

            if server == 'Lettore':
                self.Lettore_closeButton.setEnabled(True)
                self.Lettore_connectButton.setEnabled(False)
                self.Lettore_startButton.setEnabled(True)
                self.Lettore_stopButton.setEnabled(True)

            if server == 'Glmr':
                self.Glmr_closeButton.setEnabled(True)
                self.Glmr_connectButton.setEnabled(False)
                self.Glmr_startButton.setEnabled(True)
                self.Glmr_stopButton.setEnabled(True)
        except Exception as e:
            print(e)
            pass

    def close_connection(self, server):
        try:
            win = gw.getWindowsWithTitle('cmd.exe')[0]
        except:
            win = gw.getWindowsWithTitle('root')[0]
        
        win.close()

        if server == 'Norma_usdt':
            self.Norma_usdt_closeButton.setEnabled(False)
            self.Norma_usdt_connectButton.setEnabled(True)
            self.Norma_usdt_killButton.setEnabled(False)
            self.Norma_usdt_startButton.setEnabled(False)
            self.Norma_usdt_stopButton.setEnabled(False)

        if server == 'Norma_btc':
            self.Norma_btc_closeButton.setEnabled(False)
            self.Norma_btc_connectButton.setEnabled(True)
            self.Norma_btc_killButton.setEnabled(False)
            self.Norma_btc_startButton.setEnabled(False)
            self.Norma_btc_stopButton.setEnabled(False)

        if server == 'Kuoter':
            self.Kuoter_closeButton.setEnabled(False)
            self.Kuoter_connectButton.setEnabled(True)
            self.Kuoter_killButton.setEnabled(False)
            self.Kuoter_startButton.setEnabled(False)
            self.Kuoter_stopButton.setEnabled(False)

        if server == 'Lettore':
            self.Lettore_closeButton.setEnabled(False)
            self.Lettore_connectButton.setEnabled(True)
            self.Lettore_startButton.setEnabled(False)
            self.Lettore_stopButton.setEnabled(False)

        if server == 'Glmr':
            self.Glmr_closeButton.setEnabled(False)
            self.Glmr_connectButton.setEnabled(True)
            self.Glmr_startButton.setEnabled(False)
            self.Glmr_stopButton.setEnabled(False)

    def start(self, server):
        pass

    def stop(self, server):
        pass

    def send(self, command, server):
        self.send_command_to_cmd(command)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec()
