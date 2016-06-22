# PythonSlicing

This is just a test I made to see how fast Python can be with reorganizing lists.
The tests with an Intel i5-4210U with 1.70GHz and 2 cores have been done with 10 iterations each
and taking the mean of the timings which gave the following results:

Approach    | 936 elements  | 9360 elements |93600 elements |936000 elements|9360000 elements|
------------|---------------|---------------|---------------|---------------|----------------|
0           |  0.0003024 s    |  0.0032743 s    |  0.0403004 s    |  0.4586692 s    |  4.7831763 s     |
1           |  5.1e-06 s      |  3.84e-05 s     |  0.0012238 s    |  0.0305315 s    |  0.3939106 s     |
2           |  3.9e-05 s      |  0.0003406 s    |  0.0061472 s    |  0.0978767 s    |  1.1627915 s     |
3           |  6.51e-05 s     |  0.0006287 s    |  0.0124055 s    |  0.3004503 s    |  3.772804 s      |
4           |  0.0007357 s    |  0.0082182 s    |  0.0983107 s    |  1.1418245 s    |  11.8952948 s    |
5           |  4.17e-05 s     |  0.0003713 s    |  0.0067311 s    |  0.1034153 s    |  1.2939473 s     |
6           |  0.0008867 s    |  0.0098987 s    |  0.1247778 s    |  2.0547471 s    |  23.6235469 s    |

Here are the results using an AMD Opteron 6272 with 2.10GHz and 16 cores (via [Mogon](www.hpc.uni-mainz.de)):

Approach    | 936 element s  | 9360 element s |93600 element s |936000 element s|9360000 element s|
------------|---------------|---------------|---------------|---------------|----------------|
0           |   0.0 s    |  0.013 s    |  0.117 s    |  1.168 s    |  11.951 s     |
1           |   0.0 s      |  0.0 s     |  0.001 s    |  0.022 s    |  0.251 s     |
2           |   0.0 s      |  0.002 s    |  0.014 s    |  0.149 s    |  1.583 s     |
3           |   0.0 s     |  0.003 s    |  0.03 s    |  0.584 s    |  6.61 s      |
4           |  0.003 s    |  0.028 s    |  0.253 s    |  2.523 s    |  27.305 s    |
5           |  0.001 s     |  0.002 s    |  0.017 s    |  0.172 s    |  1.812 s     |
6           |  0.004 s    |  0.032 s    |  0.308 s    |  3.992 s    |  41.8399 s    |
