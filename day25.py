# my solution

card_pk = 1965712
door_pk = 19072108

def loop_size(public_key):
    result = 1
    loops = 0

    while result != public_key:
        result = result * 7
        result %= 20201227
        loops +=1
    #print(f"number of loops is {loops}")
    return loops


def encryption_key(public_key, loops):
    value = 0
    result = 1
    while value != loops:
        result = result * public_key
        result %= 20201227
        value += 1
    return result


def main():
    print(encryption_key(public_key=door_pk, loops=loop_size(card_pk)))


if __name__ == "__main__":
    main()
