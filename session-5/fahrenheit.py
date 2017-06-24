#!/usr/bin/env python3

def to_celsius(degF):
    degC = 5/9*(degF - 32)
    return degC

def main():
    print(to_celsius(32))

if __name__ == '__main__':
    main()

