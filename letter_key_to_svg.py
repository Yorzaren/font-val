import json
import os
import shutil


def write_letter_file(output_location, file_text):
    with open(output_location, 'w', encoding="utf-8") as text_file:
        text_file.write(file_text)


def generate_svg_folder(source_file, output_folder="svg_letters", input_glyphs="letters-1", split_folders=False):
    # Open the text file with the data
    with open(source_file, 'r', encoding="utf-8") as f:
        data = json.load(f)

    # print(data)

    parent_dir = output_folder
    letter_dir_src = input_glyphs

    if os.path.exists(parent_dir):
        shutil.rmtree(parent_dir)
    else:
        os.makedirs(parent_dir)

    if split_folders:
        # A-Z make folders and then add the glyphs
        for keys in data:
            # Make the folder
            this_folder = parent_dir + "/" + keys
            os.makedirs(this_folder)

            # String everything together and then output it as char.txt
            full_string = ""
            for char in data[keys]:
                full_string = full_string + char

            # Write a file to help test that the font will work.
            write_letter_file(this_folder+"/"+keys+".txt", full_string)

            # Now copy the symbols into the folder
            this_letter = keys.split("_")[1]
            print(this_letter)

            for char in data[keys]:
                shutil.copy(letter_dir_src+"/"+this_letter+".svg", this_folder+"/"+char+".svg")
    # Toss everything into the main output folder
    else:
        for keys in data:
            # String everything together and then output it as char.txt
            full_string = ""
            for char in data[keys]:
                full_string = full_string + char

            # Write a file to help test that the font will work.
            write_letter_file(parent_dir + "/" + keys + ".txt", full_string)

            # Now copy the symbols into the folder
            this_letter = keys.split("_")[1]
            print(this_letter)

            for char in data[keys]:
                shutil.copy(letter_dir_src + "/" + this_letter + ".svg", parent_dir + "/" + char + ".svg")


if __name__ == '__main__':
    generate_svg_folder("dict.txt", split_folders=False)