file_path = '/Users/kevinz/workspace/python/practise/day3/text_files/pai.txt'

with open(file_path) as file_object:
    contents = file_object.read()
    print(contents)