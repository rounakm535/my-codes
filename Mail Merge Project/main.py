MAIL_NAME = "[name]"

with open("./Input/Names/invited_names.txt") as names_files:
    names = names_files.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()

    for name in names:
        updated_name = name.strip()
        updated_letter = letter.replace(MAIL_NAME, updated_name)
        with open(f"./Output/ReadyToSend/letter_for_{updated_name}.txt", mode= "w") as send :
            send.write(updated_letter)