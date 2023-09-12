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
    from datadog_api_client.v2.model.http_destination_custom_header_auth_type import HttpDestinationCustomHeaderAuthType


class HttpDestinationCustomHeaderAuth(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.http_destination_custom_header_auth_type import (
            HttpDestinationCustomHeaderAuthType,
        )

        return {
            "header_name": (str,),
            "header_value": (str,),
            "type": (HttpDestinationCustomHeaderAuthType,),
        }

    attribute_map = {
        "header_name": "headerName",
        "header_value": "headerValue",
        "type": "type",
    }

    def __init__(self_, header_name: str, header_value: str, type: HttpDestinationCustomHeaderAuthType, **kwargs):
        """
        The HTTP destination custom header auth.

        :param header_name: The name of the header to use for the HTTP request.
        :type header_name: str

        :param header_value: The value of the header to use for the HTTP request.
        :type header_value: str

        :param type: The HTTP destination custom header auth type.
        :type type: HttpDestinationCustomHeaderAuthType
        """
        super().__init__(kwargs)

        self_.header_name = header_name
        self_.header_value = header_value
        self_.type = type
