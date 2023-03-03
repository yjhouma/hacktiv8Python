def factorials(n):
    return 1 if n <= 1 else n * factorials(n-1)


def penjumlahan(x,y,z):
    return x**2 + y*z


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        print(penjumlahan(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])))
    # print(sys.argv)