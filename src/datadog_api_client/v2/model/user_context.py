# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.user_info import UserInfo


class UserContext(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.user_info import UserInfo

        return {
            "user_info": (UserInfo,),
        }

    attribute_map = {
        "user_info": "userInfo",
    }

    def __init__(self_, user_info: UserInfo, **kwargs):
        """


        :param user_info:
        :type user_info: UserInfo
        """
        super().__init__(kwargs)

        self_.user_info = user_info
