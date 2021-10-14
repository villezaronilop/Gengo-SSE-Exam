class Palindrome():

    def __init__(self, text=None):
        self.sample_input = text
        self.collection = []
        if self.sample_input:
            total_len = len(self.sample_input)
            collection = self.get_pair(end=total_len)
            self.collection = self.eliminate_non_palindrome(collection)
    
    def get_pair(self, start=0, end=0, collection=[]):
        for i in range(start, end):
            slice_text = self.sample_input[i:end]
            # tuple
            collection.append((slice_text, slice_text[::-1]))
        if end != 0:
            collection += self.get_pair(start=0, end=end-1, collection=collection)
        return collection

    def eliminate_non_palindrome(self, collection):
        return [n[0] for n in list(set(collection)) if n[0] == n[1]]

    # level 1
    def validate(self):
        if self.sample_input:
            reversed = self.sample_input[::-1]
            return reversed == self.sample_input
        return None

    # level 2
    def longest_string(self):
        if self.sample_input:
            return max(self.collection, key=len)
        return None

    def level_three(self):
        pass
    
    def get_result(self):
        print("Level One: ", self.validate())
        print("Level Two: ", self.longest_string())

if __name__ == '__main__':
    Palindrome(input("INPUT: ")).get_result()