# BEGIN: qv3z9z7z8v5p
class TextCleaner:
    def clean_text(self, filepath):
        with open(filepath, 'r') as file:
            text = file.read()
            cleaned_text = ''.join(c for c in text if c.isalnum() or c.isspace())
            return cleaned_text.lower()
    
    def split_text(self, cleaned_text):
        split_text = cleaned_text.split('\n\n')
        return split_text
    
    def divide_text(self, split_text):
        divided_text = []
        for item in split_text:
            divided_text.append(item.split())
        return divided_text
    
    def create_word_freq_dict(self, split_text):
        word_freq = []
        for sublist in split_text:
            freq_dict = {}
            for word in sublist:
                if word in freq_dict:
                    freq_dict[word] += 1
                else:
                    freq_dict[word] = 1
            word_freq.append(freq_dict)
        return word_freq
    
    def print_all(self, filepath):
        cleaned_text = self.clean_text(filepath)
        split_text = self.split_text(cleaned_text)
        divided_text = self.divide_text(split_text)
        word_freq = self.create_word_freq_dict(divided_text)
        for i in range(len(split_text)):
            print(f"split_text index {i}")
            print(split_text[i])
            print(f"divide_text index {i}")
            print(divided_text[i])
            print(f"create_word_freq_dict index {i}")
            print(word_freq[i])
            print("\n\n")
    
    def write_to_file(self, filepath):
        with open('output.txt', 'w') as file:
            cleaned_text = self.clean_text(filepath)
            split_text = self.split_text(cleaned_text)
            divided_text = self.divide_text(split_text)
            word_freq = self.create_word_freq_dict(divided_text)
            for i in range(len(split_text)):
                file.write(f"split_text index {i}\n")
                file.write(f"{split_text[i]}\n")
                file.write(f"divide_text index {i}\n")
                file.write(f"{divided_text[i]}\n")
                file.write(f"create_word_freq_dict index {i}\n")
                file.write(f"{word_freq[i]}\n\n")
                
cleaner = TextCleaner()
cleaner.write_to_file("eksempeltekst.txt")

# cleaner = TextCleaner()
# cleaned_text = cleaner.clean_text('eksempeltekst.txt')
# print(cleaned_text)
# print("\n\n")

# split_text = cleaner.split_text(cleaned_text)
# print(split_text)
# print("\n\n")

# divided_text = cleaner.divide_text(split_text)
# print(divided_text)
# print("\n\n")

# word_freq = cleaner.create_word_freq_dict(divided_text)
# print(word_freq)
# print("\n\n")

# print_text = cleaner.print_all("eksempeltekst.txt")


