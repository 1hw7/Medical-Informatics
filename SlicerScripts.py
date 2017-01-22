#creates a button in slicer and prints button clicked in python interactor
def callback():
     print('button clicked')
     
def nodeTransform():
# Create transform node & translate
    node = slicer.vtkMRMLLinearTransformNode()
    node.SetName('PreModelToRas')
    slicer.mrmlScene.AddNode(preModelToRas)
    nodeToTranslate = vtk.vtkTransform()
    nodeToTranslate.PreMultiply() 
    nodeToTranslate.Translate(0, 100, 0)
    nodeToTranslate.Update()
    node.SetAndObserveTransformToParent(nodeToTranslate)

def main():
    button = qt.QPushButton('Click')
    button.connect('clicked()', callback)
    button.show
    nodeTransform()


