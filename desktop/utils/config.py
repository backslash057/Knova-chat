#third party library
import yaml

def load_config(path):
	file = open(path)
	
	config = yaml.safe_load(file)
	file.close()

	return config
