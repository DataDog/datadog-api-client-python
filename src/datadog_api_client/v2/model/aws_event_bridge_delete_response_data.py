# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.aws_event_bridge_delete_response_attributes import (
        AWSEventBridgeDeleteResponseAttributes,
    )
    from datadog_api_client.v2.model.aws_event_bridge_type import AWSEventBridgeType


class AWSEventBridgeDeleteResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_event_bridge_delete_response_attributes import (
            AWSEventBridgeDeleteResponseAttributes,
        )
        from datadog_api_client.v2.model.aws_event_bridge_type import AWSEventBridgeType

        return {
            "attributes": (AWSEventBridgeDeleteResponseAttributes,),
            "id": (str,),
            "type": (AWSEventBridgeType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: AWSEventBridgeDeleteResponseAttributes,
        type: AWSEventBridgeType,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Amazon EventBridge delete response data.

        :param attributes: The EventBridge source delete response attributes.
        :type attributes: AWSEventBridgeDeleteResponseAttributes

        :param id: The ID of the Amazon EventBridge list response data.
        :type id: str, optional

        :param type: Amazon EventBridge resource type.
        :type type: AWSEventBridgeType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
