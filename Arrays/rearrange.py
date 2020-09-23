"""
Page 48.
(5.8) Write a program that takes an array A of n numbers,
     and rearranges A's elements to get a new array B
     having the property that:
     B[0]<=B[1]>=B[2]<=B[3]>=B[4]<=B[5]>=....

"""
def rearrange(A):
    for i in range(len(A)):
       A[i: i + 2] = sorted(A[i:i + 2], reverse=i % 2)
    return A
def rearrange2(A):
    i = 1
    A.sort()
    while i < len(A) - 1:
        A[i], A[i+1] = A[i+1], A[i]
        i += 2
    return A
if __name__ == "__main__":
    A = [4, 3, 2, 1, 5, 7]
    print(rearrange(A))
    B = [4, 3, 2, 1, 5, 7]
    print(rearrange2(B))