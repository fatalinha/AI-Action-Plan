"""
Meaning making and information integrity in the age of AI
Given the subcorpora directory containing converted pdfs to text per group, cleans files and rewrites them to same dir.

Usage: python3 clean-corpus.py <path_files>  """
import os
import sys
import re

def normalize_quotes(txt):
    # Replace curly quotes with straight quotes
    return txt.replace('“', '"').replace('”', '"').replace("‘", "'").replace("’", "'").replace("â€","").replace("™","'")

# Pattern to detect lots of non-ASCII characters (e.g. corrupted text)
non_ascii_ratio_threshold = 0.3  # 30% or more non-ASCII characters → skip file

def is_probably_corrupted(txt):
    non_ascii_chars = sum(1 for c in txt if ord(c) > 127)
    return (non_ascii_chars / max(1, len(txt))) > non_ascii_ratio_threshold

# List of exact sentences to remove
remove_sentences = ["CAUTION: This email originated from outside your organization.",
"Exercise caution when opening attachments or clicking links, especially from unknown senders.",
'"This document is approved for public dissemination.',
"This document is approved for public dissemination.",
"The document contains no businessproprietary or confidential information.",
"Document contents may be reused by the government in developing the AI Action Plan and associated documents without attribution.",
'Document contents may be reused by the government in developing the AI Action Plan and associated documents without attribution."',
"All e-mails to and from this account are for NITRD official use only and subject to certain disclosure requirements.",
"If you have received this e-mail in error, we ask that you notify the sender and delete it immediately.",
"This electronic communication and any files transmitted with it are intended for the named recipient(s) only and may contain confidential, proprietary or legally privileged information.",
"If you have received this message in error, please advise the sender by reply email, and delete this message and any attachments.",
"Unauthorized individuals or entities are not permitted access to this information.",
"Any dissemination, distribution, disclosure, or copying of this information is unauthorized and strictly prohibited.",
"/"]

# List of sentence prefixes to remove
remove_startswith = ["From: To: Subject: Date:",
                     "As of: March 21, 2025 Received:",
                     "PUBLIC SUBMISSION Docket:",
                     "Recently Posted NSF Rules and",
                     "Document: NSF_FRDOC_0001",
                     "Submitter Information Email:",
                     "Attachments ",
                     "Sent from my iPad",
                     "Page ",
                     "PUBLIC SUBMISSION",
                     "Docket: NSF_FRDOC",
                     "Submitter Information Name:",
                     "Comments Due:",
                     "CONFIDENTIALITY NOTICE:",
                     "If you have received this email in error",
                     "Any disclosure, copying, distribution or use of this communication by someone other"]

# List of sentences to remove if contain string
remove_in = ["ostp-ai-rfi",
             "ASFAI.org",
             ".........................",
             "D'Souza"]

# Regex patterns
email_pattern = re.compile(r'\b[\w\.-]+@[\w\.-]+\.\w+\b') #[EMAIL]
url_pattern = re.compile(r'https?://\S+|www\.\S+') # [URL]
footnote_pattern = re.compile(r'\[\d+\]|\(\d+\)|\s\d+\s*$', re.MULTILINE)
single_number_pattern = re.compile(r'^\s*\d+\s*$')
starts_with_number_pattern = re.compile(r'^\d+\s')
spaced_chars_pattern = re.compile(r'(?:\b\w\b\s+){4,}')  # 4 or more single letters spaced out -> Remove spaces!


# Folder containing your .txt files
folder_path = sys.argv[1] #'txt_merged2' #'subcorpora'

# Loop through each subfolder
for filename in os.listdir(folder_path):

    if filename.endswith('.txt'):
        file_path = os.path.join(folder_path, filename)

        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()


            # Remove emails, URLs, and footnotes
            text = email_pattern.sub('', text)
            text = url_pattern.sub('', text)
            text = footnote_pattern.sub('', text)

            # Clean sentences
            cleaned = []
            for s in text.splitlines():
                s = normalize_quotes(s.strip())
                s = s.replace("General Comment", "").replace("FINAL DRAFT", "").replace("",'')
                s = s.strip()
                if not s:
                    continue  # Skip empty
                if s in remove_sentences:
                    continue
                if any(s.startswith(prefix) for prefix in remove_startswith):
                    continue
                if single_number_pattern.match(s):
                    continue
                if starts_with_number_pattern.match(s):
                    continue
                if spaced_chars_pattern.search(s):
                    continue
                if any(substr.lower() in s.lower() for substr in remove_in):
                    continue
                cleaned.append(s)


            # Write back cleaned text (joined with newlines, removing empty lines)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(cleaned))
