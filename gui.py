from PyQt5.QtWidgets import (
    QWidget, QPushButton, QFileDialog, QLabel, QVBoxLayout, 
    QLineEdit, QComboBox, QMessageBox, QHBoxLayout, QMenu
)
from PyQt5.QtCore import Qt
from conversion import convert_video_to_audio, set_id3_tags
from helpers import QUALITY_OPTIONS, CODEC_OPTIONS, EFFECT_OPTIONS, EFFECT_HELP_TEXTS

class VideoToAudioConverter(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('Video zu Audio Konverter')
        self.setGeometry(100, 100, 400, 650)
        self.setStyleSheet(self.load_stylesheet("style.qss"))

        self.file_path: str | None = None

        layout = QVBoxLayout()

        self.select_button = QPushButton('Video auswählen', self)
        self.select_button.clicked.connect(self.select_video)
        layout.addWidget(self.select_button)

        self.quality_label = QLabel('Audioqualität:')
        layout.addWidget(self.quality_label)

        self.quality_combo = QComboBox()
        self.quality_combo.addItems(QUALITY_OPTIONS.keys())
        layout.addWidget(self.quality_combo)

        self.codec_label = QLabel('Audiocodierung:')
        layout.addWidget(self.codec_label)

        self.codec_combo = QComboBox()
        self.codec_combo.addItems(CODEC_OPTIONS.keys())
        layout.addWidget(self.codec_combo)

        self.effect_label = QLabel('Klang-Effekt:')
        layout.addWidget(self.effect_label)

        self.effect_combo = QComboBox()
        self.effect_combo.addItems(EFFECT_OPTIONS.keys())
        self.effect_combo.currentTextChanged.connect(self.toggle_effect_value_input)
        layout.addWidget(self.effect_combo)

        effect_value_layout = QHBoxLayout()
        
        self.effect_value_label = QLabel('Effektwert:')
        effect_value_layout.addWidget(self.effect_value_label)
        
        self.effect_value_input = QLineEdit()
        effect_value_layout.addWidget(self.effect_value_input)
        
        self.effect_info_label = QLabel('INFO')
        self.effect_info_label.setStyleSheet("color: blue; text-decoration: underline; cursor: pointer;")
        self.effect_info_label.mousePressEvent = self.show_effect_info
        effect_value_layout.addWidget(self.effect_info_label)
        
        layout.addLayout(effect_value_layout)

        self.file_name_label = QLabel('Dateiname:')
        layout.addWidget(self.file_name_label)

        self.file_name_input = QLineEdit()
        layout.addWidget(self.file_name_input)

        self.album_label = QLabel('Album:')
        layout.addWidget(self.album_label)

        self.album_line_edit = QLineEdit()
        layout.addWidget(self.album_line_edit)

        self.title_label = QLabel('Titel:')
        layout.addWidget(self.title_label)

        self.title_line_edit = QLineEdit()
        layout.addWidget(self.title_line_edit)

        self.artist_label = QLabel('Künstler:')
        layout.addWidget(self.artist_label)

        self.artist_line_edit = QLineEdit()
        layout.addWidget(self.artist_line_edit)

        self.track_label = QLabel('Track Nummer:')
        layout.addWidget(self.track_label)

        self.track_line_edit = QLineEdit()
        layout.addWidget(self.track_line_edit)

        self.year_label = QLabel('Jahr:')
        layout.addWidget(self.year_label)

        self.year_line_edit = QLineEdit()
        layout.addWidget(self.year_line_edit)

        self.convert_button = QPushButton('In Audio konvertieren', self)
        self.convert_button.clicked.connect(self.convert_video_to_audio)
        layout.addWidget(self.convert_button)

        self.setLayout(layout)
        self.toggle_effect_value_input(self.effect_combo.currentText())

    def load_stylesheet(self, file_name: str) -> str:
        with open(file_name, "r") as file:
            return file.read()

    def toggle_effect_value_input(self, effect: str) -> None:
        """Toggle the visibility of the effect value input based on selected effect."""
        if effect == 'Kein Effekt':
            self.effect_value_label.setVisible(False)
            self.effect_value_input.setVisible(False)
            self.effect_info_label.setVisible(False)
        else:
            self.effect_value_label.setVisible(True)
            self.effect_value_input.setVisible(True)
            self.effect_info_label.setVisible(True)

    def show_effect_info(self, event) -> None:
        """Show a context menu with information about the selected effect."""
        effect = self.effect_combo.currentText()
        if effect in EFFECT_HELP_TEXTS:
            help_text = EFFECT_HELP_TEXTS[effect]
            menu = QMenu(self)
            menu.addAction(help_text)
            menu.exec_(self.effect_info_label.mapToGlobal(event.pos()))

    def select_video(self) -> None:
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, 'Video auswählen', '', 'Video Dateien (*.mp4 *.avi)', options=options)
        if file_name:
            self.file_path = file_name
            self.select_button.setText(f'Ausgewählt: {file_name}')

    def convert_video_to_audio(self) -> None:
        if self.file_path:
            quality = QUALITY_OPTIONS[self.quality_combo.currentText()]
            codec = CODEC_OPTIONS[self.codec_combo.currentText()]
            effect_template = EFFECT_OPTIONS[self.effect_combo.currentText()]
            effect_value = self.effect_value_input.text() or '0'
            effect = effect_template.format(value=effect_value)
            album = self.album_line_edit.text()
            title = self.title_line_edit.text()
            artist = self.artist_line_edit.text()
            track = self.track_line_edit.text()
            year = self.year_line_edit.text()
            file_name = self.file_name_input.text()

            if not file_name:
                QMessageBox.warning(self, 'Fehler', 'Bitte geben Sie einen Dateinamen ein.')
                return

            output_file = f'{file_name}.mp3'
            
            QMessageBox.information(self, 'Konvertierung', 'Erstellung gestartet, bitte warten...')
            
            success, error_message = convert_video_to_audio(
                self.file_path, output_file, quality, codec, effect)
            
            if success:
                set_id3_tags(output_file, title, artist, album, track, year)
                QMessageBox.information(self, 'Konvertierung', f'Konvertierung fertig. Ihre Datei finden Sie hier: {output_file}')
                self.select_button.setText('Video auswählen')
            else:
                QMessageBox.warning(self, 'Konvertierung', f'Die Konvertierung ist fehlgeschlagen: {error_message}')
