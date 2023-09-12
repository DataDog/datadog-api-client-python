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
    from datadog_api_client.v2.model.splunk_hec_destination_type import SplunkHecDestinationType


class SplunkHecDestination(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.splunk_hec_destination_type import SplunkHecDestinationType

        return {
            "access_token": (str,),
            "endpoint": (str,),
            "type": (SplunkHecDestinationType,),
        }

    attribute_map = {
        "access_token": "accessToken",
        "endpoint": "endpoint",
        "type": "type",
    }

    def __init__(self_, access_token: str, endpoint: str, type: SplunkHecDestinationType, **kwargs):
        """
        The Splunk destination.

        :param access_token: The access token of the Splunk destination.
        :type access_token: str

        :param endpoint: The intake URL to forward events to.
        :type endpoint: str

        :param type: The Splunk destination type.
        :type type: SplunkHecDestinationType
        """
        super().__init__(kwargs)

        self_.access_token = access_token
        self_.endpoint = endpoint
        self_.type = type
