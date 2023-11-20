# Drug Target Predictor (by TREAP) 
DEG 분석 결과로 부터 drug target 예측 (TREAP 알고리즘 이용)

# Installation
```sh
$ git clone https://github.com/JiyeKim/TargetPredictor.git
$ cd TargetPredictor
$ pip install -r requirements.txt

# usage
$ python targetpred.py -h
test.py -i [path/to/input] -o [path/to/outputdir] -p [prefix]

# for test
$ cd test/
$ ./example.sh
Input file is  ./input.result.txt
Results will be in  ./out
Rscript /data2/works/DrugTargetPrediction/TargetPredictor/rscripts/run_treap.R example ./out/example.FDR.txt default ./out > ./out/log 2> ./out/err
Created ./out/example.TreapScore.tsv
Finished.

```

# reference
- Wang M, Luciani LL, Noh H, Mochan E, Shoemaker JE. TREAP: A New Topological Approach to Drug Target Inference. Biophys J. 2020 Dec 1;119(11):2290-2298. doi: 10.1016/j.bpj.2020.10.021. Epub 2020 Oct 29. PMID: 33129831; PMCID: PMC7732766.
- https://github.com/ImmuSystems-Lab/TREAP
