import pandas as pd

data = pd.read_csv("nato_alphabet_data.csv")

nato_dict = {row.letter : row.code for (index, row) in data.iterrows()}
print(nato_dict)

word = input("Enter a word: ").upper()
output_list = [nato_dict[letter] for letter in word]
print(output_list)
