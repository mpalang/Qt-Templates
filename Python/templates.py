# =============================================================================
# Panel
# =============================================================================

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QFrame,
    QTabWidget,
)

from PySide6.QtCore import Signal


class Panel(QWidget):
    """
    A template for a Panel widget that handles it's 
    contents independently and only passes certain signals.
    """
    
    requested = Signal()
    
    def __init__(self):
        super().__init__()
        # Data Tweak
        
        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)

        self.layout = QGridLayout()
        frame.setLayout(self.layout)
        
        self.create_ui()
        self.create_connections()
        
        central = QVBoxLayout()
        self.setLayout(central)
        central.addWidget(frame)
    
    def create_elements(self):
        pass
    
    def create_layout(self):
        layout = self.layout

    def create_connections(self):
        pass
    
    def validate(self):
        pass

        
# =============================================================================
# Main Window
# =============================================================================

import sys
from pathlib import Path
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QLabel,
    QFrame,
    QTabWidget,
    QMessageBox,
    QTextEdit,
    QToolBar,
    QStyle,
)
from PySide6.QtGui import QFont, QIcon

from PySide6.QtGui import QAction
from PySide6.QtCore import QThread

__version__ = None

class MainWindow(QMainWindow):
    """This is a Main Window."""
    def __init__(self):
        super().__init__()

        self.setWindowTitle(f"Title v{__version__}")
        
        #Geometrics
        self.resize(1200, 500)
        # screen = QApplication.primaryScreen().availableGeometry()
        # window = self.frameGeometry()
        # window.moveCenter(screen.center())
        self.move(100,50)
        
        #Load and initialize
        self.initialize()
        self.create_menu()
        self.create_toolbar()
        self.create_elements()
        self.create_layout()
        self.create_connections()
        self.create_status_bar()
        
    def initialize(self):
        pass
    
    def create_menu(self):
        menu = self.menuBar()
        
        #File Menu
        file_menu = menu.addMenu("File")
        load_action = QAction("Load", self)
        save_action = QAction("Save", self)
        exit_action = QAction("Exit", self)
        
        file_menu.addAction(load_action)
        file_menu.addAction(save_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)
        
        # load_action.triggered.connect()
        # save_action.triggered.connect()
        # exit_action.triggered.connect()

        settings_menu = menu.addMenu("Settings")        
        user_settings_action = QAction("User Settings", self)

        settings_menu.addAction(user_settings_action)

        # user_settings_action.triggered.connect()

    def create_toolbar(self):
        toolbar = QToolBar("My main toolbar")
        
        save_action = QAction("Your button", self)
        icon = self.style().standardIcon(QStyle.SP_DialogSaveButton)
        save_action.setIcon(icon)
        save_action.setCheckable(True)
        
        open_action = QAction("Your button", self)
        pixmapi = getattr(QStyle, 'SP_DirOpenIcon')
        icon = self.style().standardIcon(pixmapi)
        open_action.setIcon(icon)
        
        save_action.setStatusTip("This is your button")
        open_action.setStatusTip("This is your button")
        
        # save_action.triggered.connect()
        # open_action.triggered.connect()

        toolbar.addAction(open_action)
        toolbar.addAction(save_action)
        
        self.addToolBar(toolbar)
    
    def create_elements(self):
        pass
    
    def create_layout(self):
        pass
    
    def create_connections(self):
        pass
    
    def create_status_bar(self):
        self.status_label1 = QLabel("")
        self.status_label2 = QLabel("")
        self.statusBar().addPermanentWidget(self.status_label1)
        self.statusBar().addPermanentWidget(self.status_label2)
        self.statusBar().showMessage('Ready...')
    
 
# =============================================================================
# Show all standard Icons
# =============================================================================
import sys

from PySide6.QtWidgets import QApplication, QGridLayout, QPushButton, QStyle, QWidget


class Window(QWidget):
    def __init__(self):
        super().__init__()

        icons = sorted(
            [attr for attr in dir(QStyle.StandardPixmap) if attr.startswith("SP_")]
        )
        layout = QGridLayout()

        for n, name in enumerate(icons):
            btn = QPushButton(name)

            pixmapi = getattr(QStyle, name)
            icon = self.style().standardIcon(pixmapi)
            btn.setIcon(icon)
            layout.addWidget(btn, n // 4, n % 4)

        self.setLayout(layout)


app = QApplication(sys.argv)

w = Window()
w.show()

app.exec()


# ---------------------------
# ENTRY POINT
# ---------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    
    icon_path = Path(r"")
    app.setWindowIcon(QIcon(str(icon_path)))
    window = MainWindow()
    window.setWindowIcon(QIcon(str(icon_path)))
    window.show()
    
    sys.exit(app.exec())   


# ---------------------------
# ENTRY POINT (Spyder-safe)
# ---------------------------
if __name__ == "__main__":
    
    # Create QApplication only once
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
        
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    
    app.exec()