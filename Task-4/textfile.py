
with open ('TextFile.txt','w') as file:
        file.write("This is the first line.\nThis is the second line.\nAnd this is the third line.")
    

class TextFileReader:

    def __init__(self,file_path):
        self.__file_path=file_path
        self.line_count=''
        self.word_count=0
        self.char_count=0
        self.num_of_lines =[]
       
    def read_file(self):
        with open(self.__file_path, 'r') as file:
            self.content=file.read()

    def count_lines(self):
            self.num_of_lines = self.content.splitlines() #The splitlines() method splits a string into a list. The splitting is done at line breaks.
            self.line_count = len(self.num_of_lines)

    def count_words(self):
            self.word_count = sum(len(i.split()) for i in self.num_of_lines )
    
    def count_characters(self):
            self.char_count = sum(len(j) for j in self.num_of_lines)

    def display_content(self):
          print(self.content)
          

                 


