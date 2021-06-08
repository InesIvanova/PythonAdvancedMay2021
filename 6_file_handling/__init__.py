def get_file_content(path):
    with open(path, 'r') as data:
        data = ''.join(data.readlines())
        return pattern.findall(data.lower())

def write_to_file(data):
    for k, v in data:
        output_data = f'{k} - {v}'
        with open('output.txt', 'a') as file:
            file.write(output_data)
            file.write("\n")


import re
pattern = re.compile(r"[a-zA-Z\']+")

path_to_words = 'words.txt'
path_to_input = 'input.txt'

get_words = get_file_content(path_to_words)
get_text = get_file_content(path_to_input)

my_dect = {word:get_text.count(word) for word in get_words if word in get_text}
sorted_list = sorted(my_dect.items(), key=lambda x: -x[1])

write_to_file(sorted_list)

