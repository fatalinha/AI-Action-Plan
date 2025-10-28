"""
Meaning making and information integrity in the age of AI

Usage: python3 separate-respondents.py <path_to_links> <folder_all_files> <output_folder> """
import os
import re
import sys
import shutil

# Paths
links_folder = sys.argv[1] 
source_folder = sys.argv[2] 
destination_folder = sys.argv[3] 



for respondent in ['individuals', 'industry-professional-scientificassoc', 'non-federal', 'non-profit', 'private-sector']:

    resp_folder = os.path.join(destination_folder, respondent)
    os.makedirs(resp_folder, exist_ok=True)
    txt_file_with_links = os.path.join(links_folder, (respondent + '_links.txt'))
    # Read the single line from the txt file
    with open(txt_file_with_links, 'r', encoding='utf-8') as f:
        line = f.read()

    # Extract filenames after 'title=' and keep only the last part after '/'
    # NOTE: all files:
    filenames = re.findall(r'title="[^"]+/([^/"]+)"', line)


    # Move each file to the destination folder if it exists
    for filename in filenames:
        full_name = (filename.replace(".pdf","") + ".txt")
        source_path = os.path.join(source_folder, full_name )
        dest_path = os.path.join(resp_folder, full_name)

        if os.path.exists(source_path):
            # Rename the copied file
            extension = '_' + str(respondent) + '.txt'
            new_filename = full_name.replace('.txt', extension)

            dest_path = os.path.join(resp_folder, new_filename)
            shutil.copy(source_path, dest_path)

            #print(f"Copied: { full_name}")
        else:
            print(f"File not found: { full_name}")

    print("File moving complete!")
