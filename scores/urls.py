from django.urls import path
from .views import ScoresIndex, createScore


urlpatterns = [
    path('', ScoresIndex.as_view(), name='score-index'),
    path('create', createScore, name='score-create')
]