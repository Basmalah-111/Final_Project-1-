from textfile import TextFileReader



def main():
    To_Display=TextFileReader('TextFile.txt')
    To_Display.read_file()
    To_Display.count_lines()
    To_Display.count_words()
    To_Display.count_characters()
    
    while True:
        
        choice=input('choose what you info you want to display:\n1-count number of lines\n2-count number of words\n3-count total number of characters\n4-display content of file\n:')
        if choice=='1':
            print (f'lines = {To_Display.line_count}')
        elif choice=='2':
            print (f'words = {To_Display.word_count}')
        elif choice =='3':
            print (f'characters = {To_Display.char_count}')
        elif choice =='4':
            print(f'content = {To_Display.content}')
        else:
            print('Invalid Option (please enter a number between 1 and 4)')

if __name__=='__main__':
    main()
