# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.relationship_to_user import RelationshipToUser

    globals()["RelationshipToUser"] = RelationshipToUser


class UserInvitationRelationships(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "user": (RelationshipToUser,),
        }

    attribute_map = {
        "user": "user",
    }

    read_only_vars = {}

    def __init__(self, user, *args, **kwargs):
        """
        Relationships data for user invitation.

        :param user: Relationship to user.
        :type user: RelationshipToUser
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.user = user

    @classmethod
    def _from_openapi_data(cls, user, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UserInvitationRelationships, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.user = user
        return self
