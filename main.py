names = open('./Input/Names/invited_names.txt').readlines()

with open('./Input/Letters/starting_letter.txt') as template:
    temp = template.read()

    for name in names:
        name = name[:-1]
        letter = temp.replace('[name]', name)
        new_file = open(f'./Output/ReadyToSend/{name}_letter.txt', mode="w")
        new_file.write(letter)
