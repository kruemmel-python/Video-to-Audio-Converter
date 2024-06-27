# Video to Audio Converter

Ein einfacher Video-zu-Audio-Konverter, der verschiedene Audioqualitäten, Codecs und Effekte unterstützt. Entwickelt mit PyQt5 für die GUI und Mutagen für das Setzen von ID3-Tags.

## Installation

1. **Repository klonen**:

    ```bash
    git clone https://github.com/dein-github-username/video-to-audio-converter.git
    cd video-to-audio-converter
    ```

2. **Virtuelle Umgebung erstellen** (optional aber empfohlen):

    ```bash
    python -m venv venv
    source venv/bin/activate  # Für Windows: venv\Scripts\activate
    ```

3. **Abhängigkeiten installieren**:

    ```bash
    pip install -r requirements.txt
    ```

## Verwendung

1. **Programm starten**:

    ```bash
    python main.py
    ```

2. **GUI-Anweisungen befolgen**:
    - Wählen Sie ein Video aus.
    - Geben Sie die gewünschten Audioqualitäts-, Codec- und Effektparameter ein.
    - Geben Sie den Dateinamen der Ausgabedatei ein.
    - Klicken Sie auf „In Audio konvertieren“, um die Konvertierung zu starten.

## Funktionen

- **Audioqualität**: Wählen Sie zwischen verschiedenen Bitraten (niedrig, mittel, hoch).
- **Codecs**: Unterstützt mehrere Audio-Codecs, einschließlich MP3, AAC, Opus, Vorbis, FLAC, ALAC, WavPack und Speex.
- **Effekte**: Anwenden verschiedener Audioeffekte wie Bass-Boost, Treble-Boost, Echo, Reverb, Lautstärkeerhöhung und Geschwindigkeitsänderung.
- **ID3-Tags**: Setzen Sie ID3-Tags für Titel, Künstler, Album, Track-Nummer und Jahr.

## Dokumentation

- [PyQt5 Dokumentation](https://www.riverbankcomputing.com/static/Docs/PyQt5/)
- [Mutagen Dokumentation](https://mutagen.readthedocs.io/en/latest/)

## Beitragen

Beiträge sind willkommen! Bitte erstellen Sie einen Fork des Repositories und senden Sie einen Pull-Request mit Ihren Änderungen.

## Lizenz

Dieses Projekt ist lizenziert unter der MIT-Lizenz. Weitere Informationen finden Sie in der [LICENSE](LICENSE) Datei.


