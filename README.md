# RepCoder
The official implementation of the paper "RepCoder: An Automated Program Repair Framework for Probability-Based Program Synthesis":
URL will be added later.

## Requirements
- Python 3.6 
- Pytorch >= 0.4.0 
- pathos 
- tqdm

## Generating a dataset (Erroneous programs)
How to create data with errors is as follows.(makeErrorfile.py)
First, you have to generate correct codes using script of PCCoder.
Second, to generate Erroneous programs:
```
python3.6 makeErrorFile.py data/test_dataset_10 10
```

## Repair codes
We use PCCoder using default predictor for next statement. If you want to change the predictor, change the model name and the location of model in repair.py line 7, 8
For example, to repair data/changed_test_dataset_5_three with length 5 and 3 errors:
```
python3.6 repair.py three 5
```

## PCCoder
Our framework, RepCoder, uses PCCoder as the main predictor.

You can find the code to generate the original correct code, train the predictive model, and how to use PCCoder.
- Paper: https://arxiv.org/abs/1809.04682
- URL: https://github.com/amitz25/PCCoder
