import sys
import pyttsx3
import random
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtCore import Qt

words = {
    'moody': 'angry or depressed without any warning',
    'agressive': 'angry and violent',
    'respected': 'admired and considered important',
    'mean': 'unkind to another person',
    'jelaous': 'angry or bitter because somebody has something you want',
    'carving': 'affectionate, helpful and sympathetic',
    'dishonest': 'not truthful, cannot be trusted',
    'well-meaning': 'unsuccessful when trying to be helpful or kind',
    'supportive': 'kind and helpful during difficult or unhappy times',
    'creative': 'able to invent and develop original ideas',
    'selfish': 'caring only about themselves',
    'loyal': 'firm in their support for a person',
    'patient': 'calm, not easily annoyed',
    'dedicated': 'devoted and enthusiastic',
    'trusting': 'honest and sincere'
}

def sound(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for v in voices:
        if "english" in v.name.lower():
            engine.setProperty('voice', v.id)
            break
    engine.say(text)
    engine.runAndWait()

class SoundPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sound")
        self.setGeometry(200, 200, 400, 200)

        self.label = QLabel("Привет, PyQt6!", alignment=Qt.AlignmentFlag.AlignCenter)
        self.button = QPushButton("Нажми меня")
        self.button.clicked.connect(self.on_button_click)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def on_button_click(self):
        word, meaning = random.choice(list(words.items()))
        self.label.setText(f"{meaning}")
        sound(meaning)
        print(word)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SoundPage()
    window.show()
    sys.exit(app.exec())
