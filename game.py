def display_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner(board, player):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for combination in winning_combinations:
        if all(board[index] == player for index in combination):
            return True

    return False


def check_draw(board):
    return all(position in ("X", "O") for position in board)


def play_game():
    board = ["1", "2", "3",
             "4", "5", "6",
             "7", "8", "9"]

    current_player = "X"

    while True:

        display_board(board)

        choice = input(
            f"Player {current_player}, choose a position (1-9): "
        )

        if not choice.isdigit():
            print("Please enter a number between 1 and 9.")
            continue

        position = int(choice)

        if position < 1 or position > 9:
            print("Please choose a number between 1 and 9.")
            continue

        index = position - 1

        if board[index] in ("X", "O"):
            print("That position is already occupied.")
            continue

        board[index] = current_player

        if check_winner(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break

        if check_draw(board):
            display_board(board)
            print("It's a draw!")
            break

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


def main():
    print("================================")
    print("       TIC-TAC-TOE GAME")
    print("================================")

    while True:

        play_game()

        replay = input("\nDo you want to play again? (y/n): ")

        if replay.lower() != "y":
            print("\nThanks for playing!")
            break


if __name__ == "__main__":
    main()