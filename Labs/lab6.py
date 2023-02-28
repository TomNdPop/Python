def sort_word(word):
  word = word.strip()
  word = word.lower()
  word = sorted(word)
  word = str("".join(word))
  return word


with open("word_list.txt") as f:
  data = f.read()

word = input("Enter a word:")

lines = data.split("\n")
for line in lines:
  if sort_word(line) == sort_word(word):
    print(line)



