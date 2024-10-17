import time
import pyRAPL
import argparse
import importlib
import gc

parser = argparse.ArgumentParser()
parser.add_argument('algo', type=str, help = "Algorithm to be run.")
args = parser.parse_args()

pyRAPL.setup()

module = importlib.import_module(args.algo)

@pyRAPL.measureit
def run(numbers):
    start_time = time.time()
    duration = 180 # 3 minutes
    while time.time() - start_time < duration:
        result = module.run(numbers)
        #time.sleep(0.000001)
    #result = module.run(numbers)
    gc.collect() # Making sure no trash remains for the next run

tuples = [(3.6, 0.2), (7.4, 0.3), (2.1, 0.1), (8.2, 0.15), (6.3, 0.25)]
run(tuples)