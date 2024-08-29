import numpy as np
import pygame
import sys
import math
import random

class Colors:
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)

class ConnectFour:
    def __init__(self):
        self.ROW_COUNT = 6
        self.COLUMN_COUNT = 7
        self.board = self.create_board()
        self.game_over = False
        self.turn = 0

    def create_board(self):
        return np.zeros((self.ROW_COUNT, self.COLUMN_COUNT))

    def drop_piece(self, row, col, piece):
        self.board[row][col] = piece

    def is_valid_location(self, col):
        return self.board[self.ROW_COUNT - 1][col] == 0

    def get_next_open_row(self, col):
        for r in range(self.ROW_COUNT):
            if self.board[r][col] == 0:
                return r

    def print_board(self):
        print(np.flip(self.board, 0))

    def winning_move(self, piece):
        # Check horizontal locations for win
        for c in range(self.COLUMN_COUNT - 3):
            for r in range(self.ROW_COUNT):
                if self.board[r][c] == piece and self.board[r][c+1] == piece and \
                   self.board[r][c+2] == piece and self.board[r][c+3] == piece:
                    return True

        # Check vertical locations for win
        for c in range(self.COLUMN_COUNT):
            for r in range(self.ROW_COUNT - 3):
                if self.board[r][c] == piece and self.board[r+1][c] == piece and \
                   self.board[r+2][c] == piece and self.board[r+3][c] == piece:
                    return True

        # Check positively sloped diagonals
        for c in range(self.COLUMN_COUNT - 3):
            for r in range(self.ROW_COUNT - 3):
                if self.board[r][c] == piece and self.board[r+1][c+1] == piece and \
                   self.board[r+2][c+2] == piece and self.board[r+3][c+3] == piece:
                    return True

        # Check negatively sloped diagonals
        for c in range(self.COLUMN_COUNT - 3):
            for r in range(3, self.ROW_COUNT):
                if self.board[r][c] == piece and self.board[r-1][c+1] == piece and \
                   self.board[r-2][c+2] == piece and self.board[r-3][c+3] == piece:
                    return True

    def evaluate_window(self, window, piece):
        score = 0
        opp_piece = 1 if piece == 2 else 2

        if window.count(piece) == 4:
            score += 100
        elif window.count(piece) == 3 and window.count(0) == 1:
            score += 5
        elif window.count(piece) == 2 and window.count(0) == 2:
            score += 2

        if window.count(opp_piece) == 3 and window.count(0) == 1:
            score -= 4

        return score

    def score_position(self, piece):
        score = 0

        # Score center column
        center_array = [int(i) for i in list(self.board[:, self.COLUMN_COUNT//2])]
        center_count = center_array.count(piece)
        score += center_count * 3

        # Score Horizontal
        for r in range(self.ROW_COUNT):
            row_array = [int(i) for i in list(self.board[r,:])]
            for c in range(self.COLUMN_COUNT-3):
                window = row_array[c:c+4]
                score += self.evaluate_window(window, piece)

        # Score Vertical
        for c in range(self.COLUMN_COUNT):
            col_array = [int(i) for i in list(self.board[:,c])]
            for r in range(self.ROW_COUNT-3):
                window = col_array[r:r+4]
                score += self.evaluate_window(window, piece)

        # Score positive sloped diagonal
        for r in range(self.ROW_COUNT-3):
            for c in range(self.COLUMN_COUNT-3):
                window = [self.board[r+i][c+i] for i in range(4)]
                score += self.evaluate_window(window, piece)

        # Score negative sloped diagonal
        for r in range(self.ROW_COUNT-3):
            for c in range(self.COLUMN_COUNT-3):
                window = [self.board[r+3-i][c+i] for i in range(4)]
                score += self.evaluate_window(window, piece)

        return score

    def is_terminal_node(self):
        return self.winning_move(1) or self.winning_move(2) or len(self.get_valid_locations()) == 0

    def minimax(self, depth, alpha, beta, maximizingPlayer):
        valid_locations = self.get_valid_locations()
        is_terminal = self.is_terminal_node()
        if depth == 0 or is_terminal:
            if is_terminal:
                if self.winning_move(2):
                    return (None, 100000000000000)
                elif self.winning_move(1):
                    return (None, -10000000000000)
                else:  # Game is over, no more valid moves
                    return (None, 0)
            else:  # Depth is zero
                return (None, self.score_position(2))
        if maximizingPlayer:
            value = -math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = self.get_next_open_row(col)
                b_copy = self.board.copy()
                self.drop_piece(row, col, 2)
                new_score = self.minimax(depth-1, alpha, beta, False)[1]
                self.board = b_copy
                if new_score > value:
                    value = new_score
                    column = col
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return column, value

        else:  # Minimizing player
            value = math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = self.get_next_open_row(col)
                b_copy = self.board.copy()
                self.drop_piece(row, col, 1)
                new_score = self.minimax(depth-1, alpha, beta, True)[1]
                self.board = b_copy
                if new_score < value:
                    value = new_score
                    column = col
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return column, value

    def get_valid_locations(self):
        valid_locations = []
        for col in range(self.COLUMN_COUNT):
            if self.is_valid_location(col):
                valid_locations.append(col)
        return valid_locations

    def pick_best_move(self, piece):
        valid_locations = self.get_valid_locations()
        best_score = -10000
        best_col = random.choice(valid_locations)
        for col in valid_locations:
            row = self.get_next_open_row(col)
            temp_board = self.board.copy()
            self.drop_piece(row, col, piece)
            score = self.score_position(piece)
            self.board = temp_board
            if score > best_score:
                best_score = score
                best_col = col

        return best_col

class GameGUI:
    def __init__(self, game, game_mode):
        self.game = game
        self.game_mode = game_mode
        self.SQUARESIZE = 100
        self.width = game.COLUMN_COUNT * self.SQUARESIZE
        self.height = (game.ROW_COUNT + 1) * self.SQUARESIZE
        self.size = (self.width, self.height)
        self.RADIUS = int(self.SQUARESIZE / 2 - 5)

        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.font = pygame.font.SysFont("monospace", 75)

    def draw_board(self):
        for c in range(self.game.COLUMN_COUNT):
            for r in range(self.game.ROW_COUNT):
                pygame.draw.rect(self.screen, Colors.BLUE, (c*self.SQUARESIZE, r*self.SQUARESIZE+self.SQUARESIZE, self.SQUARESIZE, self.SQUARESIZE))
                pygame.draw.circle(self.screen, Colors.BLACK, (int(c*self.SQUARESIZE+self.SQUARESIZE/2), int(r*self.SQUARESIZE+self.SQUARESIZE+self.SQUARESIZE/2)), self.RADIUS)
        
        for c in range(self.game.COLUMN_COUNT):
            for r in range(self.game.ROW_COUNT):        
                if self.game.board[r][c] == 1:
                    pygame.draw.circle(self.screen, Colors.RED, (int(c*self.SQUARESIZE+self.SQUARESIZE/2), self.height-int(r*self.SQUARESIZE+self.SQUARESIZE/2)), self.RADIUS)
                elif self.game.board[r][c] == 2: 
                    pygame.draw.circle(self.screen, Colors.YELLOW, (int(c*self.SQUARESIZE+self.SQUARESIZE/2), self.height-int(r*self.SQUARESIZE+self.SQUARESIZE/2)), self.RADIUS)
        pygame.display.update()

    def run_game(self):
        self.draw_board()
        pygame.display.update()

        while not self.game.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(self.screen, Colors.BLACK, (0, 0, self.width, self.SQUARESIZE))
                    posx = event.pos[0]
                    color = Colors.RED if self.game.turn == 0 else Colors.YELLOW
                    pygame.draw.circle(self.screen, color, (posx, int(self.SQUARESIZE/2)), self.RADIUS)
                    pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(self.screen, Colors.BLACK, (0, 0, self.width, self.SQUARESIZE))
                    posx = event.pos[0]
                    col = int(math.floor(posx / self.SQUARESIZE))

                    if self.game.is_valid_location(col):
                        row = self.game.get_next_open_row(col)
                        self.game.drop_piece(row, col, self.game.turn + 1)

                        if self.game.winning_move(self.game.turn + 1):
                            label = self.font.render(f"Player {self.game.turn + 1} wins!!", 1, Colors.RED if self.game.turn == 0 else Colors.YELLOW)
                            self.screen.blit(label, (40, 10))
                            self.game.game_over = True

                        self.game.print_board()
                        self.draw_board()

                        self.game.turn = (self.game.turn + 1) % 2

            # AI move
            if self.game_mode == 'AI' and self.game.turn == 1 and not self.game.game_over:
                col, minimax_score = self.game.minimax(5, -math.inf, math.inf, True)

                if self.game.is_valid_location(col):
                    row = self.game.get_next_open_row(col)
                    self.game.drop_piece(row, col, 2)

                    if self.game.winning_move(2):
                        label = self.font.render("AI wins!!", 1, Colors.YELLOW)
                        self.screen.blit(label, (40, 10))
                        self.game.game_over = True

                    self.game.print_board()
                    self.draw_board()

                    self.game.turn = (self.game.turn + 1) % 2

            if self.game.game_over:
                pygame.time.wait(3000)

def choose_game_mode():
    print("Choose game mode:")
    print("1. Player vs Player")
    print("2. Player vs AI")
    choice = input("Enter your choice (1 or 2): ")
    return 'PVP' if choice == '1' else 'AI'

if __name__ == "__main__":
    game_mode = choose_game_mode()
    game = ConnectFour()
    gui = GameGUI(game, game_mode)
    gui.run_game()