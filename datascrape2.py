
def main():
    '''
    Datascrape2 also scrapes empty lines, whereas datascrape does not.
    '''
    while True:
        print("paste in the data and hit enter twice")
        while True:
            line = input()
            with open('data.txt', mode='a+') as my_file:
                my_file.seek(0)
                data = my_file.read(100)
                if len(data) > 0:
                    my_file.write("\n")
                my_file.write(line)


if __name__ == '__main__':
    main()
