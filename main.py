import sys
from PyQt5.QtWidgets import QApplication

from controller.con_obtain_journal import JournalController

if __name__ == '__main__':
    app = QApplication(sys.argv)
    journal_con = JournalController()
    journal_con.show_ui()
    sys.exit(app.exec_())