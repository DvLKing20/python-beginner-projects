import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QHBoxLayout,QWidget,QLabel,QPushButton,QVBoxLayout
from PyQt5.QtCore import QTimer

class StopWatch(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ms = 0
        self.s = 0
        self.m = 0
        self.setGeometry(700,300,500,500)
        self.setWindowTitle("Stop Watch")
        self.button_start = QPushButton("Start")
        self.button_stop = QPushButton("Stop")
        self.button_reset = QPushButton("Reset")
        self.watch_label = QLabel("00:00:00",self)
        self.show_clock()
    
    def show_clock(self):
        my_widgets = QWidget()
        self.setCentralWidget(my_widgets)

        hbox = QHBoxLayout()

        hbox.addWidget(self.button_start)
        hbox.addWidget(self.button_stop)
        hbox.addWidget(self.button_reset)

        my_widgets.setLayout(hbox)
        
        self.watch_label.setGeometry(140,100,220,70)
        self.setStyleSheet("""
QLabel {
    background-color: #1E1F22;
    color: #00FF9C;
    font-size: 40px;
    font-family: 'Comic Sans MS';
    padding: 12px;
    border-radius: 12px;
    border: 2px solid #2C2F33;
}                           
QPushButton {
    background-color: #2A2E35;
    color: #F2F2F2;
    padding: 10px 18px;
    border-radius: 10px;
    font-size: 20px;
    font-family: 'Segoe UI';
    border: 2px solid #3A3F47;
}

QPushButton:hover {
    background-color: #353A42;
    border: 2px solid #4A5059;
}

QPushButton:pressed {
    background-color: #1F2328;
    border: 2px solid #5A5F68;
    padding-top: 12px;   /* subtle press effect */
    padding-bottom: 8px;
}
""")

        
        self.button_start.clicked.connect(self.start_stop_reset)
        self.button_stop.clicked.connect(self.start_stop_reset)
        self.button_reset.clicked.connect(self.start_stop_reset)
    
    def start_stop_reset(self):
        btn = self.sender()
        value = btn.text()
        if value == "Start":
            self.timer = QTimer()
            self.timer.timeout.connect(self.start_watch)
            self.timer.start(10)
        elif value == "Stop":
            self.timer.stop()

        elif value =="Reset":
            self.ms = 0
            self.s = 0
            self.m = 0
            self.watch_label.setText(f"{self.m:02d}:{self.s:02d}:{self.ms:02d}")

        else:
            pass

    def start_watch(self):
        self.ms+=1
        if self.ms == 60:
            self.s += 1
            self.ms = 0
        elif self.s == 60:
            self.m+=1
            self.s = 0
        self.watch_label.setText(f"{self.m:02d}:{self.s:02d}:{self.ms:02d}")
         
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StopWatch()
    window.show()
    sys.exit(app.exec_())