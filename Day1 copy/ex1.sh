conda export > msds692_environment.yml --no-build
conda deactivate
conda remove -n msds692 --all
conda env create -f msds692_environment.yml -n msds692
conda env update -f msds602_environment.yml -n msds692
