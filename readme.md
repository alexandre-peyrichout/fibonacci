Cas 2 :
The Fibonacci sequence is defined using the following recursive formula:

F(0) = 0 F(1) = 1 F(N) = F(N−1) + F(N−2) if N ≥ 2

Write a function that, given a non-negative integer N, returns the six least significant decimal digits of number F(N).

For example, given N = 8, the function should return 21, because the six least significant decimal digits of F(8) are 000021 (the complete decimal representation of F(8) is 21). Similarly, given N = 36, the function should return 930352, because the six least significant decimal digits of F(36) are 930352 (the complete decimal representation of F(36) is 14930352).

Assume that:

N is an integer within the range [0..2,147,483,647].
