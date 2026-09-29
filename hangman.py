import random
import os

class HangmanGame:
    def __init__(self):
        self.word_list = [
            'python', 'javascript', 'hangman', 'programlama', 'bilgisayar',
            'oyun', 'kelime', 'tahmin', 'müzik', 'kitap', 'kütüphane',
            'internet', 'yazılım', 'donanım', 'ağ', 'veri', 'kod', 'sistem'
        ]
        self.word = random.choice(self.word_list).upper()
        self.guessed_letters = set()
        self.correct_letters = set()
        self.attempts_left = 6
        self.game_over = False
        self.won = False

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_hangman(self):
        stages = [
            '''
               ------
               |    |
               |
               |
               |
               |
               ---------
            ''',
            '''
               ------
               |    |
               |    O
               |
               |
               |
               ---------
            ''',
            '''
               ------
               |    |
               |    O
               |    |
               |
               |
               ---------
            ''',
            '''
               ------
               |    |
               |    O
               |   \\|
               |
               |
               ---------
            ''',
            '''
               ------
               |    |
               |    O
               |   \\|/
               |
               |
               ---------
            ''',
            '''
               ------
               |    |
               |    O
               |   \\|/
               |    |
               |
               ---------
            ''',
            '''
               ------
               |    |
               |    O
               |   \\|/
               |    |
               |   / \\
               ---------
            '''
        ]
        return stages[6 - self.attempts_left]

    def display_word(self):
        display = ''
        for letter in self.word:
            if letter in self.correct_letters:
                display += letter + ' '
            else:
                display += '_ '
        return display

    def display_game_state(self):
        self.clear_screen()
        print("=" * 40)
        print("       ADAM ASMACA OYUNU")
        print("=" * 40)
        print(self.display_hangman())
        print("\nKelime: ", self.display_word())
        print("\nKalan Hak: ", self.attempts_left)
        print("Tahmin Edilen Harfler: ", ', '.join(sorted(self.guessed_letters)) if self.guessed_letters else "Henüz yok")
        print("-" * 40)

    def make_guess(self):
        while True:
            guess = input("Bir harf tahmin et (veya 'çık' yazarak oyundan çık): ").upper()
            
            if guess.lower() == 'çık':
                return None
            
            if len(guess) != 1 or not guess.isalpha():
                print("❌ Lütfen tek bir harf gir!")
                continue
            
            if guess in self.guessed_letters:
                print(f"⚠️  '{guess}' harfini zaten tahmin etmişsin!")
                continue
            
            return guess

    def process_guess(self, guess):
        self.guessed_letters.add(guess)
        
        if guess in self.word:
            self.correct_letters.add(guess)
            print(f"✅ Doğru! '{guess}' kelimede var!")
        else:
            self.attempts_left -= 1
            print(f"❌ Yanlış! '{guess}' kelimede yok!")
        
        input("Devam etmek için Enter'a bas...")

    def check_win(self):
        return all(letter in self.correct_letters for letter in self.word)

    def check_lose(self):
        return self.attempts_left <= 0

    def display_end_game(self):
        self.clear_screen()
        print("=" * 40)
        
        if self.won:
            print("🎉 KAZANDIN! 🎉")
            print(f"Kelime: {self.word}")
        else:
            print("💀 KAYBETTIN! 💀")
            print(f"Kelime: {self.word}")
        
        print("=" * 40)

    def play(self):
        while not self.game_over:
            self.display_game_state()
            
            guess = self.make_guess()
            
            if guess is None:
                print("\n👋 Oyundan çıktın. Görüşmek üzere!")
                return
            
            self.process_guess(guess)
            
            if self.check_win():
                self.won = True
                self.game_over = True
            elif self.check_lose():
                self.game_over = True
        
        self.display_end_game()


def main():
    while True:
        game = HangmanGame()
        game.play()
        
        play_again = input("\nYeniden oynamak ister misin? (e/h): ").lower()
        if play_again != 'e':
            print("Oynadığın için teşekkürler! 👋")
            break


if __name__ == "__main__":
    main()
