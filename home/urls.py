from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

app_name = 'api'
urlpatterns = [
    path('graphql/', csrf_exempt(GraphQLView.as_view())),
    path('graphiql/', csrf_exempt(GraphQLView.as_view(graphiql=True, pretty=True))),
]