import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
from PyQt5.QtCore import QTime,QTimer

class digital_clock(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,600,500)
        self.setWindowTitle("Digital Clock")
        self.current_time = QTime.currentTime()
        self.formatted_time = self.current_time.toString("hh:mm:ss")
        self.show_time_label = QLabel(self.formatted_time,self)
        self.show_time_label.setGeometry(100,90,500,120)
        self.Digital_clock()

    def Digital_clock(self):
        self.setStyleSheet("""
    QLabel {
        font-size: 72px;
        font-family: 'Consolas';
        color: #00FFCC;
        background-color: #111111;
        border: 2px solid #00CCAA;
        border-radius: 12px;
        padding: 20px;
    }
""") 
        self.clock_tick = QTimer()
        self.clock_tick.timeout.connect(self.update_clock)
        self.clock_tick.start(1000)
    
    def update_clock(self):
        time = QTime.currentTime()
        format = time.toString("hh:mm:ss")
        self.show_time_label.setText(format)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = digital_clock()
    window.show()
    sys.exit(app.exec_())