if __name__ == '__main__':
    N = int(input())
    students = []
    names = []

    for n in range(N):
        student = []
        name = input()
        score = float(input())

        student.append(name)
        student.append(score)
        students.append(student)

    marks = []
    for i in students:

        marks.append(i[1])

    lowest_mark = min(marks)

    while lowest_mark in marks:
        marks.remove(lowest_mark)



    for k in students:
        if k[1] == min(marks):
            names.append(k[0])
    names.sort()

    for name in names:
        print(name)



