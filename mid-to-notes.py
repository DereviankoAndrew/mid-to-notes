import mido
import midiTable
from tkinter import *
import tkinter
from tkinter.filedialog import askopenfilename
import time

root = tkinter.Tk()
root.withdraw()
filename = askopenfilename()
mid = mido.MidiFile(filename, clip=True)

# Creating lists with notes and velocities
notes = []
velocities = []

counter = 0
while counter < len(mid.tracks[0]):
    if mid.tracks[0][counter].type == 'note_on':
        notes.append(mid.tracks[0][counter].note)
        velocities.append(mid.tracks[0][counter].velocity)
    counter += 1

# Add the note and velocity to the list
notes_to_velocities = list(zip(notes, velocities))

# Getting rid of note if its velocity is lower than 25
counter = 0
while counter < len(notes_to_velocities):
    if notes_to_velocities[counter][1] <= 38:
        notes_to_velocities.pop(counter)
        counter = 0
    else:
        counter += 1

#  Making a list of notes only
only_notes = []
counter = 0

while counter < len(notes_to_velocities):
    only_notes.append(notes_to_velocities[counter][0])
    counter += 1

# Find out a note relatively to its number (from midiTable.py)
counter = 0
counter2 = 0
engl_notes = []

while counter < len(only_notes):
    while counter2 < len(midiTable.note_data):
        if only_notes[counter] == midiTable.note_data[counter2][0]:
            engl_notes.append(midiTable.note_data[counter2][1])
            counter2 = 0
            break
        counter2 += 1
    counter += 1

# Getting rid of doubling in ENGL_NOTES
counter = 0
try:
    while counter < len(engl_notes):
        if engl_notes[counter] == engl_notes[counter + 1]:
            engl_notes.pop(counter + 1)
            counter = 0
        else:
            counter += 1
except IndexError:
    print('\n')

# Making a string out of list in order to add this to tkinter
result = ''
counter = 0
while counter < len(engl_notes):
    if counter+1 == len(engl_notes):
        result = result + str(engl_notes[counter]) + '. '
        break
    result = result + str(engl_notes[counter]) + ', '
    counter += 1
print('\n')
print(result)

# Tkinter
window = tkinter.Tk()
window.resizable(width='False', height='False')
window.geometry('800x400+550+300')
window.title('mid-to-note')

Label1 = tkinter.Label(window, text=result, font="Arial 25")
Label1.config(height=1, width=42)
Label1.place(x=0, y=140)

window.mainloop()
time.sleep(100000000)


