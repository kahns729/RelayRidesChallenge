import os, sys, filecmp, tempfile



def main(argv):
	if len(argv) < 2:
		print("usage: python test.py [tests_directory]")
		os._exit(1)
	inputs_path = argv[1] + "/inputs/"
	outputs_path = argv[1] + "/outputs/"
	for filename in os.listdir(os.path.abspath(inputs_path)):
		# Temp file to store each test's output
		tmp = tempfile.NamedTemporaryFile()
		# Call our program and use tmp to store output
		os.system("python db.py < "+inputs_path+filename+" > "+tmp.name)
		# Compare temp file with expected output
		if filecmp.cmp(tmp.name, outputs_path + filename):
			print(filename + " passed")
		else:
			print(filename + " failed")
		tmp.close()

if __name__ == '__main__':
	main(sys.argv)