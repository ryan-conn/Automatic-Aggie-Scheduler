""" Heavily based off of Good Bull Schedules """

from django.db import models

class GradeManager(models.Manager):
    """ TODO """

    def instructor_performance(self, dept: str, course_num: str, instructor: str):
        """ Calculates the average """
        return (
            self.prefetch_related("section") # What does this do?
            # Why are the below just strings? Shouldn't they be models
            .filter(
                section__subject=dept,
                section__course_num=course_num,
                section__instructor=instructor,
            )
            .aggregate(
                gpa=models.Avg("gpa"),

                # We want a sum so we can more-easily calculate the percentage
                A=models.Sum("A"),
                B=models.Sum("B"),
                C=models.Sum("C"),
                D=models.Sum("D"),
                F=models.Sum("F"),
                I=models.Sum("I"),
                S=models.Sum("S"),
                U=models.Sum("U"),
                Q=models.Sum("Q"),
                X=models.Sum("X"),
                # Total students?
            )
        )

class Grades(models.Model):
    """ TODO """

    # Is the primary key, since one section = one grade distribution
    # Also, a OneToOneField is a ForeignKey that has unique=true (caused by primary_key)
    section = models.OneToOneField("Section", on_delete=models.CASCADE, primary_key=True)

    A = models.IntegerField(db_index=True)
    B = models.IntegerField(db_index=True)
    C = models.IntegerField(db_index=True)
    D = models.IntegerField(db_index=True)
    F = models.IntegerField(db_index=True)

    # TODO Figure what these are below
    I = models.IntegerField(db_index=True)
    S = models.IntegerField(db_index=True)
    U = models.IntegerField(db_index=True)
    Q = models.IntegerField(db_index=True)
    X = models.IntegerField(db_index=True)
    objects = GradeManager()

    gpa = models.FloatField()

    #section = models.OneToOneField(
    #    "Section", on_delete=models.CASCADE, related_name="grades", db_index=True
    #)

    class Meta:
        db_table = "grades"
