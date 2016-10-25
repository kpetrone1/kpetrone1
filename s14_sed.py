def sed(pattern, replace, source, dest):
    """Reads a source file and writes the destination file.
    In each line, replaces pattern with replace.
    pattern: string
    replace: string
    source: string filename
    dest: string filename
    """
    file_in = open(source, 'r')
    file_out = open(dest, 'w')

    for line in file_in:
        new_line = line.replace(pattern, replace)
        # new_line = new_line.replace(pattern.lower(), replace)
        file_out.write(new_line)

    file_in.close()
    file_out.close()


def main():
    pattern = 'Hey Jude'
    replace = 'Hi Jerry'
    source = 's14_sed_tester.txt'
    dest = 'new_' + source
    sed(pattern, replace, source, dest)


if __name__ == '__main__':
    main()