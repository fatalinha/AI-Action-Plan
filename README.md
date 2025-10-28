# AI-Action-Plan
Code for compiling the AI Action Plan corpus and further analysis

## Requirements
- See requirements.txt file
- Additionally install pdftotext: https://www.cyberciti.biz/faq/converter-pdf-files-to-text-format-command/

## Instructions for compiling the corpus
You can directly compile the corpus by running the bash file:

``` bash compile-corpus.sh work_dir links_dir```

where:
- ``` work_dir ``` is the working directory for procesing the files
- ``` links_dir ``` is the directory where the scripts and respondent*_links.txt are stored

The processed corpus will be stored in ``` work_dir ```.

## Steps
1. Downloads all individual responses from the NITRD website: https://files.nitrd.gov/90-fr-9088/90-fr-9088-combined-responses.zip
2. Unzip
3. Coverts pdfs to txt using pdftotext
4. Sentence split
5. Cleans data
6. Separates by respondent type
