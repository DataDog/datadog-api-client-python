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
    from datadog_api_client.v2.model.custom_destination_response_http_destination_auth_custom_header_type import (
        CustomDestinationResponseHttpDestinationAuthCustomHeaderType,
    )


class CustomDestinationResponseHttpDestinationAuthCustomHeader(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_destination_response_http_destination_auth_custom_header_type import (
            CustomDestinationResponseHttpDestinationAuthCustomHeaderType,
        )

        return {
            "header_name": (str,),
            "type": (CustomDestinationResponseHttpDestinationAuthCustomHeaderType,),
        }

    attribute_map = {
        "header_name": "header_name",
        "type": "type",
    }

    def __init__(self_, header_name: str, type: CustomDestinationResponseHttpDestinationAuthCustomHeaderType, **kwargs):
        """
        Custom header access authentication.

        :param header_name: The header name of the authentication.
        :type header_name: str

        :param type: Type of the custom header access authentication.
        :type type: CustomDestinationResponseHttpDestinationAuthCustomHeaderType
        """
        super().__init__(kwargs)

        self_.header_name = header_name
        self_.type = type
