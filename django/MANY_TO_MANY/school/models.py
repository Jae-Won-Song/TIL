from django.db import models

class Lecture(models.Model):
    title = models.CharField(max_length=100)
    room = models.CharField(max_length=100)   

    def __str__(self):
        return f'#{self.pk}:{self.title}'



class Student(models.Model):
    name = models.CharField(max_length=30)
    major = models.CharField(max_length=30)
    lectures = models.ManyToManyField(
        Lecture,                                # m:n 관계의 상대 모델
        related_name='students',                # 상대모델(Lecture)이 나(Student)를 부를때 이름
        through='school.Enrollment',            # 커스텀 중개모델 이름(str)   
        through_fields=('student','lecture')   # M:N을 맺는 FK들 명시
    )
    def __str__(self):
        return f'#{self.pk}:{self.name}'


# join Table에 추가 데이터가 있다면, 클래스 생성
class Enrollment(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2)
    semester = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.student} => {self.lecture}'



'''





    [field.name]
s1. lectures    .all()
    [related name]
l1. students    .all()

sl.lectures.add(l1) => 자동으로 Enrollment의 객체가 생성이됨.(권장x)
e1 = Enrollment.objects.get(student=s1, lecture=l1) => 방금 생성된 Enrollment 객체조회(pk조회가 아닌 fk조회)
e1.student == s1
e1.lecture == l1

# 자동 생성 시 비어있는 항목들
e1.grade == ''
e1.semester == ''
e1.gradet = 'B+'
e1.semester = '2023-1'
e1.save()

# 수강신청을 새로 생성
Enrollment.objects.create(student=s1, lecture=l2, grade = 'C+', semester = '2023-1')

# s1의 모든 수업
s1.lectures.all()

# l2의 모든 수강생
l2.students.all()

'''