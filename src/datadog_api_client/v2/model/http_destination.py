# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.http_destination_auth import HttpDestinationAuth
    from datadog_api_client.v2.model.http_destination_type import HttpDestinationType
    from datadog_api_client.v2.model.http_destination_basic_auth import HttpDestinationBasicAuth
    from datadog_api_client.v2.model.http_destination_custom_header_auth import HttpDestinationCustomHeaderAuth


class HttpDestination(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.http_destination_auth import HttpDestinationAuth
        from datadog_api_client.v2.model.http_destination_type import HttpDestinationType

        return {
            "auth": (HttpDestinationAuth,),
            "endpoint": (str,),
            "type": (HttpDestinationType,),
        }

    attribute_map = {
        "auth": "auth",
        "endpoint": "endpoint",
        "type": "type",
    }

    def __init__(
        self_,
        auth: Union[HttpDestinationAuth, HttpDestinationBasicAuth, HttpDestinationCustomHeaderAuth],
        endpoint: str,
        type: HttpDestinationType,
        **kwargs,
    ):
        """
        The HTTP destination.

        :param auth: The authentication method used for HTTP destinations.
        :type auth: HttpDestinationAuth

        :param endpoint: The intake URL to forward events to.
        :type endpoint: str

        :param type: The HTTP destination type.
        :type type: HttpDestinationType
        """
        super().__init__(kwargs)

        self_.auth = auth
        self_.endpoint = endpoint
        self_.type = type
