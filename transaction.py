class Transaction:
	def __init__(self, db):
		# Operations contains tuples of (command, args)
		self.rollback_ops = []
		# The database this transaction belongs to
		self.db = db
	def rollback(self):
		for (cmd, args) in self.rollback_ops:
			self.db.handle_command(cmd, args, rollback=True)
