def anti_vowel(text):
  vowels="aeiouAEIOIU"
  string=""
  for char in text:
    if char not in vowels:
      string += char
  return string