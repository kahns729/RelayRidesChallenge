from collections import deque
from transaction import Transaction

class Database:
	def __init__(self):
		self.db = {}
		# A stack of transaction blocks
		self.transactions = deque()


	# Class method to handle command, and return the string result of
	#	running the command.
	# 	rollback is a boolean that indicates whether this operation is being
	#	performed as part of a rollback. It defaults to False
	def handle_command(self, cmd, args, rollback = False):
		if cmd == "SET":
			return self.set(args, rollback)
		elif cmd == "GET":
			return self.get(args)
		elif cmd == "UNSET":
			return self.unset(args, rollback)
		elif cmd == "NUMEQUALTO":
			return self.numequalto(args)
		elif cmd == "BEGIN":
			return self.begin(args)
		elif cmd == "ROLLBACK":
			return self.rollback(args)
		elif cmd == "COMMIT":
			return self.commit(args)
		else:
			return "Error: no such command as " + cmd

	# rollback is a boolean that indicates whether this operation is being
	#	performed as part of a rollback. It defaults to False
	def set(self, args, rollback = False):
		if len(self.transactions) > 0 and not rollback:
			# Need to keep track of what's currently set to the value in
			#	database, for rollback
			rb_args = list(args)
			# If record already in database
			if args[0] in self.db:
				# Rollback should set record to previous value
				rb_args[1] = self.db[args[0]]
				self.transactions[-1].rollback_ops.append(("SET", rb_args))
			# If record not in database
			else:
				self.transactions[-1].rollback_ops.append(("UNSET", [args[0]]))
		self.db[args[0]] = args[1]
		

	def get(self, args):
		# Check that the item exists, then remove
		if args[0] in self.db:
			return self.db[args[0]]
		# We want to print NULL when the item does not exist
		else:
			return "NULL"

	# rollback is a boolean that indicates whether this operation is being
	#	performed as part of a rollback. It defaults to False
	def unset(self, args, rollback = False):
		if len(self.transactions) > 0 and not rollback:
			# Rollback should set value back to old value
			rb_args = [args[0], self.db[args[0]]]
			self.transactions[-1].rollback_ops.append(("SET", rb_args))
		# Remove value from database
		self.db.pop(args[0], "Could not remove " + args[0])

	def begin(self, args):
		self.transactions.append(Transaction(self))

	def rollback(self, args):
		if len(self.transactions) > 0:
			self.transactions.pop().rollback()
		else:
			return "NO TRANSACTION"

	def commit(self, args):
		self.transactions.clear()