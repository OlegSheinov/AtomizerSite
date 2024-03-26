from __future__ import unicode_literals

import graphene
from graphene_django import DjangoObjectType
from wagtail.images.models import Image
from graphene_django.converter import convert_django_field


class WagtailImageRendition(graphene.ObjectType):
    id = graphene.ID()
    url = graphene.String()
    width = graphene.Int()
    height = graphene.Int()


class WagtailImageRenditionList(graphene.ObjectType):
    rendition_list = graphene.List(WagtailImageRendition)
    src_set = graphene.String()

    def resolve_src_set(self, info):
        return ", ".join([f"{img.url} {img.width}w" for img in self.rendition_list])


class WagtailImageNode(DjangoObjectType):
    class Meta:
        model = Image
        exclude_fields = ["tags"]
        description = "Image node"

    # Define all available image rendition options as arguments
    rendition = graphene.Field(
        WagtailImageRendition,
        max=graphene.String(),
        min=graphene.String(),
        width=graphene.Int(),
        height=graphene.Int(),
        fill=graphene.String(),
        format=graphene.String(),
        bgcolor=graphene.String(),
        jpegquality=graphene.Int(),
    )
    rendition_list = graphene.Field(
        WagtailImageRenditionList, sizes=graphene.List(graphene.Int)
    )

    def resolve_rendition(self, info, **kwargs):
        filters = "|".join([f"{key}-{val}" for key, val in kwargs.items()])
        img = self.get_rendition(filters)
        return WagtailImageRendition(
            id=img.id, url=img.url, width=img.width, height=img.height
        )

    def resolve_rendition_list(self, info, sizes=None):
        if sizes is None:
            sizes = []
        rendition_list = [
            WagtailImageNode.resolve_rendition(self, info, width=width)
            for width in sizes
        ]
        return WagtailImageRenditionList(rendition_list=rendition_list)


@convert_django_field.register(Image)
def convert_image(field, registry=None):
    return WagtailImageNode(description=field.help_text, required=not field.null)