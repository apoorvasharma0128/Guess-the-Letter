'''
Created on May 14, 2019

@author: apoorvasharma
'''
class GamePlay:
    def __init__(self, word,gameNumber,flipped,choice,gueesWord,guessType,missedLetter,badGuess) :
        self.word=word
        self.status =""
        self.gameNumber =gameNumber
        self.guessWord = gueesWord
        self.flipped =flipped
        self.choice =choice
        self.totalScore =1 
        self.guessType =guessType
        self.missedLetter = missedLetter
        self.badGuess =badGuess;
        self.table = self.setFrequencyTable()
        self.caculateGameScore()
        
    # Responsible for setting the frequencies of alphabets
    def caculateGameScore(self):
        if self.choice=='t':
            self.tellMEScore(self.word,self.guessWord)
        if self.choice=='g':
            self.guessScore(self.word,self.guessWord)
    
    def guessScore(self,word,guessWord):
        tempScore =0;
        if self.guessType=='c':
            self.status ="Success"
            for y in range(len(word)):
                if guessWord[y]!= word[y] and guessWord[y]=='-':
                    tempScore =tempScore+float(self.table[word[y]])
            self.totalScore =self.totalScore+(tempScore/(self.flipped+1))
        else:
            tempScore =0.1 * self.totalScore
            self.totalScore =self.totalScore-tempScore
            
            
    # Responsible for calculating score of game for tell  me 
    def tellMEScore(self,word,guessWord):
        tempScore =0;
        self.status ="Gave up"
        if word==guessWord: # Special case of tell me where all the letters are flipped one by one
            guessWord="----"
        for y in range(len(word)):
            if guessWord[y]!= word[y] and guessWord[y]=='-':
                tempScore =tempScore+float(self.table[word[y]])
        self.totalScore =self.totalScore-tempScore
    
    def returnFinalScore(self):
        scoreCard ={
            "Game Number" :self.gameNumber,
            "Word":self.word,
            "Status":self.status,
            "Bad Guess":self.badGuess,
            "Missed Letter":self.missedLetter,
            "Score":self.totalScore -float(1)
            }
        return scoreCard
    # Responsible for setting the frequencies of alphabets
    def setFrequencyTable(self):
        
        frequencyTable ={
            "a" :  8.17,
            "b" :  1.49,
            "c" :  2.78,
            "d" :  4.25,
            "e" :  12.70,
            "f" :  2.23,
            "g" :  2.02,
            "h" :  6.09,
            "i" :  6.97,
            "j" :  0.15,
            "k" :  0.77,
            "l" :  4.03,
            "m" :  2.41,
            "n" :  6.75,
            "o" :  7.51,
            "p" :  1.93,
            "q" :  0.10,
            "r" :  5.99,
            "s" :  6.33,
            "t" :  9.06,
            "u" :  2.76,
            "v" :  0.98,
            "w" :  2.36,
            "x" :  0.15,
            "y" :  1.97,
            "z" :  0.07,   
        }
        return frequencyTable
    