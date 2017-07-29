class pieces_queue():

	def __init__(self):
		self.current_permutation = []
		self.pieces_queue = [self.get_next_piece() for i in range(5)]

	def get_next_piece(self):
		if len(current_permuation) == 0:
			self.current_permuatation = np.arange(7)
			np.random.shuffle(ar)
			return self.current_permutation.pop(0)
		else:
			return self.current_permutation.pop(1)

	def cycle_drop(self):
		self.pieces_queue.append(self.get_next_piece())
		return self.pieces_queue.pop(0)

	def get_new_piece(self):
		piece_enum = self.cycle_drop()
		if piece_enum == 0:
			return yellow()
		if piece_enum == 1:
			return cyan()
		if piece_enum == 2:
			return blue()
		if piece_enum == 3:
			return orange()
		if piece_enum == 4:
			return green()
		if piece_enum == 5:
			return red()
		if piece_enum == 6:
			return purple()



def play_game():
	# fast drop is 20 lines per second
	board = np.array([[0 for i in range(20)]for i in range(10)])
	piece_clock = 0
	game_timer = 0
	second_timer = 0
	slow_drop_timer = 0
	command = None # down, left, right, rr, lr, hold, None
	pieces = pieces_queue()
	current_piece = pieces.

	# main game loop
	while game_timer < 120:
		elapsed = time.time()
		if command == "down":
			slow_drop_timer = 0
			current_piece.shift_down()

		
		elapsed = time.time() - elapsed
		time.sleep(.05 - elapsed)
		second_timer += 1
		slow_drop_timer += 1
		if second_timer == 20:
			second_timer = 0
			game_timer += 1
			if 
			slow_drop = True

