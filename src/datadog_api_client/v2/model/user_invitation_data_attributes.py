# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class UserInvitationDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (datetime,),
            "expires_at": (datetime,),
            "invite_type": (str,),
            "uuid": (str,),
        }

    attribute_map = {
        "created_at": "created_at",
        "expires_at": "expires_at",
        "invite_type": "invite_type",
        "uuid": "uuid",
    }

    def __init__(self, *args, **kwargs):
        """
        Attributes of a user invitation.

        :param created_at: Creation time of the user invitation.
        :type created_at: datetime, optional

        :param expires_at: Time of invitation expiration.
        :type expires_at: datetime, optional

        :param invite_type: Type of invitation.
        :type invite_type: str, optional

        :param uuid: UUID of the user invitation.
        :type uuid: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UserInvitationDataAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
