def read_txt_file(file_path):
    """Reads the contents of a text file and returns it as a string."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"Error: The file '{file_path}' was not found."
    except IOError:
        return "Error: An error occurred while reading the file."

class UserExtractor:
    def __init__(self, file_path):
        # Initialize the class with file_path and an empty dictionary for usernames
        self.file_path=file_path
        self.usernames={}
    def extract_usernames(self):
        """Extracts usernames from the text file and stores them in a dictionary."""
        # Use the external read_txt_file function to read the file
        content= read_txt_file(self.file_path)
        # Process the content to extract usernames
        lines = content.splitlines()
        for line in lines:
            parts=line.split(':')
            key=parts[0]
            value=parts[1]
            self.usernames[key]=value

# add the file_path
extractor = UserExtractor(r"C:\Users\Basmalah Wagdy\OneDrive\Desktop\amit_2\final_project1\task_6\text_file.txt")
extractor.extract_usernames()
print(extractor.usernames)

