import sys
from PyQt5.QtWidgets import QApplication

from controller.con_main import MainController

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_controller = MainController()
    main_controller.show_ui()
    sys.exit(app.exec_())