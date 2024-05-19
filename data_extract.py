import lzma
import os
from tqdm import tqdm


def xz_files_in_dir(directory):
    return [filename for filename in os.listdir(directory) if filename.endswith(".xz") and os.path.isfile(os.path.join(directory, filename))]

folder_path = "C:/Users/Josh Eze/Downloads/openwebtext/openwebtext"
output_file_train = "output_train.txt"
output_file_val = "output_val.txt"
output_file = "output.txt"
vocab_file = "vocab.txt"
# split_files=int(input('How many files would you like to split this into?'))

files = xz_files_in_dir(folder_path)
total_files = len(files)
#processing files for training an validation separately
vocab = set()

#calculate split indices
# max_count = total_files // split_files if split_files != 0 else total_files
# split_index = int(total_files * .9)
# files_val = files[split_index:]
# files_train = files[:split_index]

#process training files
with open (output_file, 'w', encoding='utf-8') as outfile:
    for filename in tqdm(files, total=len(files)):
        file_path = os.path.join(folder_path, filename)
        with lzma.open(file_path, 'rt', encoding='utf-8') as infile:
            text = infile.read()
            outfile.write(text)
            characters = set(text)
            vocab.update(characters)

#process validation files
# with open (output_file_val, 'w', encoding='utf-8') as outfile:
#     for filename in tqdm(files_val, total=len(files_val)):
#         file_path = os.path.join(folder_path, filename)
#         with lzma.open(file_path, 'rt', encoding='utf-8') as infile:
#             text = infile.read()
#             outfile.write(text)
#             characters = set(text)
#             vocab.update(characters)



with open(vocab_file, 'w', encoding='utf-8') as vfile:
    for char in vocab:
        vfile.write(char + '\n')


