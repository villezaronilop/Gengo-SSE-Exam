class Palindrome():

    def __init__(self, text=None):
        self.sample_input = text

    def level_one(self):
        if self.sample_input:
            reversed = self.sample_input[::-1]
            return reversed == self.sample_input
        return None

    def level_two(self):
        pass

    def level_three(self):
        pass
    
    def get_result(self):
        print("Level One: ", self.level_one())

if __name__ == '__main__':
    Palindrome(input("INPUT: ")).get_result()