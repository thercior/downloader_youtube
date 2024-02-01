from PyQt5.QtWidgets import *
from pytube import YouTube
import sys
import os

class YoutubeDownloader(QWidget):
    def __init__(self):
        super().__init__()
        
        self.init_ui()
    
    def init_ui(self):
        #Layout principal
        layout = QVBoxLayout()
        
        # Entrada da URL
        self.url_link = QLineEdit(self)
        self.url_link.setPlaceholderText('Cole aqui a url do vídeo que deseja baixar')
        layout.addWidget(self.url_link)
        
        # Escolher local de salvamento
        self.save_folder = QLineEdit(self)
        self.save_folder.setPlaceholderText('Escolha a pasta para salvar o arquivo')
        self.browse_button = QPushButton('Procurar', self)
        self.browse_button.clicked.connect(self.browse_folder)
        layout.addWidget(self.save_folder)
        layout.addWidget(self.browse_button)
        
        # Chama a funciton para baixar o vídeo
        self.download_button = QPushButton('Baixar', self)
        self.download_button.clicked.connect(self.download_video)
        layout.addWidget(self.download_button)
        
        # Área para visualizar o que foi baixado
        self.download_status = QLabel('Downloads:')
        self.download_list = QTextBrowser(self)
        layout.addWidget(self.download_status)
        layout.addWidget(self.download_list)
        
        self.setLayout(layout)
        
        # Para editar visualização da interface GUI
        self.setWindowTitle('Downloader de vídeos do youtube')
        self.center_screen()
        # self.setGeometry(1000, 550, 640, 480)
    
    # Funcáo que serve para calcular o centro da tela e exibir a GUI no centro
    def center_screen(self):
        # Obtém a geometria da tela prinicipal
        geometry = QDesktopWidget().screenGeometry()
        
        w, h = 640, 480
        
        x = int((geometry.width() - w) / 2)
        y = int((geometry.height() - h) / 2)
        
        self.setGeometry(x, y, w, h)
    
    def browse_folder(self):
        folder = QFileDialog.getExistingDirectory(self, 'Selecione a pasta que deseja salvar o arquivo')
        self.save_folder.setText(folder)
        
    def download_video(self):
        url = self.url_link.text()
        save_path = self.save_folder.text()
        
        if url and save_path:
            try:
                youtube = YouTube(url)
                video = youtube.streams.filter(progressive=True, file_extension='mp4')[1] # Assim vem vídeo qualidade melhor
                video.download(save_path)
                
                # Adiciona o status de download à área de visualização
                download_info = f'{youtube.title} foi baixado em {save_path}'
                self.download_list.append(download_info)
                
            except Exception as e:
                self.download_list.append(f'Erro ao baixo o vídeo: {str(e)}')
        else:
            self.download_list.append('Forneça uma url válida e um local para salvar o arquivo')
        