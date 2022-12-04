def inplace_replace(file, old, new):
    with open(file, 'r') as f:
        newText=f.read().replace(old, new)

    with open(file, "w") as f:
        f.write(newText)

if __name__ == '__main__':
    pass