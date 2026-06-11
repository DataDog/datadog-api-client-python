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


class OrgAuthorizedClientAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "disabled": (bool,),
            "last_exercised": (datetime, none_type),
            "user_count": (int,),
        }

    attribute_map = {
        "disabled": "disabled",
        "last_exercised": "last_exercised",
        "user_count": "user_count",
    }

    def __init__(self_, disabled: bool, last_exercised: Union[datetime, none_type], user_count: int, **kwargs):
        """
        Attributes of an org authorized client.

        :param disabled: Whether the organization has disabled this client.
        :type disabled: bool

        :param last_exercised: The date and time this client was last exercised.
        :type last_exercised: datetime, none_type

        :param user_count: The number of users in the organization who have authorized this client.
        :type user_count: int
        """
        super().__init__(kwargs)

        self_.disabled = disabled
        self_.last_exercised = last_exercised
        self_.user_count = user_count
