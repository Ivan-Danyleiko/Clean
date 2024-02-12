# import time
#
#
# # noinspection PyTypeChecker
# def factorize(*numbers: object):
#     result = []
#     num: object
#     for num in numbers:
#         divisors = []
#         for i in range(1, num + 1):
#             if num % i == 0:
#                 divisors.append(i)
#         result.append(divisors)
#     return result
#
#
# if __name__ == "__main__":
#     start_time = time.time()
#     a, b, c, d = factorize(128, 255, 99999, 10651060)
#
#     assert a == [1, 2, 4, 8, 16, 32, 64, 128]
#     assert b == [1, 3, 5, 15, 17, 51, 85, 255]
#     assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
#     assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
#                  1521580, 2130212, 2662765, 5325530, 10651060]
#     end_time = time.time()
#     execution_time = end_time - start_time
#
#     print("a:", a)
#     print("b:", b)
#     print("c:", c)
#     print("d:", d)
#     print(f"Total execution time: {execution_time:.2f} seconds")

from multiprocessing import Pool, cpu_count
import time


def factorize(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


if __name__ == "__main__":
    numbers = [128, 255, 99999, 10651060]
    start_time = time.time()

    with Pool(cpu_count()) as pool:
        results = pool.starmap(factorize, [(num,) for num in numbers])

    a, b, c, d = results

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]

    end_time = time.time()
    execution_time = end_time - start_time

    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)
    print(f"Загальний час виконання: {execution_time:.2f} секунд")
