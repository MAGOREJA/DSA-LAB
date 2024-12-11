# Create a HuffmanCodeBook
codebook = HuffmanCodeBook()

# Add sequences to the codebook
codebook.add_sequence('a', '0')
codebook.add_sequence('b', '10')
codebook.add_sequence('c', '11')

# Check if a character is in the codebook
print(codebook.contains('a'))  # Output: True
print(codebook.contains('d'))  # Output: False

# Get the binary sequence for a character
print(codebook.get_sequence('b'))  # Output: '10'

# Encode a string using the codebook
try:
    encoded_text = codebook.encode('abc')
    print(f"Encoded text: {encoded_text}")  # Output: '01011'
except ValueError as e:
    print(e)

# Check if all characters in a text are in the codebook
print(codebook.contains_all('abc'))  # Output: True
print(codebook.contains_all('abcd'))  # Output: False

# Get all characters in the codebook
print(codebook.characters())  # Output: ['a', 'b', 'c']
