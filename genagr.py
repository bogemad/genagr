#!/usr/bin/env python3

import sys, os, argparse
from collections import defaultdict
try:
    from Bio import SeqIO
    from Bio.SeqRecord import SeqRecord
except ModuleNotFoundError:
    sys.exit("biopython not fount, please install.")

parser = argparse.ArgumentParser(description="Genagr - Gene name grabber, grab fasta sequences from an annotated reference using gene names")
parser.add_argument("-r", "--ref", required=True, help="Reference in genbank format.", action="store", dest="ref", type=os.path.abspath)
parser.add_argument("-o", "--output", required=True, help="Fasta file containing desired gene sequences", action="store", dest="output", type=os.path.abspath)
parser.add_argument("-l", "--genelist", required=True, help="Text file containing gene names, one per line.", action="store", dest="genelist", type=os.path.abspath)
parser.add_argument("-d", "--db_name", required=True, help="Database name for ABRicate.", action="store", dest="db_name")

args = parser.parse_args()

recs = SeqIO.to_dict(SeqIO.parse(args.ref, 'genbank'))

info_d = defaultdict(dict)

for rec in recs.values():
    for feat in rec.features:
        if feat.type == 'CDS':
            if 'gene' in list(feat.qualifiers):
                info_d['gene'][feat.qualifiers['gene'][0]] = (rec.id, feat)
            if 'locus_tag' in list(feat.qualifiers):
                info_d['locus_tag'][feat.qualifiers['locus_tag'][0]] = (rec.id, feat)
            if 'old_locus_tag' in list(feat.qualifiers):
                info_d['old_locus_tag'][feat.qualifiers['old_locus_tag'][0]] = (rec.id, feat)

outrecs = []

with open(args.genelist) as gl:
    for line in gl:
        if line.strip() == '':
            continue
        gene = line.strip()
        found_qual = ''
        if gene in list(info_d['gene']):
            print("{} found in gene qualifier.".format(gene))
            found_qual = 'gene'
        elif gene in list(info_d['locus_tag']):
            print("{} found in locus_tag qualifier.".format(gene))
            found_qual = 'locus_tag'
        elif gene in list(info_d['old_locus_tag']):
            print("{} found in old_locus_tag qualifier.".format(gene))
            found_qual = 'old_locus_tag'
        else:
            print("{} not found in reference".format(gene))
            continue
        outrecs.append(SeqRecord(seq=info_d[found_qual][gene][1].extract(recs[info_d[found_qual][gene][0]].seq), id='{}~~~{}~~~{}~~~{}'.format(args.db_name, gene, info_d[found_qual][gene][0], 'undetermined'), name='', description=''))

outseqs = SeqIO.write(outrecs, args.output, 'fasta')
print("{} genes output to {}".format(outseqs, args.output))
