import graphene
from graphene_django import DjangoObjectType

from home.models import User


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        only_fields = ['tg_id', 'tg_username', 'tg_first_name', 'tg_last_name', 'tariff', 'total_uses',
                       'uses_left']


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
