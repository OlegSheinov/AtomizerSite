from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from home.api.serializers import BotSettingSerializer
from home.models.snippets import TgBotSnippet


class GetBotSettingsAPI(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        if request.GET.get("fields"):
            fields = list(filter(None, request.GET.get("fields").split(";")))
        else:
            fields = []
        bot_setting: TgBotSnippet = TgBotSnippet.objects.first()
        serializer = BotSettingSerializer(bot_setting, many=False)
        data = {}
        if fields:
            for key, value in serializer.data.items():
                if key in fields:
                    data[key] = value
        else:
            data = serializer.data
        return Response(data)
