#!/bin/bash


WRKDIR=$1
LINKS=$2

# Download responses
echo "Step 1: Download data"
wget -P $WRKDIR https://files.nitrd.gov/90-fr-9088/90-fr-9088-combined-responses.zip 

# Unzip
echo "Step 2: Unzipping data"
unzip $WRKDIR/90-fr-9088-combined-responses.zip 

echo $WKRDIR

# Convert pdf to txt
echo "Step 3: convert pdf to txt"
mkdir -p $WRKDIR/txt
for pdff in $WRKDIR/90-fr-9088-combined-responses/*.pdf
do
	bname=$(basename "${pdff%.*}")
	pdftotext $pdff $WRKDIR/txt/$bname.txt
done

# Merge and split paragraphs into sentences
echo "Step 4: sentence-split"
mkdir -p $WRKDIR/merged
python3 $LINKS/merge-text.py $WRKDIR/txt $WRKDIR/merged

# Clean texts
echo "Step 5: Clean files"
python3 $LINKS/clean-corpus.py $WRKDIR/merged

# Separate respondents
echo "Step 6: Separate respondents"
python3 $LINKS/separate-respondents.py $LINKS $WRKDIR/merged $WRKDIR/

rm -rf $WRKDIR/merged
rm -rf $WRKDIR/txt

