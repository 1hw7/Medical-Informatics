#creates a button in slicer and prints button clicked in python interactor
def callback():
     print('button clicked')
def main():
    button = qt.QPushButton('Click')
    button.connect('clicked()', callback)
    button.show
