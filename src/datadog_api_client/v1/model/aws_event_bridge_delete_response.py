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
    from datadog_api_client.v1.model.aws_event_bridge_delete_status import AWSEventBridgeDeleteStatus


class AWSEventBridgeDeleteResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.aws_event_bridge_delete_status import AWSEventBridgeDeleteStatus

        return {
            "status": (AWSEventBridgeDeleteStatus,),
        }

    attribute_map = {
        "status": "status",
    }

    def __init__(self_, status: Union[AWSEventBridgeDeleteStatus, UnsetType] = unset, **kwargs):
        """
        An indicator of the successful deletion of an EventBridge source.

        :param status: The event source status "empty".
        :type status: AWSEventBridgeDeleteStatus, optional
        """
        if status is not unset:
            kwargs["status"] = status
        super().__init__(kwargs)
