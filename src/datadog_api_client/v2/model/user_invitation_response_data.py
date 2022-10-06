# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.user_invitation_data_attributes import UserInvitationDataAttributes
    from datadog_api_client.v2.model.user_invitations_type import UserInvitationsType


class UserInvitationResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.user_invitation_data_attributes import UserInvitationDataAttributes
        from datadog_api_client.v2.model.user_invitations_type import UserInvitationsType

        return {
            "attributes": (UserInvitationDataAttributes,),
            "id": (str,),
            "type": (UserInvitationsType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[UserInvitationDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[UserInvitationsType, UnsetType] = unset,
        *args,
        **kwargs,
    ):
        """
        Object of a user invitation returned by the API.

        :param attributes: Attributes of a user invitation.
        :type attributes: UserInvitationDataAttributes, optional

        :param id: ID of the user invitation.
        :type id: str, optional

        :param type: User invitations type.
        :type type: UserInvitationsType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)

        self_._check_pos_args(args)
