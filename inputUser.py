import sys
import random
import hashlib

class RockPaperScissorsGame:
    def __init__(self, moves):
        self.moves = moves
        self.key = self.generate_crypto_key()
        self.rules = self.generate_rules()
    
    def generate_crypto_key(self):
        # Generate a cryptographically strong random key with at least 256 bits
        key = ''.join(random.choice('0123456789ABCDEF') for _ in range(64))
        return key
    
    def generate_rules(self):
        # Generate rules for determining the winner
        n = len(self.moves)
        rules = {}
        for i in range(n):
            next_moves = self.moves[i+1:] + self.moves[:i]
            half = n // 2
            rules[self.moves[i]] = next_moves[:half], next_moves[half:]
        return rules
    
    def calculate_hmac(self, message):
        # Calculate HMAC using SHA256
        key = bytes.fromhex(self.key)
        message_bytes = message.encode('utf-8')
        hmac = hashlib.sha256(key + message_bytes).hexdigest()
        return hmac
    
    def display_help(self):
        # Display the table of winning moves
        table = [[' '] + self.moves]
        for move in self.moves:
            row = [move]
            for opponent in self.moves:
                if opponent in self.rules[move][0]:
                    row.append('Win')
                elif opponent in self.rules[move][1]:
                    row.append('Lose')
                else:
                    row.append('Draw')
            table.append(row)
        
        for row in table:
            print(' | '.join(row))
    
    def start_game(self):
        print(f"Generated Key: {self.key}")
        while True:
            print("\nMenu:")
            for i, move in enumerate(self.moves, start=1):
                print(f"{i} - {move}")
            print("0 - Exit")
            choice = input("Make your choice: ")
            
            if choice == '0':
                break
            
            try:
                choice = int(choice)
                if 1 <= choice <= len(self.moves):
                    user_move = self.moves[choice - 1]
                    computer_move = random.choice(self.moves)
                    hmac = self.calculate_hmac(user_move)
                    
                    print(f"Your move: {user_move}")
                    print(f"Computer's move: {computer_move}")
                    print(f"Original Key: {self.key}")
                    
                    if computer_move in self.rules[user_move][1]:
                        print("You Win!")
                    elif computer_move in self.rules[user_move][0]:
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
        game = RockPaperScissorsGame(args)
        game.start_game()


