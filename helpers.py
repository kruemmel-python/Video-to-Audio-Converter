QUALITY_OPTIONS = {
    'Niedrig': '64k',
    'Mittel': '128k',
    'Hoch': '320k'
}

CODEC_OPTIONS = {
    'MP3 (LAME)': 'libmp3lame',
    'AAC': 'aac',
    'Opus': 'libopus',
    'Vorbis': 'libvorbis',
    'FLAC': 'flac',
    'ALAC': 'alac',
    'WavPack': 'wavpack',
    'Speex': 'libspeex'
}

EFFECT_OPTIONS = {
    'Kein Effekt': '',
    'Bass-Boost': 'bass=g={value}',
    'Treble-Boost': 'treble=g={value}',
    'Echo': 'aecho=0.8:0.9:{value}:0.3',
    'Reverb': 'aecho=0.8:0.9:1000|1800:{value}|0.25',
    'Lautstärke erhöhen': 'volume={value}dB',
    'Geschwindigkeit erhöhen': 'atempo={value}',
    'Custom Equalizer': 'equalizer=f=60:width_type=o:width=2:g={value}, equalizer=f=170:width_type=o:width=2:g={value}, equalizer=f=310:width_type=o:width=2:g={value}, equalizer=f=600:width_type=o:width=2:g={value}'
}

EFFECT_HELP_TEXTS = {
    'Bass-Boost': 'Geben Sie den Verstärkungswert für die Bassfrequenzen an. Beispiel: 20',
    'Treble-Boost': 'Geben Sie den Verstärkungswert für die Höhenfrequenzen an. Beispiel: 5',
    'Echo': 'Geben Sie die Verzögerungszeit für das Echo an. Beispiel: 1000',
    'Reverb': 'Geben Sie den Wert für den Nachhall an. Beispiel: 0.3',
    'Lautstärke erhöhen': 'Geben Sie den Wert für die Lautstärkeerhöhung in dB an. Beispiel: 5',
    'Geschwindigkeit erhöhen': 'Geben Sie den Wert für die Geschwindigkeitsänderung an. Beispiel: 1.5',
    'Custom Equalizer': 'Geben Sie die Verstärkungswerte für verschiedene Frequenzen an. Beispiel: 5'
}
