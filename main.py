import json


class MorseEncoder:
    """
    Encode a text input to morse code with the format ('/' as space )\n
    encode_text() -> returns Morse code
    """

    def __init__(self):
        self.encoded_text = ''
        with open(file="morse-code.json", mode='r') as data:
            self.code = json.load(data)

    def encode_text(self):
        """
        Receives a text input
        :return: Morse code
        """
        word = input("Enter a text to convert: ").lower()
        for letter in word:
            if letter in self.code:
                self.encoded_text += self.code[letter]

        return self.encoded_text


encode = MorseEncoder()
print(encode.encode_text())
