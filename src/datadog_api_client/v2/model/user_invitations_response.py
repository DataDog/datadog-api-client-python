# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.user_invitation_response_data import UserInvitationResponseData


@dataclass
class UserInvitationsResponseJSON:
    id: str
    created_at: Union[datetime, UnsetType] = unset
    expires_at: Union[datetime, UnsetType] = unset
    invite_type: Union[str, UnsetType] = unset
    uuid: Union[str, UnsetType] = unset


class UserInvitationsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.user_invitation_response_data import UserInvitationResponseData

        return {
            "data": ([UserInvitationResponseData],),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = UserInvitationsResponseJSON

    def __init__(self_, data: Union[List[UserInvitationResponseData], UnsetType] = unset, **kwargs):
        """
        User invitations as returned by the API.

        :param data: Array of user invitations.
        :type data: [UserInvitationResponseData], optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
