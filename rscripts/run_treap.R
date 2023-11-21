library(treap)


args = commandArgs(trailingOnly=TRUE)

prefix <- args[1]
f_fdr <- args[2]
pgi <- args[3]
outdir <- args[4]

print(prefix)

# prefix <- "GBM123IC_SKL31010_DE000158"
# f_fdr <- "/home/yeye/data2/works/DrugTargetPrediction/treap_test/data/1.pval/GBM123IC_SKL31018.DE000158.FDR.txt"
# pgi <- read.csv("../data/3.pgi/GBM_pgi.tsv", sep="\t")[c("sym1", "sym2")]
# pgi <- read.csv("../data/3.pgi/NSCLC_pgi.tsv", sep="\t")[c("sym1", "sym2")]

#########################################

fdr <- read.table(f_fdr, row.names=1, header=T)
colnames(fdr) <- prefix


genesym = rownames(fdr)

if (pgi == 'default'){pgi <- pgi.b} else {}
print(head(pgi))

btw = btw_pro(ppi=ppi.hm, pgi=pgi, genesym=genesym)
scores = treap(adj=fdr, btw=btw)

head(sort(scores[, prefix], decreasing=T))

# scores = merge(scores.gbm.1932, scores.gbm.2556, by.x=0, by.y=0, all=T)

head(scores)
outfile <- sprintf("%s/%s.TreapScore.tsv", outdir, prefix)
write.table(scores, sep="\t", quote=F, file=outfile)
# print(outfile)
print("Done run_treap.R")
