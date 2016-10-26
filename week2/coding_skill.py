import json
import sys
from pprint import pprint

def read_json():
	with open(sys.argv[1], "r") as f:
		data = json.load(f)
 
	return data

pprint(read_json())