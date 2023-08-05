# 1. pip install easygui
# 2. pip install rembg

from rembg import remove
import easygui
from PIL import Image

inputPath = easygui.fileopenbox(title='Select image file')
outputPath = easygui.filesavebox(title='Select file to..')

input = Image.open(inputPath)
output = remove(input)
output.save(outputPath)

# 3. After that select the image u want to remove bg
# 4. And, then write of o/p image name as png.