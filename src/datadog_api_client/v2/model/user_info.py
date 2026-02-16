# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class UserInfo(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "org_name": (str,),
            "user_email": (str,),
            "user_name": (str,),
            "user_uuid": (str,),
        }

    attribute_map = {
        "org_name": "orgName",
        "user_email": "userEmail",
        "user_name": "userName",
        "user_uuid": "userUUID",
    }

    def __init__(
        self_, org_name: str, user_email: str, user_uuid: str, user_name: Union[str, UnsetType] = unset, **kwargs
    ):
        """


        :param org_name: The organization name.
        :type org_name: str

        :param user_email: The user's email address.
        :type user_email: str

        :param user_name: The user's name.
        :type user_name: str, optional

        :param user_uuid: The user's UUID.
        :type user_uuid: str
        """
        if user_name is not unset:
            kwargs["user_name"] = user_name
        super().__init__(kwargs)

        self_.org_name = org_name
        self_.user_email = user_email
        self_.user_uuid = user_uuid
