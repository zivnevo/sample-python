class Boards:
    """
    This class represents a board configuration, namely the number of pebbles left in each line
    """
    def __init__(self):
        self.cache = {str([0, 0, 0, 0, 0, 1]): False}

    @staticmethod
    def get_board_children(board):
        """
        :param list board: The board to get children of
        :return list: A list of children boards
        """
        children = []
        for line_num, line in enumerate(board):
            for pebbles_left in range(0, line):
                new_child = board.copy()
                new_child[line_num] = pebbles_left
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

        # 1st player wins the board, if it has a child board which is loosing for *its* 1st player
        children = self.get_board_children(board)
        is_winning = not all(self.is_first_player_winning(brd) for brd in children)
        self.cache[board_str] = is_winning
        return is_winning


if __name__ == "__main__":
    if Boards().is_first_player_winning([3, 3, 5, 5, 6, 6]):
        print("First player is winning")
    else:
        print("First player is losing")
