# genagr
Gene name grabber, grab fasta sequences from an annotated reference using gene names

```
usage: genagr.py [-h] -r REF -o OUTPUT -l GENELIST -d DB_NAME

Genagr - Gene name grabber, grab fasta sequences from an annotated reference using gene names

optional arguments:
  -h, --help            show this help message and exit
  -r REF, --ref REF     Reference in genbank format.
  -o OUTPUT, --output OUTPUT
                        Fasta file containing desired gene sequences
  -l GENELIST, --genelist GENELIST
                        Text file containing gene names, one per line.
  -d DB_NAME, --db_name DB_NAME
                        Database name for ABRicate.
```

## Test/Example data

```
python genagr.py -r test/sequence.gb -o test/testOut.fa -l test/testList.txt -d custom_db_name
```
