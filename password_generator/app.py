import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QCloseEvent

from ui.ui_main import Ui_MainWindow
from password_generator import PasswordGenerator

GENERATE_PASSWORD = (
    'btn_refresh',
    'btn_lower',
    'btn_upper',
    'btn_digits',
    'btn_punct',
)


class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.set_password()
        self.connect_slider_to_spinbox()
        self.ui.btn_copy.clicked.connect(self.copy_to_clipboard)

        for btn in GENERATE_PASSWORD:
            getattr(self.ui, btn).clicked.connect(self.set_password)

    def closeEvent(self, event: QCloseEvent) -> None:
        QApplication.clipboard().clear()

    def connect_slider_to_spinbox(self) -> None:
        self.ui.slider_length.valueChanged.connect(self.ui.spinbox_length.setValue)
        self.ui.spinbox_length.valueChanged.connect(self.ui.slider_length.setValue)
        self.ui.spinbox_length.valueChanged.connect(self.set_password)

    def _password(self) -> PasswordGenerator:
        length = self.ui.slider_length.value()
        password = PasswordGenerator(
            length=length,
            add_lower=self.ui.btn_lower.isChecked(),
            add_upper=self.ui.btn_upper.isChecked(),
            add_digits=self.ui.btn_digits.isChecked(),
            add_punct=self.ui.btn_punct.isChecked(),
        )
        return password

    def set_password(self):
        self.ui.line_password.setText(self._password().password)
        self.set_entropy()
        self.set_strength()

    def set_entropy(self):
        self.ui.label_entropy.setText(
            f'Entropy: {self._password().entropy} bit'
        )

    def set_strength(self):
        self.ui.label_strength.setText(
            f'Strength: {self._password().strength}'
        )

    def copy_to_clipboard(self) -> None:
        QApplication.clipboard().setText(self.ui.line_password.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = App()
    window.show()

    sys.exit(app.exec())
