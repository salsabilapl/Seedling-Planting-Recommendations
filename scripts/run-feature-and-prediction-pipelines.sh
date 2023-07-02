#!/bin/bash

set -e


jupyter nbconvert --to notebook --execute Klasifikasi-Feature-Pipeline.ipynb
jupyter nbconvert --to notebook --execute Klasifikasi-Batch-Inference-Pipeline.ipynb