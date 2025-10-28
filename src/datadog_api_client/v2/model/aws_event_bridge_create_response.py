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
    from datadog_api_client.v2.model.aws_event_bridge_create_response_data import AWSEventBridgeCreateResponseData


class AWSEventBridgeCreateResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_event_bridge_create_response_data import AWSEventBridgeCreateResponseData

        return {
            "data": (AWSEventBridgeCreateResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: AWSEventBridgeCreateResponseData, **kwargs):
        """
        Amazon EventBridge create response body.

        :param data: Amazon EventBridge create response data.
        :type data: AWSEventBridgeCreateResponseData
        """
        super().__init__(kwargs)

        self_.data = data
