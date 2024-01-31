from rest_framework import serializers
from .models import Solver, ExInSolver, Categories
from django.contrib.auth.models import User


class SolversSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Solver
        fields = ['name', 'cat', 'image', 'full_description', 'author', 'verified', 'owner']

    def create(self, validated_data):
        return Solver.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.image = validated_data.get('image', instance.image)
        instance.full_description = validated_data.get('full_description', instance.full_description)
        instance.author = validated_data.get('author', instance.author)
        instance.verified = validated_data.get('verified', instance.verified)
        instance.save()
        return instance


class CategoriesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['name', 'comment']

    def create(self, validated_data):
        return Categories.objects.create(**validated_data)

    def update(self, instance, validate_data):
        instance.name = validate_data.get('name', instance.name)
        instance.comment = validate_data.get('comment', instance.comment)


class ExInSolverSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExInSolver
        fields = ['solver', 'number_ex', 'text', 'correct_answer', 'complexity']

    def create(self, validated_data):
        return ExInSolver.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.solver = validated_data.get('solver', instance.solver)
        instance.number_ex = validated_data.get('number_ex', instance.number_ex)
        instance.text = validated_data.get('text', instance.text)
        instance.correct_answer = validated_data.get('correct_answer', instance.correct_answer)
        instance.complexity = validated_data.get('complexity', instance.complexity)


class UserSerializer(serializers.ModelSerializer):
    solver = serializers.PrimaryKeyRelatedField(many=True, queryset=Solver.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'solver']
