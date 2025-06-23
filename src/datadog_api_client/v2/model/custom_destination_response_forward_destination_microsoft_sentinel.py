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
    from datadog_api_client.v2.model.custom_destination_response_forward_destination_microsoft_sentinel_type import (
        CustomDestinationResponseForwardDestinationMicrosoftSentinelType,
    )


class CustomDestinationResponseForwardDestinationMicrosoftSentinel(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_destination_response_forward_destination_microsoft_sentinel_type import (
            CustomDestinationResponseForwardDestinationMicrosoftSentinelType,
        )

        return {
            "client_id": (str,),
            "data_collection_endpoint": (str,),
            "data_collection_rule_id": (str,),
            "stream_name": (str,),
            "tenant_id": (str,),
            "type": (CustomDestinationResponseForwardDestinationMicrosoftSentinelType,),
        }

    attribute_map = {
        "client_id": "client_id",
        "data_collection_endpoint": "data_collection_endpoint",
        "data_collection_rule_id": "data_collection_rule_id",
        "stream_name": "stream_name",
        "tenant_id": "tenant_id",
        "type": "type",
    }

    def __init__(
        self_,
        client_id: str,
        data_collection_endpoint: str,
        data_collection_rule_id: str,
        stream_name: str,
        tenant_id: str,
        type: CustomDestinationResponseForwardDestinationMicrosoftSentinelType,
        **kwargs,
    ):
        """
        The Microsoft Sentinel destination.

        :param client_id: Client ID from the Datadog Azure integration.
        :type client_id: str

        :param data_collection_endpoint: Azure data collection endpoint.
        :type data_collection_endpoint: str

        :param data_collection_rule_id: Azure data collection rule ID.
        :type data_collection_rule_id: str

        :param stream_name: Azure stream name.
        :type stream_name: str

        :param tenant_id: Tenant ID from the Datadog Azure integration.
        :type tenant_id: str

        :param type: Type of the Microsoft Sentinel destination.
        :type type: CustomDestinationResponseForwardDestinationMicrosoftSentinelType
        """
        super().__init__(kwargs)

        self_.client_id = client_id
        self_.data_collection_endpoint = data_collection_endpoint
        self_.data_collection_rule_id = data_collection_rule_id
        self_.stream_name = stream_name
        self_.tenant_id = tenant_id
        self_.type = type
