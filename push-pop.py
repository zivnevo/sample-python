class Boards:
    def __init__(self):
        self.cache = {str([0, 0, 0, 0, 0, 1]): False}

    @staticmethod
    def get_board_children(board):
        """
        :param list board: The board to get children of
        :return list: A list of children boards
        """
        children = []
        for line in range(0, len(board)):
            for pebbles_left in range(0, board[line]):
                new_child = board.copy()
                new_child[line] = pebbles_left
                new_child.sort()
                if new_child not in children:
                    children.append(new_child)
        return children

    def is_first_player_winning(self, board):
        """
        :param list board: The pebbles in each line of the board
        :return bool: if the first player is winning
        """
        board_str = str(board)
        if board_str in self.cache:
            return self.cache[board_str]

        # A board is winning for the 1st player, if it has a child board which is loosing for *its* 1st player
        is_winning = not all(self.is_first_player_winning(brd) for brd in self.get_board_children(board))
        self.cache[board_str] = is_winning
        return is_winning


if __name__ == "__main__":
    if Boards().is_first_player_winning([3, 3, 5, 5, 6, 6]):
        print("First player is winning")
    else:
        print("First player is losing")
