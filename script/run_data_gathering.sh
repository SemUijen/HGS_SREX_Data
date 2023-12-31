#!/bin/bash
#SBATCH --job-name=test_creation_speed
#SBATCH --output=logging/test_creation_speed-%j.out
#SBATCH --error=logging/test_creation_speed-%j.error
#SBATCH --chdir /home/suijen/HGS_SREX_Data
#SBATCH --export=ALL
#SBATCH --get-user-env=L

#SBATCH --partition=genoa
#SBATCH --nodes=1
#SBATCH --ntasks=192
#SBATCH --time=50:00:00

#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --mail-user=s.j.uijen@tilburguniversity.edu

# Setup modules
if [ ! -z "${SLURM_JOB_ID}" ]; then
    module purge
    module load 2022
    module load Python/3.10.4-GCCcore-11.3.0
    module load aiohttp/3.8.3-GCCcore-11.3.0
    module load matplotlib/3.5.2-foss-2022a
    module load SciPy-bundle/2022.05-foss-2022a
fi

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