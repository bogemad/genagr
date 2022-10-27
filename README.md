# genagr
Gene name grabber, grab fasta sequences from an annotated reference using gene names

```
usage: genagr.py [-h] -r REF -o OUTPUT -l GENELIST

Genagr - Gene name grabber, grab fasta sequences from an annotated reference using gene names

optional arguments:
  -h, --help            show this help message and exit
  -r REF, --ref REF     Reference in genbank format.
  -o OUTPUT, --output OUTPUT
                        Fasta file containing desired gene sequences
  -l GENELIST, --genelist GENELIST
                        Text file containing gene names, one per line.
```

## Test/Example data

```
python genagr.py -r test/sequence.gb -o test/testOut.fa -l test/testList.txt
```
