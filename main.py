import sys
from PyQt5.QtWidgets import QApplication

from login.views.VistaLogin import VistaLogin


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = VistaLogin()
    main.show()
    sys.exit(app.exec())

