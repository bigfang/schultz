from typing import ClassVar

from ninja import ModelSchema

from .models import User


class UserSchema(ModelSchema):
    class Meta:
        model = User
        model_fields: ClassVar[list[str]] = ['id', 'username', 'email']
