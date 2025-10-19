def converted_font_size(doc_type):
    def doc_check(font_size):
        if doc_type == "txt":
            return font_size
        if doc_type == "md":
            return font_size * 2
        if doc_type == "docx":
            return font_size * 3
        raise ValueError("invalid doc type")
    return doc_check


def lines_with_sequence(char):
    def with_char(length):
        sequence = char * length
        def with_length(doc):
            doc = list(doc.split('/n'))
            count = 0
            for st in doc:
                if "in" in st:
                    count+=1
            return count
        return with_length
    return with_char


