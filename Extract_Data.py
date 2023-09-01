import os
import lzma
from tqdm import tqdm

def xz_files_in_dir(dir):
    files = []
    for filename in os.listdir(dir):
        if filename.endswith(".xz") and os.path.isfile(os.path.join(dir, filename)):
            files.append(filename)
    return files

folder_path = "openwebtext"
output_train_file = "output_train.txt"
output_val_file = "output_val.txt"
vocab_file = "vocab.txt"


files= xz_files_in_dir(folder_path)

total_files = len(files)

#calculate split index
split_index = int(total_files *0.9)
files_train = files[:split_index]
files_val = files[split_index:]

vocab = set()

#process the training files:
with open(output_train_file, "w", encoding='utf-8') as outfile:
    for filename in tqdm(files_train,total=len(files_train)):
        file_path = os.path.join(folder_path, filename)
        with lzma.open(file_path, "rt", encoding='utf-8') as infile:
            text = infile.read()
            outfile.write(text)
            characters = set(text)
            vocab.update(characters)

#process the validation file:
with open(output_val_file, "w", encoding='utf-8') as outfile:
    for filename in tqdm(files_val ,total=len(files_val)):
        file_path = os.path.join(folder_path, filename)
        with lzma.open(file_path, "rt", encoding='utf-8') as infile:
            text = infile.read()
            outfile.write(text)
            characters = set(text)
            vocab.update(characters)

#write the vocabulary ti vocab.txt
with open(vocab_file, 'w', encoding='utf-8') as vfile:
    for char in vocab:
        vfile.write(char  + "\n")