def depth_first(dictionary,source):
    stack = [source]
    while stack != []:
        current = stack.pop()
        print(current, end=", ")
        for x in dictionary.get(current):
            stack.append(x)
    print()

def breath_first(dictionary,source):
    queue = [source]
    while queue != []:
        current = queue.pop(0)
        print(current, end=', ')
        for x in dictionary.get(current):
            queue.append(x)
    print()

def depth_first_recursive(dictionary,source):
    print(source)
    for neighbor in dictionary.get(source):
        depth_first_recursive(dictionary,neighbor)

# You cant make a breath_first recursive function

def has_path_df(dictionary,src,dst):
    if src == dst: return True
    for neighbor in dictionary[src]:
        if has_path_df(dictionary,neighbor,dst):
            return True
    return False

test_dict = {
        'a': ['b','c'],
        'b': ['d'],
        'c': ['e'],
        'd': ['f'],
        'e': [],
        'f': []
        }

print("depth first")
depth_first(test_dict,'a')
# depth_first_recursive(test_dict,'a')
print("breath first")
breath_first(test_dict,'a')
