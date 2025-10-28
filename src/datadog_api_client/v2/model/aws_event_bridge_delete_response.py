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
    from datadog_api_client.v2.model.aws_event_bridge_delete_response_data import AWSEventBridgeDeleteResponseData


class AWSEventBridgeDeleteResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_event_bridge_delete_response_data import AWSEventBridgeDeleteResponseData

        return {
            "data": (AWSEventBridgeDeleteResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: AWSEventBridgeDeleteResponseData, **kwargs):
        """
        Amazon EventBridge delete response body.

        :param data: Amazon EventBridge delete response data.
        :type data: AWSEventBridgeDeleteResponseData
        """
        super().__init__(kwargs)

        self_.data = data
