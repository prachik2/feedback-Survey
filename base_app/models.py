from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    """Base model extended by other models through out the project.
        Here we define all the common fields used by all the models used in the project.
    """

    date_added = models.DateTimeField(db_index=True)
    date_updated = models.DateTimeField()

    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """Overriding the save methods to extend the logic."""

        if self.is_deleted is False:
            self.date_added = timezone.now()
            self.date_updated = timezone.now()

        super(BaseModel, self).save(*args, **kwargs)


class Student(BaseModel):
    student_id = models.CharField(max_length=128, unique=True, db_index=True)
    student_name = models.CharField(max_length=128)
    email = models.EmailField(unique=True)

    class Meta:
        db_table = 'students'
        ordering = ['date_added', '-student_id']

    def __str__(self):
        return "{} :{}".format(self.student_name, self.student_id)

    def save(self, *args, **kwargs):
        super(Student, self).save(*args, **kwargs)


class Course(BaseModel):
    course_id = models.CharField(max_length=128, unique=True, db_index=True)
    course_name = models.CharField(max_length=128)

    class Meta:
        db_table = 'course'
        ordering = ['date_added', '-course_id']

    def __str__(self):
        return "{} :{}".format(self.course_name, self.course_id)

    def save(self, *args, **kwargs):
        super(Course, self).save(*args, **kwargs)


class SemesterOffering(BaseModel):
    semester_offering_id = models.CharField(max_length=128, unique=True, db_index=True)
    semester_name = models.CharField(max_length=128)
    course = models.ForeignKey('Course', on_delete=models.PROTECT,null=True)
    start_date = models.DateField(db_index=True, null=True)
    end_date = models.DateField(db_index=True, null=True)

    class Meta:
        db_table = 'semester_offering'
        ordering = ['date_added', '-semester_offering_id']

    def __str__(self):
        return "{} :{}".format(self.course, self.semester_offering_id)

    def save(self, *args, **kwargs):
        super(SemesterOffering, self).save(*args, **kwargs)


class StudentCourseRegistration(BaseModel):
    student = models.ForeignKey('Student', on_delete=models.PROTECT,null=True)
    semester_offering = models.ForeignKey('SemesterOffering', on_delete=models.PROTECT, null=True)

    class Meta:
        db_table = 'student_course_registration'

    def __str__(self):
        return "{} :{}".format(self.student, self.semester_offering)

    def save(self, *args, **kwargs):
        super(StudentCourseRegistration, self).save(*args, **kwargs)


class Survey1(BaseModel):
    student_name = models.CharField(max_length=128)
    semester= models.ForeignKey('SemesterOffering', on_delete=models.PROTECT, null=True)
    vote = models.IntegerField(default=1)
    missed_class = models.CharField(max_length=128)

    class Meta:
        db_table = 'survey1'

    def __str__(self):
        return "{} :{}".format(self.student_name, self.semester)

    def save(self, *args, **kwargs):
        super(Survey1, self).save(*args, **kwargs)


class Survey2(BaseModel):
    student_name = models.CharField(max_length=128)
    semester= models.ForeignKey('SemesterOffering', on_delete=models.PROTECT, null=True)
    vote = models.IntegerField(default=1)
    expected_topic = models.CharField(max_length=128)
    is_class_off_time = models.BooleanField(default=False)

    class Meta:
        db_table = 'survey2'

    def __str__(self):
        return "{} :{}".format(self.student_name, self.semester)

    def save(self, *args, **kwargs):
        super(Survey2, self).save(*args, **kwargs)