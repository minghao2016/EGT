# Explore-Exploit Graph Traversal for Image Retrieval
Code for CVPR2019 paper: Explore-Exploit Graph Traversal for Image Retrieval

## Overview
Given global latent descriptors generated for a database of image (e.g. [R-MAC](http://www.europe.naverlabs.com/Research/Computer-Vision/Learning-Visual-Representations/Deep-Image-Retrieval)), EGT re-ranks nearest-neighbors to produce improved rankings.
<p>





## Dataset and Environment
* EGT requires java 1.8
* Graph generation and evaluation script is tested for Python 3.5
* For ROxford and RParis, please obtain dataset and evaluation code from https://github.com/filipradenovic/revisitop
* Download from https://s3.amazonaws.com/public.layer6.ai/landmark/EGT-DATA/evaluation.tar.gz to get the evaluation data

## Get Started

Run graph generation, EGT, then evaluation to produce the ROxford 5k results with `run_all.py`
<p>
The graph generation produces a kNN prebuild file that describes the weighted kNN graph.
Our EGT program takes this as input and produces output text file of the final ranking.
Additional script is provided to evaluate for ROxford and RParis.

## kNN "prebuild" file
* We provide Python script to generate initial kNN graph used as input to EGT, similar to other retrieval papers.
Inner product is computed and the results are sorted. The format of this file is row separated list of edges denoted by `<qid>` as the image id of the row, followed by pairs of `<id> <weight>` where `<id>` is the neighbor image id and `<weight>` is the edge weight.
```
<qid>,<id> <weight> <id> <weight> ... <id> <weight>
<qid>,<id> <weight> <id> <weight> ... <id> <weight>
...

<qid>,<id> <weight> <id> <weight> ... <id> <weight>
```
* Example to generate a "prebuild" file from embedding:
    ```
    cd python
    python egt.py --query_features ../data/roxHD_query_fused_3s_cq.npy \
        --index_features ../data/roxHD_index_fused_3s_cq.npy \
        --query_hashes query_hashes.txt --index_hashes index_hashes.txt \
        --Do_QE False --Num_candidates 300 --OutputFile prebuild_from_python.txt \
        --evaluate roxford5k
    ```
    
## EGT

* Execute EGT program jar with
` java -jar target/egt.jar`

* Example to generate the paper result from a prebuild file:
    ```
    java -jar target/egt.jar -k 250 -q 70 -t 420000 -p 5000 \
    python/prebuild_from_python.txt test.txt
    ```
     
* For research and development on top of EGT, see `src/main/java/EGT.java` on how to execute `EGTImpl` directly.
    
* To create executable jar, compile with
     `mvn clean compile assembly:single`

## Evaluation

* To evaluate a file with one header line:

    ```
    python evaluate_prebuild.py --f ../test.txt \
        --index_hashes index_hashes.txt --num_query 70 \
        --num_score 0 --evaluate roxford5k --skip 1
    ```
