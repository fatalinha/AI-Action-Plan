# AI-Action-Plan
Code for compiling the AI Action Plan corpus and further analysis

## Requirements
- pdftotext: https://www.cyberciti.biz/faq/converter-pdf-files-to-text-format-command/
- unzip
- Stanza 
- Python 3.6


## Instructions for compiling the corpus
You can directly compile the corpus by running the bash file:

``` bash run.sh input_dir output_dir ```

## Steps
1. Downloads all individual responses from the NITRD website: https://files.nitrd.gov/90-fr-9088/90-fr-9088-combined-responses.zip
2. Unzip
3. Coverts pdfs to txt using pdftotext
4. Sentence split
5. Cleans data
6. Separates by respondent type
