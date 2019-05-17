'''
Created on May 14, 2019

@author: apoorvasharma
'''
class DatabaseOperations:
    # Responsible for reading the  four_letters text
    def loadFile(self):
            word_list = []
            try:
                fileToRead = open("four_letters.txt","r")
                if fileToRead.mode== 'r':
                    readContent = fileToRead.read()
                    word_list.extend(readContent.split())
                    return word_list
            except:
                print("An exception has occurred. Cannot read the file.")

    