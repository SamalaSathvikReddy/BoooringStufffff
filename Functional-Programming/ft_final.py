"""
Complete the get_filter_cmd function. It takes two functions as input, filter_one and filter_two, and returns a function, filter_cmd.

filter_cmd should take as input two strings: content and option.

Set the default value of the option argument to --one.
Complete filter_cmd so that it filters and returns the content according to the input option.
If --one, use filter_one
If --two, use filter_two
If --three, use filter_one first, then use filter_two
If another option is passed, raise an exception, "invalid option"
"""


def get_filter_cmd(filter_one, filter_two):
    def filter_cmd(content, option=1):
        if option == 1:
            filter_one(content)
        if option == 2:
            filter_two(content)
        if option == 3:
            filter_two(filter_one(content))
        else:
            raise Exception("invalid option")

    return filter_cmd


# don't touch below this line


def replace_bad(text):
    return text.replace("bad", "good")


def replace_ellipsis(text):
    return text.replace("..", "...")


def fix_ellipsis(text):
    return text.replace("....", "...")

