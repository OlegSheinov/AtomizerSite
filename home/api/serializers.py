from rest_framework import serializers

from home.models.snippets import TgBotSnippet


class BotSettingSerializer(serializers.ModelSerializer):
    terms_of_use = serializers.SerializerMethodField()

    class Meta:
        model = TgBotSnippet
        fields = "__all__"

    def get_terms_of_use(self, obj):
        return obj.terms_of_use_link.full_url
