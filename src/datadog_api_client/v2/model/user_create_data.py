# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class UserCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.user_create_attributes import UserCreateAttributes
        from datadog_api_client.v2.model.user_relationships import UserRelationships
        from datadog_api_client.v2.model.users_type import UsersType

        return {
            "attributes": (UserCreateAttributes,),
            "relationships": (UserRelationships,),
            "type": (UsersType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(self, attributes, type, *args, **kwargs):
        """
        Object to create a user.

        :param attributes: Attributes of the created user.
        :type attributes: UserCreateAttributes

        :param relationships: Relationships of the user object.
        :type relationships: UserRelationships, optional

        :param type: Users resource type.
        :type type: UsersType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.attributes = attributes
        self.type = type

    @classmethod
    def _from_openapi_data(cls, attributes, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UserCreateData, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.attributes = attributes
        self.type = type
        return self
