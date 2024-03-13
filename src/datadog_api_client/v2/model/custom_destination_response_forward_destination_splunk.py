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
    from datadog_api_client.v2.model.custom_destination_response_forward_destination_splunk_type import (
        CustomDestinationResponseForwardDestinationSplunkType,
    )


class CustomDestinationResponseForwardDestinationSplunk(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_destination_response_forward_destination_splunk_type import (
            CustomDestinationResponseForwardDestinationSplunkType,
        )

        return {
            "endpoint": (str,),
            "type": (CustomDestinationResponseForwardDestinationSplunkType,),
        }

    attribute_map = {
        "endpoint": "endpoint",
        "type": "type",
    }

    def __init__(self_, endpoint: str, type: CustomDestinationResponseForwardDestinationSplunkType, **kwargs):
        """
        The Splunk HTTP Event Collector (HEC) destination.

        :param endpoint: The destination for which logs will be forwarded to.
            Must have HTTPS scheme and forwarding back to Datadog is not allowed.
        :type endpoint: str

        :param type: Type of the Splunk HTTP Event Collector (HEC) destination.
        :type type: CustomDestinationResponseForwardDestinationSplunkType
        """
        super().__init__(kwargs)

        self_.endpoint = endpoint
        self_.type = type
