from .models import Solver, Categories, ExInSolver
from .permissions import IsOwnerOrReadOnly
from .serializers import SolversSerializer, CategoriesSerializers, ExInSolverSerializer, UserSerializer


from rest_framework.response import Response
from rest_framework import status, generics, permissions, renderers, viewsets
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, action


class SolverViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    queryset = Solver.objects.all()
    serializer_class = SolversSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CategoriesViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ExInSolverViewSet(viewsets.ModelViewSet):
    queryset = ExInSolver.objects.all()
    serializer_class = ExInSolverSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
