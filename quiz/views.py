from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Quizzes, Question
from .serializer import QuizSerializer, RandomQuestionSerializer, QuizQuestionSerializer


class Quiz(generics.ListAPIView):
    queryset = Quizzes.objects.all()
    serializer_class = QuizSerializer


class RandomQuestion(APIView):
    def get(self, request, **kwargs):
        question = Question.objects.filter(quiz__title=kwargs['topic']).order_by("?")[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)


class QuizQuestion(APIView):
    def get(self, request, **kwargs):
        question = Question.objects.filter(quiz__title=kwargs['topic'])
        serializer = QuizQuestionSerializer(question, many=True)
        return Response(serializer.data)

