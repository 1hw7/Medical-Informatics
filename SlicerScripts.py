import qt
def toggle():
     print('button clicked')
def main():
    b = qt.QPushButton('Toggle')
    b.connect('clicked()', toggle)
    b.show