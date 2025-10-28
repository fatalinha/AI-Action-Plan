"""
Meaning making and information integrity in the age of AI

Usage: python3 merge-text.py <folder_extracted_pdfs> <folder_resplit_txts> """

import os
import sys
import stanza

# Initialize the Stanza pipeline for English
nlp = stanza.Pipeline(lang='en', processors='tokenize', use_gpu=False)

# Paths
source_folder = sys.argv[1] #"/90-fr-9088-combined-responses/90-fr-9088-combined-responses/txt"
destination_folder = sys.argv[2] #"/90-fr-9088-combined-responses/90-fr-9088-combined-responses/txt_merged"
os.makedirs(destination_folder, exist_ok=True)

# Loop through each .txt file in the source folder
for filename in os.listdir(source_folder):
    if filename.endswith('.txt'):
        print(filename)
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)

        # Read and merge lines into a single block of text
        with open(source_path, 'r', encoding='utf-8') as f:
            content = f.read()
            #merged_text = ' '.join(line.strip() for line in f if line.strip())
            # basic text cleaning
            content = content.replace("", "").replace("•","").replace("●","").replace("​","")
            # Split text into paragraphs
            paragraphs = content.split('\n\n')


        # Write the sentences to the destination file
        with open(destination_path, 'w', encoding='utf-8') as f_out:
            for paragraph in paragraphs:
                paragraph = paragraph.strip().replace('\n', ' ')
                if not paragraph:
                    continue
                # Use Stanza to split paragraph into sentences
                doc = nlp(paragraph)
                for sentence in doc.sentences:
                    f_out.write(sentence.text + '\n')
                f_out.write('\n')  # Add an empty line to separate paragraphs


print('Processing complete!')
