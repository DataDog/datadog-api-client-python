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
    from datadog_api_client.v2.model.aws_event_bridge_delete_request_attributes import (
        AWSEventBridgeDeleteRequestAttributes,
    )
    from datadog_api_client.v2.model.aws_event_bridge_type import AWSEventBridgeType


class AWSEventBridgeDeleteRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_event_bridge_delete_request_attributes import (
            AWSEventBridgeDeleteRequestAttributes,
        )
        from datadog_api_client.v2.model.aws_event_bridge_type import AWSEventBridgeType

        return {
            "attributes": (AWSEventBridgeDeleteRequestAttributes,),
            "type": (AWSEventBridgeType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: AWSEventBridgeDeleteRequestAttributes, type: AWSEventBridgeType, **kwargs):
        """
        Amazon EventBridge delete request data.

        :param attributes: The EventBridge source to be deleted.
        :type attributes: AWSEventBridgeDeleteRequestAttributes

        :param type: Amazon EventBridge resource type.
        :type type: AWSEventBridgeType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
