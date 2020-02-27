"""
file: main.py

Question selector
"""

# question container
class Question:
    """
    Question class
    """
    def __init__(self):
        pass

    def add_header(self, header):
        pad

    def add_part(self, header):

# worksheet class
class Worksheet:
    """
    LaTeX worksheet class
    """
    def __init__(self, preamble):
        """constructor"""
        self.__preamble_filename__ = preamble
        self.__preamble_text__ = ""
        self.__document_text__ = ""
        self.__questions__ = []
        
    def add_question():
        pass

    def build_doc(self):
        """build worksheet"""

        # get preamble
        with open(self.__preamble_filename__) as f:
            self.__preamble_text__ = f.read()

        # assemble
        self.__document_text__ = self.__preamble_text__

    def get_doc(self):
        """worksheet document getter"""
        return self.__document_text__

# worksheet instance
worksheet = Worksheet("data/preamble.tex")
worksheet.build_doc()
document = worksheet.get_doc()

# return worksheet
print(document)
