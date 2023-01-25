from music21 import *
from wand.image import Image
from wand.color import Color
import io

print("Welcome to NoteRec by Aryaman!")
print("Enter the path of your PDF and we will convert and output the notes for you.")
file = input()
# Open the PDF using Wand
with Image(filename=file) as img:
    img.background_color = Color('white')
    img.alpha_channel = 'remove'
    img.save(filename=f'{file}.png')

# Load the PNG image into Music21
score = graph.plot.Plot().process_file(f'{file}.png')

# Extract the notes from the score
for n in score.flat.notes:
    print(n.nameWithOctave)