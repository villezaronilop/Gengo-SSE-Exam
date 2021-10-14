class Palindrome():

    def __init__(self, text=None):
        self.sample_input = text
        self.collection = []
        if self.sample_input:
            collection = self.get_pair(end=len(self.sample_input))
            self.collection = self.eliminate_non_palindrome(collection)
    
    def get_pair(self, start=0, end=0, collection=[]):
        for i in range(start, end):
            slice_text = self.sample_input[i:end]
            # tuple
            collection.append((slice_text, slice_text[::-1]))
        if end != 0:
            collection += self.get_pair(end=end-1, collection=collection)
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

    # level 3
    def count_cuts(self):
        if self.sample_input:
            self.collection = sorted(self.collection, key=len, reverse=True)
            sample_input = self.sample_input
            count = 0
            deducted = []
            for n in self.collection:
                if n in sample_input:
                    count += 1
                    deducted.append(n)
                    sample_input = sample_input.replace(n, "")

            return f"{count-1} // {' | '.join(deducted)}"
        return None

    def get_result(self):
        print("Level 1: ", self.validate())
        print("Level 2: ", self.longest_string())
        print("Level 3: ", self.count_cuts())

if __name__ == '__main__':
    Palindrome(input("INPUT: ")).get_result()