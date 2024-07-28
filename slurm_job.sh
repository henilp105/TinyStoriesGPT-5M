#! /bin/bash  

SBATCH --job-name=TinyStories_SLM-21BCE085

SBATCH --output=TinyStories_SLM-21BCE085_%j.log  

SBATCH --error=TinyStories_SLM-21BCE085_err_%j.log

SBATCH --nodes=1

SBATCH --ntasks-per-node=1

SBATCH --gres=gpu:1

cd $SLURM_SUBMIT_DIR

module load anaconda3

python train.py