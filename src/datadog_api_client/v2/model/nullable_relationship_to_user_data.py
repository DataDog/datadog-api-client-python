# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.users_type import UsersType

    globals()["UsersType"] = UsersType


class NullableRelationshipToUserData(ModelNormal):

    validations = {}
    _nullable = True

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "id": (str,),
            "type": (UsersType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    read_only_vars = {}

    def __init__(self, id, type, *args, **kwargs):
        """
        Relationship to user object.

        :param id: A unique identifier that represents the user.
        :type id: str

        :param type: Users resource type.
        :type type: UsersType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.id = id
        self.type = type

    @classmethod
    def _from_openapi_data(cls, id, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(NullableRelationshipToUserData, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.id = id
        self.type = type
        return self
