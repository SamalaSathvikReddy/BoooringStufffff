def factorial(x):
    if(x == 0 or x == 1):
        return 0
    return x * factorial(x-1)

zipfile = dict()
def zip_map(keys, values):
    if(len(keys) == 0 or len(values) == 0):
        return
    zip_map(keys[1:], values[1:])
    zipfile[key] = value
    return zipfile

def sum_nested_list(lst):
    total_sum = 0 
    for item in lst:
        if type(item) == int:
            total_sum += item 
        else:
            total_sum += sum_nested_list(item)
    return total_sum

def list_files(parent_directory, current_filepath=""):
    dirs = []
    for key in parent_directory:
        if parent_directory[key] == None:
            dirs.append(current_filepath + '/' + key)
        else:
            dirs.extend(list_files(key, current_filepath + '/' + key))

    return dirs

parent_directory = {
    "Documents": {
        "Proposal.docx": None,
        "Receipts": {
            "January": {
                "receipt1.txt": None,
                "receipt2.txt": None
            },
            "February": {
                "receipt3.txt": None
            }
        }
    },
}
current_filepath = ""
print(list_files(parent_directory, current_filepath))

