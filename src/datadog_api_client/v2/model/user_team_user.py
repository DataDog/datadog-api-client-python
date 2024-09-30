# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.user_team_user_attributes import UserTeamUserAttributes
    from datadog_api_client.v2.model.user_team_user_type import UserTeamUserType


class UserTeamUser(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.user_team_user_attributes import UserTeamUserAttributes
        from datadog_api_client.v2.model.user_team_user_type import UserTeamUserType

        return {
            "attributes": (UserTeamUserAttributes,),
            "id": (str,),
            "type": (UserTeamUserType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: UserTeamUserType,
        attributes: Union[UserTeamUserAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``UserTeamUser`` object.

        :param attributes: The definition of ``UserTeamUserAttributes`` object.
        :type attributes: UserTeamUserAttributes, optional

        :param id: The ``UserTeamUser`` ID.
        :type id: str, optional

        :param type: User team user type
        :type type: UserTeamUserType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
