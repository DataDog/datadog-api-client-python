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
    from datadog_api_client.v2.model.http_destination_basic_auth_type import HttpDestinationBasicAuthType


class HttpDestinationBasicAuth(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.http_destination_basic_auth_type import HttpDestinationBasicAuthType

        return {
            "password": (str,),
            "type": (HttpDestinationBasicAuthType,),
            "username": (str,),
        }

    attribute_map = {
        "password": "password",
        "type": "type",
        "username": "username",
    }

    def __init__(self_, password: str, type: HttpDestinationBasicAuthType, username: str, **kwargs):
        """
        The HTTP destination basic username and password auth.

        :param password: The password to use for the HTTP request.
        :type password: str

        :param type: The HTTP destination basic auth type.
        :type type: HttpDestinationBasicAuthType

        :param username: The username to use for the HTTP request.
        :type username: str
        """
        super().__init__(kwargs)

        self_.password = password
        self_.type = type
        self_.username = username
