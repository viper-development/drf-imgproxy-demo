from rest_framework.serializers import (
    ModelSerializer
)

from drf_imgproxy.serializers import ImgproxyResizeableImageField

from .models import Picture


class PictureSerializer(ModelSerializer):
    """
    Serializer for Questline model.
    """

    thumbs = ImgproxyResizeableImageField(
        read_only=True,
        source='image'
    )

    class Meta:
        model = Picture
        fields = ("id", "title", "image", "thumbs")
