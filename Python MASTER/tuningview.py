sharpnotes = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
flatnotes = ['A','Bb','B','C','Db','D','Eb','E','F','Gb','G','Ab']

#lower strings at end of list
standard = [7,2,10,5,0,7]
drop =  [7,2,10,5,0,5]

notes = sharpnotes
strings = standard
while(True):
    if __name__ == "__main__":
        adjust = input("Half steps from standard?\n")
        if (adjust == 'q'):
            exit()
        elif (adjust == 'b'):
            notes = flatnotes
            print("Now showing flats.")
            continue
        elif (adjust == 's'):
            notes = sharpnotes
            print("Now showing sharps.")
            continue
        elif (adjust == 'drop'):
            strings = drop
            print("Now showing drop tuning.")
            continue
        elif (adjust == 'standard'):
            strings = standard
            print("Now showing standard tuning.")
            continue

        adjust = int(adjust)
        adjustedstrings = []
        for m in strings:
            adjustedstrings.append(m+adjust)

        for num in range (13):
            print(num, end='|\t')
        print()

        for i in adjustedstrings:
            for j in range(0,13):
                trimmed = (i+j)%12
                if (trimmed < len(notes)):
                    print(notes[trimmed], end='|\t')
                else:
                    print(notes[trimmed - len(notes)], end='|\t')
            print()