"""Write a program to input three numbers(A, B & C) from user and print the minimum element among A, B & C in each line.

Problem Constraints
1 <= A <= 1000000
1 <= B <= 1000000
1 <= C <= 1000000

Input Format
First line is a single integer A.
Second line is a single integer B.
Third line is a single integer C.

Output Format
One line containing an integer as per the question.

Example Input
Input 1:

5 
6 
7
Input 2:

1000 
10000 
100000

Example Output
Output 1:-
5
Output 2:-
1000

Example Explanation
Explanation 1:

Clearly, among 5, 6 and 7, 5 is minimum.
Explanation 2:

Clearly, among 1000, 10000 and 100000, 1000 is minimum."""


#Solution_1----------------------------------------------------------------------------------
def main():
    a=int(input())
    b=int(input())
    c=int(input())
    print(min(a,b,c))

    return 0

if __name__ == '__main__':
    main()

#Solution_2----------------------------------------------------------------------------------
def main():
    li = list(map(int,input().split()))
    a = li[0]
    b = li[1]
    c = li[2]
    if a <= b and a <= c :
        print(a)
    elif b <= a and b <= c :
        print(b)
    else :
        print(c)
    return 0

if __name__ == '__main__':
    main()
