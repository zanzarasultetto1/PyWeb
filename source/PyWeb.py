import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QToolBar, QAction, QLineEdit, QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        self.navbar = QToolBar()
        self.addToolBar(self.navbar)

        self.home_btn = QAction('Home', self)
        self.home_btn.triggered.connect(self.navigate_home)
        self.navbar.addAction(self.home_btn)

        self.back_btn = QAction('Back', self)
        self.back_btn.triggered.connect(self.browser.back)
        self.navbar.addAction(self.back_btn)

        self.forward_btn = QAction('Forward', self)
        self.forward_btn.triggered.connect(self.browser.forward)
        self.navbar.addAction(self.forward_btn)

        self.reload_btn = QAction('Reload', self)
        self.reload_btn.triggered.connect(self.browser.reload)
        self.navbar.addAction(self.reload_btn)

        self.about_btn = QAction('About', self)
        self.about_btn.triggered.connect(self.about)
        self.navbar.addAction(self.about_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

    def about(self):
        msg = QMessageBox()
        msg.setWindowTitle('About')
        msg.setText("PyWeb, 9/24/21, Mariano C.se\nPietro Marelli")
        msg.setIcon(QMessageBox.Information)

        msg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    QApplication.setApplicationName('PyWeb')
    window = MainWindow()
    app.exec_()
