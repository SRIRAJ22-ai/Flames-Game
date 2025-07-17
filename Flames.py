# Input names
name1 = input("Enter first name: ").lower().replace(" ","")
name2 = input("Enter second name: ").lower().replace(" ","")

# Remove common characters
for char in name1:
    if char in name2:
        name1 = name1.replace(char,'', 1)
        name2 = name2.replace(char,'', 1)

# Count remaining letters
count = len(name1) + len(name2)

# FLAMES logic
flames = ['F','L','A','M','E','S']
while len(flames) > 1:
    split_index = (count % len(flames)) - 1
    if split_index >= 0:
        right = flames[split_index + 1:]
        left = flames[:split_index]
        flames = right + left
    else:
        flames = flames[:len(flames) - 1]

# Meaning of result
result_map = {
    'F': 'Friends',
    'L': 'Love',
    'A': 'Affection',
    'M': 'Marriage',
    'E': 'Enemy',
    'S': 'Siblings'
}
print("Relationship status:", result_map[flames[0]])