class TextProcessor:
    # Implement method overloading for format_text method
    # def format_text(self, word1:str, word2: str = ""):
    #     if word2 == '':
    #         return word1.upper()
    #     else:
    #         return word1+word2

    def format_text(self,*args):
        if len(args) > 1:
            return args[0]+args[1]
        else:
            return args[0].upper()



# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
