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
    from datadog_api_client.v2.model.aws_event_bridge_list_response_attributes import (
        AWSEventBridgeListResponseAttributes,
    )
    from datadog_api_client.v2.model.aws_event_bridge_type import AWSEventBridgeType


class AWSEventBridgeListResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_event_bridge_list_response_attributes import (
            AWSEventBridgeListResponseAttributes,
        )
        from datadog_api_client.v2.model.aws_event_bridge_type import AWSEventBridgeType

        return {
            "attributes": (AWSEventBridgeListResponseAttributes,),
            "id": (str,),
            "type": (AWSEventBridgeType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: AWSEventBridgeListResponseAttributes, type: AWSEventBridgeType, **kwargs):
        """
        Amazon EventBridge list response data.

        :param attributes: An object describing the EventBridge configuration for multiple accounts.
        :type attributes: AWSEventBridgeListResponseAttributes

        :param id: The ID of the Amazon EventBridge list response data.
        :type id: str

        :param type: Amazon EventBridge resource type.
        :type type: AWSEventBridgeType
        """
        super().__init__(kwargs)
        id = kwargs.get("id", "get_event_bridge")

        self_.attributes = attributes
        self_.id = id
        self_.type = type
