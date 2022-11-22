import random


def gen_random_int_seq(min_value, max_value, size):
    count = 0
    return [random.randint(min_value, max_value) for _ in range(size)]


def main():
    return gen_random_int_deq(1, 100, 20)


if __name__ == '__main__':
    print(main())

