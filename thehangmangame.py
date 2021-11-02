#Declaring variables
secretWord = ' ' # word we hide and try to guess
hiddenWord = ' ' # same as secretWord but will be shown as '_ _ _ _ _'
lifeTotal = 7 # this will be used to print parts of the gallow
gallow = [
' |\n O\n/|\\\n/ \\\n',
' |\n O\n/|\\\n/ \n',
' |\n O\n/|\\\n \n',
' |\n O\n/ \ \n \n',
' |\n O\n/  \n  \n',
' |\n O\n   \n  \n',
' |\n  \n   \n  \n'
]
# this prints a gallow i swear
inputLetter = ' '#the letter that we input
winningStatus = False #checks if the game is won

while (secretWord.isspace()):
    secretWord = input('Enter your word to play The Hangman Game, by charles8ff: \n\n\t>> ')
    if secretWord.isalpha() and (secretWord.find(' ')==-1):#
        secretWord = secretWord.upper()
        for letter in secretWord: #loop adds a '_' for every letter secretWord has 
            hiddenWord = hiddenWord + '_'
    else:
        secretWord = ' '
        print('That was not a valid word, m\'lad.')

#asks for new word until you fill without numbers and without spaces
print('Let\'s play, the hidden word has ' + str(len(secretWord)) + ' letters: \n\n')
print('\n\t', end='')
print(*hiddenWord, end='')
print('\t')
print('\n\nAnd you have '+ str(lifeTotal) + ' hitpoints left to play. GLHF!' )

#the game begins
while( winningStatus == False and lifeTotal > 0):
    #input of a letter
    while (inputLetter.isspace()):
        inputLetter  = input('Type a letter to try to guess: \n >> ')
        if not inputLetter.isalpha() or len(inputLetter)!=1:
            inputLetter = ' '
            print('That was not a valid word, fella.')
        else:
            inputLetter = inputLetter.upper()
    #find'em, every one of them
    if secretWord.find(inputLetter) != -1:
        aux = 1
        for c in secretWord:
            if c == inputLetter:
                hiddenWord = hiddenWord[:aux] + inputLetter + hiddenWord[aux+1:]#strings behave as lists and this is a very complicated way
            aux=aux+1
            
        #prints hidden word
        print('\n\t', end='')
        print(*hiddenWord, end='')
        print('\n\n')
        #checks if game is over
        if hiddenWord.find('_')!=-1:#if no underscore, means we solved and won the game
            winningStatus = False
        else:
            winningStatus = True
    else:#failed to find
        lifeTotal = lifeTotal-1
        print('\nDing Dong your letter is wrong.\n')
        print('Hitpoints left: '+str(lifeTotal)+'\n')
        print(gallow[lifeTotal])#this prints the hanged man with a very ugly array we declared above
        print('\n')
    inputLetter = ' '#reset input so it asks again
if winningStatus:
    print('\n\n\n-------------------YOU WIN-------------------\n\n\nYou got '+ str(lifeTotal)+ ' spare lives. GGWP!!\n')#winning msg
else:
    print('\n\n\n-------------------GAME OVER-------------------\n\n\nAny last words?\n')#loser msg
