from rest_framework import viewsets

from quiz.models import Question
from quiz.api.serializers import QuestionSerializer

class QuestionViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_queryset(self):
		query_params = self.request.GET.get('q')
		if query_params:
			queryset = self.request.user.questions.filter(is_private=False, title__contains=query_params)
		else:
			queryset = self.request.user.questions.filter(is_private=False)

		return queryset
