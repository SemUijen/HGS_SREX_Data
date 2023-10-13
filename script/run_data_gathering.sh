#!/bin/bash
#SBATCH --job-name=test_creation_speed
#SBATCH --output=/logging/test_creation_speed-%j.out
#SBATCH --error=/logging/test_creation_speed-%j.error
#SBATCH --chdir /home/suijen/HGS_SREX_Data
#SBATCH --export=ALL
#SBATCH --get-user-env=L

#SBATCH --partition=genoa
#SBATCH --nodes=1
#SBATCH --ntasks=18
#SBATCH --time=03:00:00

#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --mail-user=s.j.uijen@tilburguniversity.edu

# Setup modules
module load 2022
module load Python/3.10.4-GCCcore-11.3.0
module purge


# Log versions
echo "PYTHON_VERSION = $(python3.10 --version)"
echo "PIP_VERSION = $(pip3.10 --version)"

# Setup environment
if [ -f .env ]; then
    export $(cat .env | xargs)
fi
export PYTHONPATH=src

# Setup dependencies
pip3.10 install -q \
    tqdm \
    numpy \
    pyvrp \


# Run experiment
python3.10 -m main
