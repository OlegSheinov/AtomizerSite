from datetime import datetime, timezone

import graphene
from django.utils.translation import gettext_lazy as _
from graphene_django import DjangoObjectType

from home.models import User
from home.utils.formatted_date import format_time


class UserNode(DjangoObjectType):
    tariff = graphene.String()
    time_with_us = graphene.String()

    class Meta:
        model = User
        only_fields = ['tg_id', 'tg_username', 'tg_first_name', 'tg_last_name', 'total_uses',
                       'uses_left', 'date_joined']

    def resolve_tariff(self: User, info):
        return self.tariff.name if self.tariff else _("Nothing")

    def resolve_time_with_us(self: User, info):
        current_date = datetime.now(timezone.utc)
        date_joined = self.date_joined
        time_with_us = current_date - date_joined
        text = format_time(time_with_us.seconds)
        return text


class CreateUserMutation(graphene.Mutation):
    class Arguments:
        tg_id = graphene.Int()
        tg_username = graphene.String()
        tg_first_name = graphene.String()
        tg_last_name = graphene.String()

    create = graphene.Field(graphene.String)

    def mutate(self, info, tg_id, tg_username, tg_first_name, tg_last_name):
        user = User(tg_id=tg_id, tg_username=tg_username, tg_first_name=tg_first_name, tg_last_name=tg_last_name,
                    username=tg_username)
        try:
            user.save()
            create = True
        except BaseException as err:
            create = False
        return CreateUserMutation(create=create)


class UserQuery:
    get_user = graphene.Field(UserNode)
    create_user = CreateUserMutation.Field()

    def resolve_get_user(self, info, **kwargs):
        user = User.objects.user(info)
        return user
