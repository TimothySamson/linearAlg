import time

def main(string, depth):
    print("-" * depth + " " + str(depth) + " " + string)
    if depth == 6:
        return 
    
    depth += 1
    if string[-1] == 'i':
        main(string + "u", depth)

    for i in range(len(string)):
        if string[i: i+3] == "iii":
            main(string[0:i] + "u" + string[i+3:len(string)], depth)

    for i in range(len(string)):
        if string[i: i+2] == "uu":
            main(string[0:i] + string[i+2:len(string)], depth)

    if string[0] == "m":
        main(string[0] + string[1:]*2, depth)

if __name__ == "__main__":
    main("mi", 0)


