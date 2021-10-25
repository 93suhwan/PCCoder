# RepCoder
The official implementation of the paper "RepCoder: An Automated Program Repair Framework for Probability-Based Program Synthesis":
URL will be added later.

## Requirements
- Python 3.6 
- Pytorch >= 0.4.0 
- pathos 
- tqdm

## Generating a dataset (Erroneous programs)
You can generate erroneous programs using original correct codes.

First, you have to generate a correct dataset using the script of PCCoder.

Next, generate Erroneous programs using the previous dataset with the number of errors, as follows:
```
python3 makeErrorFile.py data/test_dataset_5 2
```

## Repair
We use PCCoder as a default predictor for a next statement. 

If you want to change the predictor, change the model name and the location of the model in repair.py line 7, 8

For example, If you want to repair data/changed_test_dataset_5_two with length 5 and 2 errors, as follows:
```
python3 repair.py data/changed_test_dataset_5_two 5
```

## Program representation
We use a program of deepcoder's dsl which is displayed in string format.

As in https://github.com/dkamm/deepcoder, a string representing a program has two characteristics.
1. '|' delimits each statement
2. ',' delimits a function call and its arguments

We use json format include program, input-output examples, etc.
For example, a program:
```
Var0 <- [int]
Var1 <- int
Var2 <- Last Var0
Var3 <- Access Var2 Var0 
Var4 <- Take Var1 Var0 
Var5 <- ZipWith (-) Var4 Var0 
Var6 <- Take Var3 Var5
```
will be represented as representation of PCCoder:
```
{"program": "LIST|INT|TAIL,0|ACCESS,2,0|TAKE,1,0|ZIPWITH,-,4,0|TAKE,3,5", 
 "examples": [{"output": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "inputs": [[6, 6, 6, 3, 1, 4, 0, 10, 3, 2, 10, 10], 34]}, 
              {"output": [0, 0, 0, 0, 0, 0], "inputs": [[10, 11, 6, 8, 8, 6, 5, 1, 2, 3, 10, 11, 2], 52]}, 
              {"output": [0], "inputs": [[4, 1, 4, 4, 8, 1, 3, 4, 4, 5], 35]}, 
              {"output": [0, 0, 0, 0, 0, 0, 0], "inputs": [[10, 9, 7, 5, 1, 12, 9, 13, 2, 4, 12, 11, 4, 2, 1, 1, 2], 252]}, 
              {"output": [0, 0, 0, 0, 0, 0], "inputs": [[1, 14, 5, 1, 11, 13, 14, 10, 6, 12, 6, 13, 13, 3, 4, 8], 241]}]}
```
It would be generated code with two erroneous using makeErrorfile.py, it will be represented with "changedOP" as:
```
{"changedOp": [1, 2], 
 "examples": [{"output": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "inputs": [[6, 6, 6, 3, 1, 4, 0, 10, 3, 2, 10, 10], 34]}, 
              {"output": [0, 0, 0, 0, 0, 0], "inputs": [[10, 11, 6, 8, 8, 6, 5, 1, 2, 3, 10, 11, 2], 52]}, 
              {"output": [0], "inputs": [[4, 1, 4, 4, 8, 1, 3, 4, 4, 5], 35]}, 
              {"output": [0, 0, 0, 0, 0, 0, 0], "inputs": [[10, 9, 7, 5, 1, 12, 9, 13, 2, 4, 12, 11, 4, 2, 1, 1, 2], 252]}, 
              {"output": [0, 0, 0, 0, 0, 0], "inputs": [[1, 14, 5, 1, 11, 13, 14, 10, 6, 12, 6, 13, 13, 3, 4, 8], 241]}], 
 "program": "LIST|INT|TAIL,0|DROP,|ZIPWITH,-,4,0|TAKE,3,5"}
```

"ChangedOP" which means the position(s) of the changed statement except for inputs(LIST, INT) in the original code. 
## PCCoder
Our framework, RepCoder, uses PCCoder as the main predictor.

You can find the codes to generate the original correct code, train the predictive model, and how to use PCCoder.
- Paper: https://arxiv.org/abs/1809.04682
- URL: https://github.com/amitz25/PCCoder
