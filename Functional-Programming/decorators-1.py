def file_type_aggregator(func_to_decorate):
    # dict of file_type -> count
    counts = {}

    def wrapper(doc, file_type):
        nonlocal counts

        if file_type not in counts:
            counts[file_type] = 0
        counts[file_type] += 1
        result = func_to_decorate(doc, file_type)

        return result, counts

    return wrapper

@file_type_aggregator
def process_doc():
    return f"Processing doc: '{doc}'. File Type: {file_type}"


def args_logger(*args, **kwargs):
    i = 1
    for val in args:
        print(f"{i}. {val}")
        i+=1 
    for k in kwargs:
        print(f"* {k} : {kwargs[k]}")

args_logger("hi", "there", age=17, date="July 4 1776")


def configure_plugin_decorator(func):
    def wrapper(*args):
        hm = dict()
        for t in args:
            hm[t[0]] = t[1]
        return hm
    return wrapper

@configure_plugin_decorator
def configure_backups(**kwargs):
    return kwargs

plugin_config = configure_backups(("path", "~/duplicates"), ("prefix", "duplicate_"), ("extension", ".rtf"))
print(plugin_config)


"""
    LRU Cache 
"""
from functools import lru_cache

@lru_cache()
def is_palindrome(word):
    left = 0
    right = len(word)-1
    if left >= right:
        return True
    if word[left] != word[right]:
        return False
    return is_palindrome(word[left+1:right])
    
print(is_palindrome("racecar"))
print(is_palindrome("string"))


def replacer(old, new):
    def replace(decorated_func):
        def wrapper(text):
            text = text.replace(old, new) 
            return decorated_func(text) 
        return wrapper 
    return replace

@replacer("&", "&amp;")
@replacer("<", "&lt;")
@replacer(">", "&gt;")
@replacer('"', "&quot;")
@replacer("'", "&#x27;")
def tag_pre(text):
    return f"<pre>{text}</pre>"
print(tag_pre("5 > 3 & 2 < 4"))

