def writefile(directory, content):
    with open(directory, 'w+') as fp:
        fp.write(str(content))