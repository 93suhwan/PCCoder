import json
from model.model import PCCoder
from scripts.solve_problems import load_problems, solve_problems
import argparse

thresholds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50]
model = PCCoder()
model.load('./createdModel/model')
model.eval()

parser = argparse.ArgumentParser()
parser.add_argument('input_path', type=str)
parser.add_argument('max_prog_leng', type=str)

args = parser.parse_args()

errors = [args.input_path]

for error in errors:
  print(args.max_prog_leng)
  print(error)
  for threshold in thresholds:
      problems = load_problems('./data/changed_test_dataset_' + args.max_prog_leng + '_' + error)
                                    
      print(threshold)
      res = solve_problems(problems, 'beam_repair', model, 5, int(args.max_prog_leng), 819200, 16, threshold)
      print("")

      solved = len([x for x in res if x['result'] != 'Failed'])
      print("Solved: %d\\%d:" % (solved, len(res)), str(100.0 * solved / len(res)) + '%')

      open('./result/beam_repair/result_' + args.max_prog_leng + '/result_' + error + '/result_repair_' + str(space), 'w+').write('\n'.join([json.dumps(x) for x in res]))
