#Collatz Tag Sequence

#a -> bc
#b -> a
#c -> aaa

#inputting any amount of a's ending with 1 letter (a)
LetterChanges = { 'a':'bc' , 'b':'a' , 'c':'aaa'}
Acheck = False

while Acheck == False:
    print('Enter any 1 letter to quit')
    InputtedString = raw_input('Enter a string of a\'s\n')

    Acheck = True

    #Error checking input. really not necessary since I'll be the only one using
    # this program :'(

    for i in range(1,len(InputtedString)):

        if InputtedString[i] != 'a':

            Acheck = False
            print('The input must be only a\'s\n')
            break


def CollatzSequence(InputtedString):
    while len(InputtedString) > 1:
        InputtedString = InputtedString[2:] + LetterChanges[InputtedString[0]]
        print(InputtedString)

if __name__ == "__main__":
    CollatzSequence(InputtedString)
    print('The End\n')
