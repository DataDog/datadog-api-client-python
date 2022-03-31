# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.user_invitation_relationships import UserInvitationRelationships
    from datadog_api_client.v2.model.user_invitations_type import UserInvitationsType

    globals()["UserInvitationRelationships"] = UserInvitationRelationships
    globals()["UserInvitationsType"] = UserInvitationsType


class UserInvitationData(ModelNormal):
    @cached_property
    def openapi_types(_):
        lazy_import()
        return {
            "relationships": (UserInvitationRelationships,),
            "type": (UserInvitationsType,),
        }

    attribute_map = {
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(self, relationships, type, *args, **kwargs):
        """
        Object to create a user invitation.

        :param relationships: Relationships data for user invitation.
        :type relationships: UserInvitationRelationships

        :param type: User invitations type.
        :type type: UserInvitationsType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.relationships = relationships
        self.type = type

    @classmethod
    def _from_openapi_data(cls, relationships, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UserInvitationData, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.relationships = relationships
        self.type = type
        return self
