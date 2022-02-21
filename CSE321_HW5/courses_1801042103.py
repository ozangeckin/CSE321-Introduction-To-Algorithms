def maximumCourseSelection(lesson, start, finish, n):
 
  A = [0]*n
  A[0] = lesson[0]
  k=0
  iter = 0

  for i in range(1, n):
    if start[i] >= finish[k]:
      iter = iter+1
      A[iter] = lesson[i]
      k=i    
  return A

if __name__ == '__main__':

  lesson = ['English', 'Mathematics', 'Physics', 'Chemistry', 'Biology', 'Geography']
  start = [1, 3, 0, 5, 8, 5]
  finish = [2, 4, 6, 7, 9, 9]
 
  p = maximumCourseSelection(lesson, start,finish, len(lesson))

  for i in range(len(p)):
      if p[i]!=0:
          print(p[i])