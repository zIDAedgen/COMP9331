
def flip_data(string):
    s = chr(ord(string[-1]) ^ 1)
    return string[:-1] + s
def checkMD5():
    print('Receiver = 1')



if __name__ == '__main__':
    print(flip_data('adhkad'))