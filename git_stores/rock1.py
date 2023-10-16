import sys
import random
import hashlib

class Move:
    def __init__(self, name):
        self.name = name

class RuleBook:
    def __init__(self, moves):
        self.moves = moves
        self.rules = self.generate_rules()

    def generate_rules(self):
        n = len(self.moves)
        rules = {}
        for i, move in enumerate(self.moves):
            next_moves = self.moves[i + 1:] + self.moves[:i]
            half = n // 2
            rules[move] = next_moves[:half], next_moves[half:]
        return rules

class Helper:
    @staticmethod
    def display_help(rules, moves):
        # Create headers with emphasis
        header = ' '
        
        print(header)
        print(f'|{"v PC User >":^12}|', end='')

        for move in moves:
            print(f' {move:^8} |', end='')
        print(header)

        # Create and display the table
        for move in moves:
            print(f'| {move:^10} |', end='')
            for opponent in moves:
                result = 'Win' if opponent in rules[move][0] else 'Lose' if opponent in rules[move][1] else 'Draw'
                print(f' {result:^8} |', end='')
            print(header)

        # Add explanation
        print("Results are from the user's point of view.")
        print("Example: If you choose 'Rock' and the computer chooses 'Paper', you Lose.")

class Game:
    def __init__(self, moves):
        self.moves = [Move(move) for move in moves]
        self.rulebook = RuleBook([move.name for move in self.moves])
        self.key = self.generate_crypto_key()

    def generate_crypto_key(self):
        key = ''.join(random.choice('0123456789ABCDEF') for _ in range(64))
        return key

    def calculate_hmac(self, message):
        key = bytes.fromhex(self.key)
        message_bytes = message.encode('utf-8')
        hmac = hashlib.sha256(key + message_bytes).hexdigest()
        return hmac

    def display_help_menu(self):
        print("\nMenu:")
        for i, move in enumerate(self.moves, start=1):
            print(f"{i} - {move.name}")
        print("h - Help")
        print("0 - Exit")

    def start_game(self):
        print(f"Generated Key: {self.key}")
        while True:
            self.display_help_menu()
            choice = input("Make your choice: ")

            if choice == '0':
                break
            elif choice.lower() == 'h':
                Helper.display_help(self.rulebook.rules, [move.name for move in self.moves])
                continue

            try:
                choice = int(choice)
                if 1 <= choice <= len(self.moves):
                    user_move = self.moves[choice - 1]
                    computer_move = random.choice(self.moves)
                    hmac = self.calculate_hmac(user_move.name)

                    print(f"Your move: {user_move.name}")
                    print(f"Computer's move: {computer_move.name}")
                    print(f"Original Key: {self.key}")

                    if computer_move.name in self.rulebook.rules[user_move.name][1]:
                        print("You Win!")
                    elif computer_move.name in self.rulebook.rules[user_move.name][0]:
                        print("Computer Wins!")
                    else:
                        print("It's a Draw!")
                    print(f"HMAC: {hmac}")
                else:
                    print("Invalid choice. Please choose a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")
            except KeyboardInterrupt:
                print("\nGame aborted.")

if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) < 3 or len(args) % 2 == 0 or len(set(args)) != len(args):
        print("Usage: python rock_paper_scissors.py move1 move2 move3 ...")
        print("Please provide an odd number of non-repeating moves.")
    else:
        game = Game(args)
        game.start_game()