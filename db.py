import sys
from database import Database



def main(argv):
	db = Database()
	line = sys.stdin.readline().rstrip()
	# Program finished when END indicated
	while line != "END":
		command = line.split(" ")

		result = db.handle_command(command[0], command[1:])
		if result != None:
			print result
		line = sys.stdin.readline().rstrip()


if __name__ == '__main__':
	main(sys.argv)