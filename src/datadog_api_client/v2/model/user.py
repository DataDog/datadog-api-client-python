# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class User(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.user_attributes import UserAttributes
        from datadog_api_client.v2.model.user_response_relationships import UserResponseRelationships
        from datadog_api_client.v2.model.users_type import UsersType

        return {
            "attributes": (UserAttributes,),
            "id": (str,),
            "relationships": (UserResponseRelationships,),
            "type": (UsersType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(self, *args, **kwargs):
        """
        User object returned by the API.

        :param attributes: Attributes of user object returned by the API.
        :type attributes: UserAttributes, optional

        :param id: ID of the user.
        :type id: str, optional

        :param relationships: Relationships of the user object returned by the API.
        :type relationships: UserResponseRelationships, optional

        :param type: Users resource type.
        :type type: UsersType, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(User, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
