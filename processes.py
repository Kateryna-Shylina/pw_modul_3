
import os
import time
import multiprocessing


def factorize(*number):
    result = []
    for num in number:
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        result.append(factors)
    return result

def multiprocessing_factorize(*number):
    with multiprocessing.Pool(os.cpu_count()) as p:
        result = p.map(factorize, number)

    return result


if __name__ == "__main__":
    start_time = time.time()
    factor  = factorize(128, 255, 99999, 10651060, 333, 89895, 23658912, 23232323)
    end_time = time.time()
    print(f"Sequential execution time: {end_time - start_time}")

    start_time_m = time.time()
    factor_m  = multiprocessing_factorize(128, 255, 99999, 10651060, 333, 89895, 23658912, 23232323)
    end_time_m = time.time()
    print(f"Multiprocessing execution time: {end_time_m - start_time_m}")

    print(factor)
    print(factor_m)

