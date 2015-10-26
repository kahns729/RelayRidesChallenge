from collections import deque

class Database:
	def __init__(self):
		self.db = {}

	# Class method to handle command, and return the string result of
	#	running the command
	def handle_command(self, cmd, args):
		if cmd == "SET":
			return self.set(args)
		elif cmd == "GET":
			return self.get(args)
		elif cmd == "UNSET":
			return self.unset(args)
		elif cmd == "NUMEQUALTO":
			return self.numequalto(args)
		else:
			return "Error: no such command as " + cmd

	def set(self, args):
		self.db[args[0]] = args[1]

	def get(self, args):
		# Check that the item exists, then remove
		if args[0] in self.db:
			return self.db[args[0]]
		# We want to print NULL when the item does not exist
		else:
			return "NULL"

	def unset(self, args):
		self.db.pop(args[0], "Could not remove " + args[0])