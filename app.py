from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
import sys
from download_youtube import YoutubeDownloader


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_icon = QIcon('./icon.ico')
    app.setWindowIcon(app_icon)
    downloader_app = YoutubeDownloader()
    downloader_app.show()
    sys.exit(app.exec_())
