class GameBoard:
  def __init__(self, size_x = 10, size_y = 16) -> None:
    self.size_x = size_x
    self.size_y = size_y
    self.score = 0
    self.tower_height = 0 # need to keep track of this for AI purposes
    self.next_tetrimino = None
    self.falling_tetrimino = None

  def game_loop():
    # spawn (next) tetrimino
    # tetrimino falls until 1 `tick` after it cannot move or it is held 
    # tetrimino is `settled` 
    
    # if held -> restart loop with held tetrimino (or next if hold is empty)

    # if settled ->
    # compute state
    # generate new next tetrimino
    # loop
    pass

  def fall():
    """note: falling is only for the display since we will assume the desired position will be computed near instantly"""
    # take tetrimino coordinates and push the position down one.
    pass

  def spawn_block():
    # take a tetrimino and start it at the top of the screen
    # center based on leftmost block on (size_x / 2) - 1, where x is even
    pass

  def spawn_next_block():
    # spawn tetrimino from next 
    pass

  def hold_block():
    # if hold is empty -> hold tetrimino -> finish state
    # if hold is full -> spawn held tetrimino
    pass

  def compute_state():
    # find tower height
    # update score
    pass