from django.db import models

class Kafedralar(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Fakultetlar(models.Model):
    name = models.CharField(max_length=50)
    kafedra = models.ForeignKey(Kafedralar, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Guruhlar(models.Model):
    name = models.CharField(max_length=50)
    fakultet = models.ForeignKey(Fakultetlar, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Talabalar(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50, blank=True, null=True)
    guruh = models.ForeignKey(Guruhlar, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.surname}"

class Ustozlar(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50, blank=True, null=True)
    kafedra = models.ForeignKey(Kafedralar, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.surname}"

class Fanlar(models.Model):
    name = models.CharField(max_length=50)
    ustoz = models.ForeignKey(Ustozlar, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Universitetlar_royxati(models.Model):
    name = models.CharField(max_length=50)
    fakultet = models.ForeignKey(Fakultetlar, on_delete=models.CASCADE)
    kafedra = models.ForeignKey(Kafedralar, on_delete=models.CASCADE)
    guruh = models.ForeignKey(Guruhlar, on_delete=models.CASCADE)
    talaba = models.ForeignKey(Talabalar, on_delete=models.CASCADE)
    ustoz = models.ForeignKey(Ustozlar, on_delete=models.CASCADE)
    fan = models.ForeignKey(Fanlar, on_delete=models.CASCADE)

    def __str__(self):
        return self.name