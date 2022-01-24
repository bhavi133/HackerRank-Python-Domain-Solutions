Link : https://www.hackerrank.com/challenges/finding-the-percentage/problem 

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        avg = "%.2f" %(sum(scores) / len(scores))
        student_marks[name] = avg

    query_name = input()
    print(student_marks[query_name])
