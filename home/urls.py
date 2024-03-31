from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

from home.views import GetFrameView

app_name = 'api'
urlpatterns = [
    path('graphql/', csrf_exempt(GraphQLView.as_view())),
    path('graphiql/', csrf_exempt(GraphQLView.as_view(graphiql=True, pretty=True))),
    path('get_frame/', csrf_exempt(GetFrameView.as_view()))
]