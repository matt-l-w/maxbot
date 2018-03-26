import re
import markovify

original_file = 'data/2018_06_03-OfficialSteelbankForever.txt'
cleaned_file = 'data/cleaned.csv'
author = 'Max Aghaeipour'

# clean original input file
with open(original_file, 'r', encoding="utf8") as input_file:
    with open(cleaned_file, 'w', encoding="utf8") as output_file:
        line_count = 0
        for line in input_file.readlines():            
            # search lines for author
            reg = re.search('(?<='+author+': ).*', line)
            if reg != None:
                message = reg.group(0)

                # remove media lines
                if '<Media omitted>' in line:
                    continue

                output_file.write(message + '\n')
                line_count += 1
        
        print("Generated {} lines of speech.".format(line_count))


# Get raw text as string.
with open(cleaned_file, encoding='utf8') as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)

# Print five randomly-generated sentences
print("Sentences:")
for i in range(5):
    print(text_model.make_sentence())

# Print three randomly-generated sentences of no more than 140 characters
print("Short Sentences:")
for i in range(3):
    print(text_model.make_short_sentence(140))