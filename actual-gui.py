from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
from PySide6.QtCore import QTimer, Slot
from PySide6.QtCore import Qt
from gui import Ui_Widget

import qdarktheme
import sys, time, os, math

class AI_Covers_Window(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.pushButton_1.clicked.connect(self.grab_content)
        self.pushButton_2.clicked.connect(self.grab_style)
        self.pushButton_3.clicked.connect(self.neural_art)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_bar)
        self.timer.start(100)

        os.system("echo 0 > /tmp/state")

        self.show()

    def grab_content(self):
        file_name = QFileDialog.getOpenFileName(self, "Select Content Image", "/home/alphara/neural-art/Images", "PNG or JPG (*.png *.jpg *.jpeg)")
        if len(file_name[0]) > 0: self.label_1.setText(file_name[0])

    def grab_style(self):
        file_name = QFileDialog.getOpenFileName(self, "Select Style Image", "/home/alphara/neural-art/Images", "PNG or JPG (*.png *.jpg *.jpeg)")
        if len(file_name[0]) > 0: self.label_2.setText(file_name[0])

    def neural_art(self):
        if self.label_1.text() != "path/to/content" and self.label_2.text() != "path/to/style":
            self.label_3.setText("")
            os.system("echo 0 > /tmp/state")
            self.pushButton_3.setEnabled(False)
            os.system(f"cd neural-art ; ./stylize.sh {self.label_2.text()} {self.label_1.text()} &")

    @Slot()
    def update_bar(self):
        with open('/tmp/state') as state_file:
            bar_state = math.ceil(int(state_file.read()) / 600 * 100)

        self.progressBar.setValue(bar_state)

        if bar_state > 96 and bar_state < 100:
            self.label_3.setText("Done!")
            self.pushButton_3.setEnabled(True)
            os.system("echo 600 > /tmp/state")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.neural_art()


if __name__ == '__main__':
    app = QApplication([])
    window = AI_Covers_Window()
    qdarktheme.setup_theme()
    app.exec()
    os.system("pkill python")
