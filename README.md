# RepCoder
The official implementation of the paper "RepCoder: An Automated Program Repair Framework for Probability-Based Program Synthesis":
URL will be added later.

## Requirements
- Python 3.6 
- Pytorch >= 0.4.0 
- pathos 
- tqdm

## Generating a dataset (Erroneous programs)
You can generate erroneous programs using original correct programs.

First, you have to generate a correct dataset using the script of PCCoder.

Next, erroneous programs using the dataset with the number of errors to be made, as follows:
```
python3 makeErrorFile.py data/test_dataset_5 2
```

## Repair
For example, you can repair the programs in a file "data/changed_test_data_5_two", each of which consists of 5 lines of code and 2 errors, as follows:
```
python3 repair.py data/changed_test_dataset_5_two 5
```
We use PCCoder as a default predictor for a next statement. 

If you want to change the predictor, change the model name and its location in line 7 and 8 in repair.py, respectively.

## Program representation
Programs are written in DeepCoder's DSL and displayed in a string format.

As in https://github.com/dkamm/deepcoder, we use the following notation.
1. '|' delimits each statement.
2. ',' delimits a function call and its arguments.

We use a JSON format to include a program, input-output examples, etc.

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
is represented as follows, as in PCCoder:
```
{"program": "LIST|INT|TAIL,0|ACCESS,2,0|TAKE,1,0|ZIPWITH,-,4,0|TAKE,3,5", 
 "examples": [{"output": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "inputs": [[6, 6, 6, 3, 1, 4, 0, 10, 3, 2, 10, 10], 34]}, 
              {"output": [0, 0, 0, 0, 0, 0], "inputs": [[10, 11, 6, 8, 8, 6, 5, 1, 2, 3, 10, 11, 2], 52]}, 
              {"output": [0], "inputs": [[4, 1, 4, 4, 8, 1, 3, 4, 4, 5], 35]}, 
              {"output": [0, 0, 0, 0, 0, 0, 0], "inputs": [[10, 9, 7, 5, 1, 12, 9, 13, 2, 4, 12, 11, 4, 2, 1, 1, 2], 252]}, 
              {"output": [0, 0, 0, 0, 0, 0], "inputs": [[1, 14, 5, 1, 11, 13, 14, 10, 6, 12, 6, 13, 13, 3, 4, 8], 241]}]}
```
If you generate a fault program with two errors using makeErrorFile.py and the above code, then it will be represented as follows:
```
{"changedOp": [1, 2], 
 "examples": [{"output": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "inputs": [[6, 6, 6, 3, 1, 4, 0, 10, 3, 2, 10, 10], 34]}, 
              {"output": [0, 0, 0, 0, 0, 0], "inputs": [[10, 11, 6, 8, 8, 6, 5, 1, 2, 3, 10, 11, 2], 52]}, 
              {"output": [0], "inputs": [[4, 1, 4, 4, 8, 1, 3, 4, 4, 5], 35]}, 
              {"output": [0, 0, 0, 0, 0, 0, 0], "inputs": [[10, 9, 7, 5, 1, 12, 9, 13, 2, 4, 12, 11, 4, 2, 1, 1, 2], 252]}, 
              {"output": [0, 0, 0, 0, 0, 0], "inputs": [[1, 14, 5, 1, 11, 13, 14, 10, 6, 12, 6, 13, 13, 3, 4, 8], 241]}], 
 "program": "LIST|INT|TAIL,0|DROP,2,0|TAKE,3,0|ZIPWITH,-,4,0|TAKE,3,5"}
```

where "changedOP" denotes the positions of the changed statements. (Input statements, e.g., LIST, INT, are never changed.)
## PCCoder
Our framework RepCoder uses PCCoder as the main predictor.

You can find the code to generate correct programs and train the prediction model, and how to use PCCoder below.
- Paper: https://arxiv.org/abs/1809.04682
- URL: https://github.com/amitz25/PCCoder
