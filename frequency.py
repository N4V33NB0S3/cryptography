import sys
from collections import Counter

def frequency_analysis(text, group_size):
    text = ''.join(filter(str.isalpha, text))  # Remove non-alphabetic characters
    
    groups = [text[i:i+group_size] for i in range(len(text) - group_size + 1)]
    frequency = Counter(groups)
    
    return dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))  # Sort by count

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 frequency.py <file> <group>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    try:
        group_size = int(sys.argv[2])
        if group_size < 1:
            raise ValueError
    except ValueError:
        print("Error: Group size must be a positive integer.")
        sys.exit(1)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    
    result = frequency_analysis(text, group_size)
    
    print("\nCharacter Frequency Analysis:")
    for group, count in result.items():
        print(f"{group}: {count}")
