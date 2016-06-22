# PythonSlicing

This is just a test I made to see how fast Python can be with reorganizing lists.
The tests with an i5-4210U with 1.70GHz have been done with 10 iterations each
and taking the mean of the timings which gave the following results:

Approach    | 936 elements  | 9360 elements |93600 elements |936000 elements|9360000 elements|
------------|---------------|---------------|---------------|---------------|----------------|
0           |  0.0003024s    |  0.0032743s    |  0.0403004s    |  0.4586692s    |  4.7831763s     |
1           |  5.1e-06s      |  3.84e-05s     |  0.0012238s    |  0.0305315s    |  0.3939106s     |
2           |  3.9e-05s      |  0.0003406s    |  0.0061472s    |  0.0978767s    |  1.1627915s     |
3           |  6.51e-05s     |  0.0006287s    |  0.0124055s    |  0.3004503s    |  3.772804s      |
4           |  0.0007357s    |  0.0082182s    |  0.0983107s    |  1.1418245s    |  11.8952948s    |
5           |  4.17e-05s     |  0.0003713s    |  0.0067311s    |  0.1034153s    |  1.2939473s     |
6           |  0.0008867s    |  0.0098987s    |  0.1247778s    |  2.0547471s    |  23.6235469s    |