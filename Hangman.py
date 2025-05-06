class Hangman:
    def __init__(self,phrase):
        self.phrase = phrase
        self.guessed = []
        self.wrong_guesses = []
        self.placeholder = ''.join(["_" if i.isalpha() else i for i in self.phrase])
        self.counter = len(self.wrong_guesses)
    def check_guess(self,guess:str):
        guess = guess.lower()
        if len(guess) == 1 or len(guess) == len(self.phrase):
            if len(guess) == 1 and guess.upper() not in self.guessed:
                self.guessed.append(guess.upper())
                if guess in self.phrase.lower():
                    return True
                else:
                    self.wrong_guesses.append(guess.upper())
                    return False
            elif guess.lower() == self.phrase.lower() or self.placeholder.count("_") == 0:
                return "Solved".upper()
            elif guess.upper() in self.guessed:
                return "Guessed".upper()
        elif len(guess) > 1 and len(guess) != len(self.phrase):
            return "Too Many Letters".upper()
    def place_guess(self,guess:str):
        index = [i for i in range(len(self.phrase)) if self.phrase[i].lower() == guess.lower()]
        self.placeholder = "".join([self.phrase[i] if i in index else self.placeholder[i] for i in range(len(self.placeholder))])



