
def callback():
     print('button clicked')
def main():
    b = qt.QPushButton('Toggle')
    b.connect('clicked()', callback)
    b.show
