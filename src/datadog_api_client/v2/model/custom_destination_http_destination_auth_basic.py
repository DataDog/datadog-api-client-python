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
    from datadog_api_client.v2.model.custom_destination_http_destination_auth_basic_type import (
        CustomDestinationHttpDestinationAuthBasicType,
    )


class CustomDestinationHttpDestinationAuthBasic(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_destination_http_destination_auth_basic_type import (
            CustomDestinationHttpDestinationAuthBasicType,
        )

        return {
            "password": (str,),
            "type": (CustomDestinationHttpDestinationAuthBasicType,),
            "username": (str,),
        }

    attribute_map = {
        "password": "password",
        "type": "type",
        "username": "username",
    }

    def __init__(self_, password: str, type: CustomDestinationHttpDestinationAuthBasicType, username: str, **kwargs):
        """
        Basic access authentication.

        :param password: The password of the authentication. This field is not returned by the API.
        :type password: str

        :param type: Type of the basic access authentication.
        :type type: CustomDestinationHttpDestinationAuthBasicType

        :param username: The username of the authentication. This field is not returned by the API.
        :type username: str
        """
        super().__init__(kwargs)

        self_.password = password
        self_.type = type
        self_.username = username
