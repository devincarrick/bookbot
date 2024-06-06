# Change main.py so that instead of printing "hello world", it reads the contents of the "frankenstein.txt" and prints it all to the console.

def main():
    # path to the book
    book_path = "books/frankenstein.txt"
    # get the text from the book
    text = get_text(book_path)
    print(text)

# helper function to get the text from a file
def get_text(path):
    # with block opens a file
    with open(path) as f:
        # read contents of file into a string
        return f.read()
    
# Call the main function
if __name__ == "__main__":
    main()