import os
import sys
import getopt
import config

from utils import preprocess

TREAP_SCRIPT = config.PATH_CONFIG['TREAP_SCRIPT']


def main(argv):
    infile = ''
    outdir = ''
    opts, args = getopt.getopt(
        argv, "hi:o:p:", ["infile=", "outdir=", "prefix="])
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i [path/to/input] '
                  '-o [path/to/outputdir] -p [prefix]')
            sys.exit()
        elif opt in ("-i", "--infile"):
            infile = arg
        elif opt in ("-o", "--outdir"):
            outdir = arg
        elif opt in ("-p", "--prefix"):
            prefix = arg

    print('Input file is ', infile)
    print('Results will be in ', outdir)

    run(infile, outdir, prefix)


def run(infile, outdir, prefix="result"):
    input_ = f"{outdir}/{prefix}.FDR.txt"
    infile_processed = preprocess(infile)
    infile_processed.to_csv(input_, sep="\t")

    pgi = "default"

    # run treap
    cmd = f"Rscript {TREAP_SCRIPT} {prefix} {input_} {pgi} {outdir} > {outdir}/log 2> {outdir}/err"
    print(cmd)
    os.system(cmd)

    print(f"Created {outdir}/{prefix}.TreapScore.tsv") 
    print("Finished.")
    return infile_processed

if __name__ == "__main__":
    main(sys.argv[1:])


