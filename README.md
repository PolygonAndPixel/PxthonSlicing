# PythonSlicing

This is just a test I made to see how fast Python can be with reorganizing lists.
The tests with an i5-4210U with 1.70GHz have been done with 10 iterations each
and taking the mean of the timings which gave the following results:


Approach    |   Seconds     |
------------|---------------|
0           |   0.0003024   |
1           |  5.1e-06      |
2           |  3.9e-05      |
3           |  6.51e-05     |
4           |  0.0007357    |
5           |  4.17e-05     |
6           |  0.0008867    |
[936 elements]

Approach    |   Seconds     |
------------|---------------|
0           |  0.0032743    |
1           |  3.84e-05     |
2           |  0.0003406    |
3           |  0.0006287    |
4           |  0.0082182    |
5           |  0.0003713    |
6           |  0.0098987    |
[9360 elements]

Approach    |   Seconds     |
------------|---------------|
0           |  0.0403004    |
1           |  0.0012238    |
2           |  0.0061472    |
3           |  0.0124055    |
4           |  0.0983107    |
5           |  0.0067311    |
6           |  0.1247778    |
[93600 elements]

Approach    |   Seconds     |
------------|---------------|
0           |  0.4586692    |
1           |  0.0305315    |
2           |  0.0978767    |
3           |  0.3004503    |
4           |  1.1418245    |
5           |  0.1034153    |
6           |  2.0547471    |
[936000 elements]

Approach    |   Seconds     |
------------|---------------|
0           |  4.7831763    |
1           |  0.3939106    |
2           |  1.1627915    |
3           |  3.772804     |
4           |  11.8952948   |
5           |  1.2939473    |
6           |  23.6235469   |
[9360000 elements]