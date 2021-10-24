import env.operator as op
import itertools
import random
from dsl.impl import FIRST_ORDER_FUNCTIONS, HIGHER_ORDER_FUNCTIONS
import json
import copy
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_path', type=str)
parser.add_argument('max_prog_leng', type=str)

args = parser.parse_args()

def cart(func, lambd):
  lst = []
  for element in itertools.product(func, lambd):
    lst.append(','.join(element))
  return lst

def argInt(func, maxLen):
  lst = []
  for length in range(1, maxLen + 1):
    string = func + ',' + str(length)
    lst.append(string)
  return lst

def changeOp(progList, changedOp, length, changeNum):
  if changeNum == 0:
    return progList, sorted(changedOp)
  while True:
    rNum = random.randrange(0, length)
    if rNum not in changedOp:
      changeNum -= 1
      changedOp.append(rNum)
      break
  for i in range(len(progList)):
    if progList[i] == 'LIST' or progList[i] == 'INT':
      rNum = rNum + 1
      continue
    else:
      break
  L2LOP = ['REVERSE', 'SORT'] \
          + cart(['MAP'], I2I) + cart(['FILTER'], I2B) + cart(['SCAN1L'], I2I2I) \
          + argInt('TAKE', rNum2) + argInt('DROP', rNum2)

  L2IOP = ['HEAD', 'TAIL', 'MINIMUM', 'MAXIMUM', 'SUM'] \
          + cart(['COUNT'], I2B) + argInt('ACCESS', rNum2)

  funcArgs = progList[rNum].split(',')

  if funcArgs[0] in L2I:
    if funcArgs[0] in ['ACCESS', 'COUNT']:
      origFunc = funcArgs[0] + ',' + funcArgs[1]
      funcArgs.remove(funcArgs[1])
    else:
      origFunc = funcArgs[0]
    funcArgs.remove(funcArgs[0])
    if origFunc in L2IOP:
      L2IOP.remove(origFunc)
      funcArgs = [L2IOP[random.randrange(0, len(L2IOP))]] + funcArgs
      L2IOP.append(origFunc)
    else:
      funcArgs = [L2IOP[random.randrange(0, len(L2IOP))]] + funcArgs
  elif funcArgs[0] in L2L:
    if funcArgs[0] in ['REVERSE', 'SORT']:
      origFunc = funcArgs[0]
    else:
      origFunc = funcArgs[0] + ',' + funcArgs[1]
      funcArgs.remove(funcArgs[1])
    funcArgs.remove(funcArgs[0])
    if origFunc in L2LOP:
      L2LOP.remove(origFunc)
      funcArgs = [L2LOP[random.randrange(0, len(L2LOP))]] + funcArgs
      L2LOP.append(origFunc)
    else:
      funcArgs = [L2LOP[random.randrange(0, len(L2LOP))]] + funcArgs
  elif funcArgs[0] in L2L2L:
    origFunc = funcArgs[0] + ',' + funcArgs[1]
    funcArgs.remove(funcArgs[1])
    funcArgs.remove(funcArgs[0])
    if origFunc in L2L2LOP:
      L2L2LOP.remove(origFunc)
      funcArgs = [L2L2LOP[random.randrange(0, len(L2L2LOP))]] + funcArgs
      L2L2LOP.append(origFunc)
    else:
      funcArgs = [L2L2LOP[random.randrange(0, len(L2L2LOP))]] + funcArgs
  else:
    print("Error")
  progList[rNum] = ','.join(funcArgs)

  return changeOp(progList, changedOp, length, changeNum)

L2I = ['HEAD', 'TAIL', 'MINIMUM', 'MAXIMUM', 'SUM', 'ACCESS', 'COUNT']
L2L = ['MAP', 'FILTER', 'SCAN1L', 'REVERSE', 'SORT', 'TAKE', 'DROP']
L2L2L = ['ZIPWITH']

I2I = ["+1", "-1", "*2", "/2", "*-1", "**2", "*3", "/3", "*4", "/4"]
I2B = [">0", "<0", "EVEN", "ODD"]
I2I2I = ["+", "-", "*", "max", "min"]

L2L2LOP = cart(L2L2L, I2I2I)

with open(args.input_path, 'r') as f:
  lines = f.read().splitlines()

leng = ['one', 'two', 'three', 'four', 'five']
leng1 = ['six', 'seven', 'eight']
leng2 = ['nine', 'ten']
leng3 = ['eleven', 'twelve']
leng4 = ['thirteen', 'fourteen']
leng5 = ['fifteen']
leng6 = ['sixteen']

if args.max_prog_leng == '8':
  leng += leng1
elif args.max_prog_leng == '10':
  leng += leng1
  leng += leng2
elif args.max_prog_leng == '12':
  leng += leng1
  leng += leng2
  leng += leng3
elif args.max_prog_leng == '14':
  leng += leng1
  leng += leng2
  leng += leng3
  leng += leng4
elif args.max_prog_leng == '15':
  leng += leng1
  leng += leng2
  leng += leng3
  leng += leng4
  leng += leng5
elif args.max_prog_leng == '16':
  leng += leng1
  leng += leng2
  leng += leng3
  leng += leng4
  leng += leng5
  leng += leng6
            
for i in range(len(lines)):
  data = json.loads(lines[i].rstrip())
  prog = data['program']
  progList = prog.split('|')
  for l in range(len(leng)):
    progListArg = copy.deepcopy(progList)
    results = changeOp(progListArg, [], int(args.max_prog_leng), l + 1)
    data['program'], data['changedOp'] = '|'.join(results[0]), results[1]
    with open('./data/changed_test_dataset_' + args.max_prog_leng + '_' + leng[l], 'a') as outFile:
      outFile.write(json.dumps(data) + '\n')

