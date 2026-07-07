# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
)


class UserAuthorizedClientAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (datetime,),
            "disabled": (bool,),
            "last_exercised": (datetime, none_type),
            "modified_at": (datetime,),
            "org_disabled": (bool,),
        }

    attribute_map = {
        "created_at": "created_at",
        "disabled": "disabled",
        "last_exercised": "last_exercised",
        "modified_at": "modified_at",
        "org_disabled": "org_disabled",
    }

    def __init__(
        self_,
        created_at: datetime,
        disabled: bool,
        last_exercised: Union[datetime, none_type],
        modified_at: datetime,
        org_disabled: bool,
        **kwargs,
    ):
        """
        Attributes of a user authorized client.

        :param created_at: The date and time this authorization was created.
        :type created_at: datetime

        :param disabled: Whether the user has disabled this authorization.
        :type disabled: bool

        :param last_exercised: The date and time this authorization was last exercised.
        :type last_exercised: datetime, none_type

        :param modified_at: The date and time this authorization was last modified.
        :type modified_at: datetime

        :param org_disabled: Whether the organization has disabled this authorization.
        :type org_disabled: bool
        """
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.disabled = disabled
        self_.last_exercised = last_exercised
        self_.modified_at = modified_at
        self_.org_disabled = org_disabled
