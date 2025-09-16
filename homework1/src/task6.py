def CountWords(filePath):
    with open(filePath, 'r') as f:
        text = f.read()
    return len(text.split())
