import os
import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *




class CuteZilla(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(CuteZilla, self).__init__()
        
        QWebSettings.globalSettings().setAttribute(QWebSettings.PluginsEnabled, True)
        self.browser = QWebView()
        
        self.setupInspector()
       
        self.splitter = QSplitter(self)
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.addWidget(self.browser)
        self.splitter.addWidget(self.webInspector)

        self.browser.setUrl(QUrl("http://google.com"))
        self.setCentralWidget(self.splitter)

        nav_tab = QToolBar("navigation")
        self.addToolBar(nav_tab)

        back_btn = QAction(QIcon(os.path.join("icon", "arrow-180.png")),"back",self)
        back_btn.setStatusTip("back")
        back_btn.triggered.connect(self.browser.back)
        nav_tab.addAction(back_btn)

        forward_btn = QAction(QIcon(os.path.join("icon", "arrow-000.png")),"forward",self)
        forward_btn.setStatusTip("forward")
        forward_btn.triggered.connect(self.browser.forward)
        nav_tab.addAction(forward_btn)

        reload_btn = QAction(QIcon(os.path.join("icon", "arrow-circle.png")),"reload",self)
        reload_btn.setStatusTip("reload")
        nav_tab.addAction(reload_btn)
        reload_btn.triggered.connect(self.browser.reload)
       
        self.url_input = QLineEdit()
        self.url_input.returnPressed.connect(self.update_page)
        nav_tab.addSeparator()
        nav_tab.addWidget(self.url_input)

        close_btn = QAction(QIcon(os.path.join("icon", "cross-circle.png")),"close",self)
        close_btn.setStatusTip("close")
        nav_tab.addAction(close_btn)
        close_btn.triggered.connect(self.browser.close)

        self.browser.urlChanged.connect(self.update_urlbar)

        self.show()
        self.setWindowTitle("Cute Zilla")
        self.setWindowIcon(QIcon(os.path.join("icon", "leaf-red.png")))
    
    def update_urlbar(self,url_object):
        self.url_input.setText(url_object.toString())
        self.url_input.setCursorPosition(0)
    
    def update_page(self):
        url = QUrl(self.url_input.text())
        if url.scheme() == "":
            url.setScheme("http")
        self.browser.setUrl(url)

    def setupInspector(self):
        page = self.browser.page()
        page.settings().setAttribute(QWebSettings.DeveloperExtrasEnabled, True)
        self.webInspector = QWebInspector(self)
        self.webInspector.setPage(page)
        shortcut = QShortcut(self)
        shortcut.setKey(Qt.Key_F12)
        shortcut.activated.connect(self.toggleInspector)
        self.webInspector.setVisible(False)
    

    def toggleInspector(self):
        self.webInspector.setVisible(not self.webInspector.isVisible())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("Cute Zilla")
    app.setOrganizationDomain("Cute Zilla.org")
    app.setOrganizationName("Cute Zilla org")
    browser = CuteZilla()
    browser.show()
    app.exec_()

#https://www.youtube.com/watch?v=qVqWMjChtPk