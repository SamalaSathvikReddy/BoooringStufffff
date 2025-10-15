"""
    Complete the doc_format_checker_and_converter function.

It takes a conversion_function and a list of valid_formats as parameters. It should return a new function that takes two parameters of its own:

filename: The name of the file to be converted
content: The content (body text) of the file to be converted
If the file extension of the filename is in the valid_formats list, then it should return the result of calling the conversion_function on the content.
Otherwise, it should raise a ValueError with the message invalid file format.
"""



def doc_format_checker_and_converter(conversion_function, valid_formats):
    def inner_func(file_name, content):
        extension = (list(file_name.split('.')))[1]
        if extension in valid_formats:
            conversion_function(content)
        else:
            raise ValueError("invalid file format")
    return inner_func


# Don't edit below this line


def capitalize_content(content):
    return content.upper()


def reverse_content(content):
    return content[::-1]

