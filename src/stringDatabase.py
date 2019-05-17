'''
This Module is responsible for performing I/O operations to four_letters text file
Created on May 14, 2019

@author: apoorvasharma
'''

class DatabaseOperations:
    '''
        Responsible for reading the  four_letters text
    '''
    # Responsible for reading the  four_letters text
    def loadFile(self):
        '''
            Responsible for reading the  four_letters text
            @return word_list: list of words in four_letters text file
            @raise exception: Custom Exception, in case of file related issue
        '''
        word_list = []
        try:
            fileToRead = open("four_letters.txt","r")
            if fileToRead.mode== 'r':
                readContent = fileToRead.read()
                word_list.extend(readContent.split())
                return word_list
        except:
            raise Exception("An exception has occurred. Cannot read the file.")

    