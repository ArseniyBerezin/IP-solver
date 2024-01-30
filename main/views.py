from .models import Solver, Categories, ExInSolver
from .serializers import SolversSerializer, CategoriesSerializers, ExInSolverSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework import mixins


class SolverList(APIView):
    """
    List all solvers, or create a new solver.
    """
    def get(self, request, format=None):
        solver = Solver.objects.all()
        serializer = SolversSerializer(solver, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SolversSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SolverDetail(APIView):
    """
    Retrieve, update or delete a solver instance.
    """
    def get_object(self, pk):
        try:
            return Solver.objects.get(pk=pk)
        except Solver.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        solver = self.get_object(pk)
        serializer = SolversSerializer(solver)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        solver = self.get_object(pk)
        serializer = SolversSerializer(solver, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        solver = self.get_object(pk)
        solver.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoriesList(APIView):
    """
    List all solvers, or create a new solver.
    """
    def get(self, request, format=None):
        categories = Categories.objects.all()
        serializer = CategoriesSerializers(categories, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CategoriesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoriesDetail(APIView):
    """
    Retrieve, update or delete a solver instance.
    """
    def get_object(self, pk):
        try:
            return Categories.objects.get(pk=pk)
        except Categories.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        categories = self.get_object(pk)
        serializer = CategoriesSerializers(categories)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        categories = self.get_object(pk)
        serializer = CategoriesSerializers(categories, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        categories = self.get_object(pk)
        categories.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ExInSolverList(APIView):
    """
    List all ex, or create a new ex.
    """
    def get(self, request, format=None):
        ex_in_solver = ExInSolver.objects.all()
        serializer = ExInSolverSerializer(ex_in_solver, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ExInSolverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExInSolverDetail(APIView):
    """
    Retrieve, update or delete a ex instance.
    """
    def get_object(self, pk):
        try:
            return ExInSolver.objects.get(pk=pk)
        except ExInSolver.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        ex_in_solver = self.get_object(pk)
        serializer = ExInSolverSerializer(ex_in_solver)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        ex_in_solver = self.get_object(pk)
        serializer = ExInSolverSerializer(ex_in_solver, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        ex_in_solver = self.get_object(pk)
        ex_in_solver.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        