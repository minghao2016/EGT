import sys
import subprocess
import os

# generate prebuild file
cmd = "cd python && python egt.py --query_features ../data/roxHD_query_fused_3s_cq.npy --index_features ../data/roxHD_index_fused_3s_cq.npy --query_hashes ../data/roxford_query_hashes.txt --index_hashes ../data/roxford5k_index_hashes.txt --Do_QE False --k 250 --OutputFile prebuild_from_python.txt && cd .."
subprocess.call(['/bin/bash', '-c', cmd])

print("finished prebuild")

# run egt
cmd = 'java -jar target/egt.jar -k 250 -q 70 -t 0.42 -p 5000 --time python/prebuild_from_python.txt test.txt'
subprocess.call(['/bin/bash', '-c', cmd])

print("finished EGT")

# evaluate
cmd = 'cd python && python evaluate_prebuild.py --f ../test.txt --index_hashes ../data/roxford5k_index_hashes.txt --num_query 70 --evaluate roxford5k && cd ..'
subprocess.call(['/bin/bash', '-c', cmd])

