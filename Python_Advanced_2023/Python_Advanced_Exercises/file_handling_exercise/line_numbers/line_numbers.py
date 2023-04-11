def read_text():

    try:

        file = open("text.txt", "r")
        lines = [line for line in file]
        file.close()

    except FileNotFoundError:
        raise FileNotFoundError("File not found")

    for line in range(len(lines)):

        letters = 0
        punctuation_marks = 0

        for character in range(len(lines[line])):

            char = lines[line][character]

            if 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122:
                letters += 1

            elif 33 <= ord(char) <= 47 or 58 <= ord(char) <= 64:
                punctuation_marks += 1

        if lines[line][-1] == '\n':
            lines[line] = lines[line][:-1]

        lines[line] = f"Line {line+1}: {lines[line]} ({letters})({punctuation_marks})\n"

    return lines


def output_txt(text):

    file = open("output.txt", "w")
    [file.write(line) for line in text]
    file.close()

    file = open("output.txt", "r")
    output = ''.join([line for line in file])
    file.close()
    return output


text = read_text()
print(output_txt(text))