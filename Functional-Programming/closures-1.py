import copy

def word_count_aggregator():
    count = 0
    doc = input("Enter the string")
    def word_count(doc):
        doc = list(doc.split())
        n = len(doc)
        nonlocal count
        count = count + n
        return count
    return word_count

def new_collection(initial_docs):
    def inside_func(s):
        nonlocal initial_docs
        initial_docs.append(s)
        return initial_docs
    return inside_func

def css_styles(initial_styles):
    def add_style(sec, pro, val):
        Copy = copy.deepcopy(initial_styles)
        if sec not in Copy:
            Copy[sec] = {}
        Copy[sec][pro] = val
        return Copy
    return add_style

my_collection = new_collection(["doc1", "doc2", "doc3"])
print(my_collection("doc4"))
# ['doc1', 'doc2', 'doc3', 'doc4']
print(my_collection("doc5"))
# ['doc1', 'doc2', 'doc3', 'doc4', 'doc5']


initial_styles = {
    "body": {
        "background-color": "white",
        "color": "black"
    },
    "h1": {
        "font-size": "16px",
        "padding": "10px"
    }
}

add_style = css_styles(initial_styles)

new_styles = add_style("p", "color", "grey")
print(new_styles)
# {
#    "body": {
#        "background-color": "white",
#        "color": "black"
#    },
#    "h1": {
#        "font-size": "16px",
#        "padding": "10px"
#    },
#    "p": {
#        "color": "grey",
#    }
# }
