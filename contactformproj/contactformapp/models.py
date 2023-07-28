from django.db import models


class testpaper(models.Model):
    testname = models.CharField(max_length=25)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.testname


class question(models.Model):
    objects = models.Manager()
    question = models.CharField(max_length=500)
    option1 = models.CharField(max_length=300)
    option2 = models.CharField(max_length=300)
    option3 = models.CharField(max_length=300)
    option4 = models.CharField(max_length=300)
    correctanswer = models.CharField(max_length=1)
    explanation = models.CharField(max_length=500)
    testpapers = models.ForeignKey(testpaper, on_delete=models.CASCADE)

#
# # Create your models here.
# class user(models.Model):
#     objects = models.Manager()
#     firstname = models.CharField(max_length=50)
#     lastname = models.CharField(max_length=50, required=False, null=True, blank=True)
#     password = models.CharField(max_length=50)
#     emailid = models.CharField(max_length=50)
#     paidmember = models.CharField(default="N")
#     paidon = models.DateField(null=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         db_table = "user"


# class usertestdetails(models.Model):
#     objects = models.Manager()
#     name = models.ForeignKey(user, on_delete=models.CASCADE)
#     tests = models.ForeignKey(testpaper, on_delete=models.CASCADE)
#     questions = models.ForeignKey(question, on_delete=models.CASCADE)
