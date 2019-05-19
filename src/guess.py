"""
This module is the main module for the guessing game.It imports DatabaseOperations and GamePlay
classes from their respective modules.
@see: DatabaseOperations
@see: GamePlay
Created on May 14, 2019

@author: apoorvasharma
"""
import random
from stringDatabase import DatabaseOperations
from game import GamePlay

class GameController:
    '''
        This class is the controller class for the guessing game
        @param self:
    '''
    def __init__(self) :
        self.gameNumber =0
        self.guessWord ='----'
        self.badGuess=0
        self.flipped = 0
        self.word =""
        self.finalSummary =[]
        self.guessType=""
        self.missedLetter =0
    def gameStart(self):
        '''
            This method is responsible for initiating the game.
            @param self:
        '''
        self.guessWord="----"
        self.missedLetter =0
        self.badGuess=0
        self.flipped =0
        if self.gameNumber ==0:
            print("Welcome to the guessing game")
            print("Game Level 1")
        else:
            print("Game Level "+str(self.gameNumber+1))
        print("Choose one of the following option to continue:")
        print("g : to guess the word")
        print("t : tell me")
        print("l : to guess a letter")
        print("q : to quit the game")
        op = DatabaseOperations()
        wordList  = op.loadFile()
        print()
        while self.gameNumber <100:
            self.gameNumber =int(self.gameNumber)+1
            indextoChoose =random.randint(0,wordList.__len__())
            self.word = wordList[indextoChoose]
            ch =input("Enter your choice ")
            self.playGuess(ch.lower())
                
                
    def gameSummary(self):
        '''
            This method is responsible for providing the game summary once the users decides to
            quit.
        '''
        print()
        finalScore=0
        tab ="\t" 
        print("Game\t Word\t Status\t  Bad Guesses\t Missed Letters\t Score")
        print("----\t----\t ------\t -----------\t--------------\t-----")
        for temp in range(len(self.finalSummary)):
            y = self.finalSummary[temp]
            finalScore = y["Score"]+finalScore
            print(str(y["Game Number"])+tab+y["Word"]+tab+y["Status"]+tab+tab+str(y["Bad Guess"])+tab+tab+str(y["Missed Letter"])+tab+"{:.{}f}".format(y["Score"],2))
        print("Final Score of Player "+"{:.{}f}".format(finalScore,2))
        exit(0)
    
    # Responsible for playing the game   
    def playGuess(self,choice):
        '''
            This method is responsible for taking appropriate actions based on user choices.
            @param choice:User choice
        '''
        while choice!='q':
            if choice=='t':
                self.tellME()
            elif choice=='l':
                self.seekletter()
            elif choice=='g':
                self. seekWord()
            choice = input("Enter the next operation : t=tell me,q =quit,l= for letter, g = guess ").lower()
        if choice=='q':
            confirm =input("Are you sure you want to exit the game?(y/n) ")
            if confirm=='y' or confirm=='Y':
                if self.flipped>0:
                    self.caculateGameScore('t') # will deduct point in similar fashion of tell me for an ongoing game.
                self.gameSummary()
            else:
                choice = input("Enter the next operation : t=tell me,q =quit,l= for letter, g = guess ").lower()
                self.playGuess(choice)
                
            
    # Responsible for guessing the game       
    def seekWord(self):
        '''
            This method is responsible for guessing word.
        '''
        print("Word to guess: "+self.guessWord)
        x = input("Enter the word : ").lower()
        if x.__eq__(self.word) :
            print("You've guessed the correct word.")
            self.guessType='c'
            self.caculateGameScore('g')
            self.gameStart()
        else:
            print("Wrong guess. Better luck next time!!")
            self.badGuess=self.badGuess+1
            self.caculateGameScore('g')
            self.guessType='n'
            
    
    def seekletter(self):
        '''
            This method is responsible for guessing letters.
            @param choice:User choice
        '''
        print("Word to guess: "+self.guessWord)
        x = input("Enter the letter: ").lower()
        counter =0
        self.flipped = self.flipped+1
        for y in range(len(self.word)):
            if x==self.word[y]:
                temp =list(self.guessWord)
                temp[y] = x
                self.guessWord ="".join(temp)
                counter =counter+1
                print("Letter guessed correctly.")
                print(self.guessWord)
        if self.word == self.guessWord:
            print("I told you all the letters! Just use 'tell me' next time.")
            self.caculateGameScore('t')
            self.gameStart()
        if counter==0:
            self.missedLetter =self.missedLetter+1
            print("Wrong guess. Better luck next time!!")
        
    def tellME(self):
        '''
            This method is responsible for tell Me Functionality.
            @param choice:User choice
        '''
        print("The word was "+self.word)
        self.caculateGameScore('t')
        self.gameStart()
    
    def quitME(self): 
        '''
            This method is responsible for Quit Functionality.
            @param choice:User choice
        '''
        self.gameStart()
    def caculateGameScore(self,optionCh):
        '''
            This method is responsible for score calculation. It creates object of class GamePlay which maintains specific game state.
            @param optionCh:User choice
            @see: GamePlay
        '''
        
        currentGame =GamePlay(self.word,self.gameNumber,self.flipped,optionCh,self.guessWord,self.guessType,self.missedLetter,self.badGuess)
        gameScore = currentGame.returnFinalScore()
        self.upddateDictionary(gameScore)
        if optionCh =='q':
            confirm =input("Are you sure you want to exit the game?(y/n)")
            if confirm=='y' or confirm=='Y':
                self.gameSummary()
            else:
                optionCh=input("Enter the next operation : t=tell me,q =quit,l= for letter, g = guess ")
                self.playGuess(optionCh)
    
    def upddateDictionary(self,currentGameScore):
        '''
            This method is responsible for updating final score card once a game is finished.
            @param currentGameScore:state of recently played game
        '''
        index =currentGameScore["Game Number"]
        if index>self.finalSummary.__len__():
            self.finalSummary.insert(self.gameNumber-1,currentGameScore)
        else:
            y =self.finalSummary[index-1]
            print()
            y["Status"] = currentGameScore["Status"]
            y["Score"] = currentGameScore["Score"]+y["Score"]
            y["Bad Guess"]=currentGameScore["Bad Guess"]
            self.finalSummary.pop(index-1)
            self.finalSummary.insert(index-1,y)

if __name__=="__main__":
    cntrl = GameController() 
    cntrl.gameStart()
