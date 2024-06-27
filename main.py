import sys
from PyQt5.QtWidgets import QApplication
from gui import VideoToAudioConverter

if __name__ == '__main__':
    app = QApplication(sys.argv)
    converter = VideoToAudioConverter()
    converter.show()
    sys.exit(app.exec())
