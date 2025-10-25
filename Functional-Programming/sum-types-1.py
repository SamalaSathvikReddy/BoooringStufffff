class MaybeParsed:
    pass


class Parsed(MaybeParsed):
    def __init__(self, doc_name, text):
        self.doc_name = doc_name
        self.text = text 


class ParseError(MaybeParsed):
    def __init__(self, doc_name, err):
        self.doc_name = doc_name
        self.err = err

# Enums
from enum import Enum
Doc = Enum('Doctype', ['PDF', 'TXT', 'DOCX', 'MD', 'HTML'])
print(Doc.PDF)


