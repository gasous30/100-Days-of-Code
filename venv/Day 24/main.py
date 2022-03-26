#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


from xml.etree.ElementTree import tostring


with open('Input\Letters\starting_letter.txt') as f:
    letter_lines = f.readlines()

with open(r"Input\Names\invited_names.txt") as f:
    names = f.readlines()

for name in names:
    dear_lines = letter_lines.copy()
    dear_lines[0] = dear_lines[0].replace('[name]',name.strip('\n'))

    file_name = 'letter_to_' + name.strip('\n') + '.txt'
    f = open(r"Output\ReadyToSend\{file_name}".format(file_name=file_name), 'w')
    for line in dear_lines:
        f.write(line)
    f.close()

