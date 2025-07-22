def main(s):
    """
    A str of several words is given. All letters are lowercase. Make sure that the first letter of each word is capitalized.
    Args:
        s: str
    Returns:
        str: answer
    """
    
    return ' '.join(word.capitalize() for word in s.split())
print("hello WORLD".capitalize())
