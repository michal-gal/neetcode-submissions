class TextProcessor:
    # Implement method overloading for format_text method
    def format_text(self, word1:str, word2: str = ""):
        if word2 == '':
            return word1.upper()
        else:
            return word1+word2



# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
