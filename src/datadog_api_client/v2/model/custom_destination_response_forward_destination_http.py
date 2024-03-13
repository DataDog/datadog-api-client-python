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
    from datadog_api_client.v2.model.custom_destination_response_http_destination_auth import (
        CustomDestinationResponseHttpDestinationAuth,
    )
    from datadog_api_client.v2.model.custom_destination_response_forward_destination_http_type import (
        CustomDestinationResponseForwardDestinationHttpType,
    )
    from datadog_api_client.v2.model.custom_destination_response_http_destination_auth_basic import (
        CustomDestinationResponseHttpDestinationAuthBasic,
    )
    from datadog_api_client.v2.model.custom_destination_response_http_destination_auth_custom_header import (
        CustomDestinationResponseHttpDestinationAuthCustomHeader,
    )


class CustomDestinationResponseForwardDestinationHttp(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_destination_response_http_destination_auth import (
            CustomDestinationResponseHttpDestinationAuth,
        )
        from datadog_api_client.v2.model.custom_destination_response_forward_destination_http_type import (
            CustomDestinationResponseForwardDestinationHttpType,
        )

        return {
            "auth": (CustomDestinationResponseHttpDestinationAuth,),
            "endpoint": (str,),
            "type": (CustomDestinationResponseForwardDestinationHttpType,),
        }

    attribute_map = {
        "auth": "auth",
        "endpoint": "endpoint",
        "type": "type",
    }

    def __init__(
        self_,
        auth: Union[
            CustomDestinationResponseHttpDestinationAuth,
            CustomDestinationResponseHttpDestinationAuthBasic,
            CustomDestinationResponseHttpDestinationAuthCustomHeader,
        ],
        endpoint: str,
        type: CustomDestinationResponseForwardDestinationHttpType,
        **kwargs,
    ):
        """
        The HTTP destination.

        :param auth: Authentication method of the HTTP requests.
        :type auth: CustomDestinationResponseHttpDestinationAuth

        :param endpoint: The destination for which logs will be forwarded to.
            Must have HTTPS scheme and forwarding back to Datadog is not allowed.
        :type endpoint: str

        :param type: Type of the HTTP destination.
        :type type: CustomDestinationResponseForwardDestinationHttpType
        """
        super().__init__(kwargs)

        self_.auth = auth
        self_.endpoint = endpoint
        self_.type = type
