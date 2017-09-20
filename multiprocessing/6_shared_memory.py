import multiprocessing as mp

value = mp.Value('d', 1)
value = mp.Value('d', 3.14)
array = mp.Array('i', [1, 2, 3])



# https://docs.python.org/3/library/array.html
