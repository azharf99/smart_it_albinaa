from django.urls import path
from .views import ScoresIndex, createScore, ScoresClassIndex


urlpatterns = [
    path('', ScoresIndex.as_view(), name='score-index'),
    path('<str:class_name>', ScoresClassIndex.as_view(), name='score-class'),
    path('<str:class_name>/create', createScore, name='score-create')
]