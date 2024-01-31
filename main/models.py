from django.core.validators import MaxValueValidator
from django.db import models


class Categories(models.Model):
    """ Модель категорий """

    name = models.CharField(max_length=64, blank=True, null=False)
    comment = models.CharField(max_length=1024, blank=True, null=True)

    def __str__(self):
        return f"категория {self.name}"


class Solver(models.Model):
    """ Модель решебника с заданиями """

    name = models.CharField(max_length=256)
    owner = models.ForeignKey('auth.User', related_name='solver', on_delete=models.CASCADE)  # связь с моделью юзеров
    cat = models.ForeignKey('Categories', on_delete=models.CASCADE)  # связь с моделью категорий
    image = models.ImageField(upload_to='solver_image', blank=True, null=True)
    full_description = models.CharField(max_length=2048)
    author = models.CharField(max_length=256, blank=True, null=False)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f"Решебник {self.name}, подтвержден: {self.verified}, автор: {self.author}"


class ExInSolver(models.Model):
    """ Модель заданий в решебнике """

    solver = models.ForeignKey('Solver', on_delete=models.CASCADE)  # связь с моделью решебника
    number_ex = models.IntegerField(blank=True, null=False)
    text = models.CharField(max_length=2048, blank=True, null=False)
    correct_answer = models.CharField(max_length=1024, blank=True, null=False)
    complexity = models.PositiveIntegerField(validators=[MaxValueValidator(limit_value=5)])

    def __str__(self):
        return f'{self.solver.name} | задание №{self.number_ex}'


