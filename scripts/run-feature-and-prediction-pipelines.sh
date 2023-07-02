#!/bin/bash

set -e


jupyter nbconvert --to notebook --executePreprocessor.kernel_name=python3 Klasifikasi-Feature-Pipeline.ipynb
jupyter nbconvert --to notebook --executePreprocessor.kernel_name=python3 Klasifikasi-Batch-Inference-Pipeline.ipynb