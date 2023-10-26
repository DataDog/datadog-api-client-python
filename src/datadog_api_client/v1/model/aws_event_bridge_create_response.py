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
    from datadog_api_client.v1.model.aws_event_bridge_create_status import AWSEventBridgeCreateStatus


class AWSEventBridgeCreateResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.aws_event_bridge_create_status import AWSEventBridgeCreateStatus

        return {
            "event_source_name": (str,),
            "has_bus": (bool,),
            "region": (str,),
            "status": (AWSEventBridgeCreateStatus,),
        }

    attribute_map = {
        "event_source_name": "event_source_name",
        "has_bus": "has_bus",
        "region": "region",
        "status": "status",
    }

    def __init__(
        self_,
        event_source_name: Union[str, UnsetType] = unset,
        has_bus: Union[bool, UnsetType] = unset,
        region: Union[str, UnsetType] = unset,
        status: Union[AWSEventBridgeCreateStatus, UnsetType] = unset,
        **kwargs,
    ):
        """
        A created EventBridge source.

        :param event_source_name: The event source name.
        :type event_source_name: str, optional

        :param has_bus: True if the event bus was created in addition to the source.
        :type has_bus: bool, optional

        :param region: The event source's `AWS region <https://docs.aws.amazon.com/general/latest/gr/rande.html#regional-endpoints>`_.
        :type region: str, optional

        :param status: The event source status "created".
        :type status: AWSEventBridgeCreateStatus, optional
        """
        if event_source_name is not unset:
            kwargs["event_source_name"] = event_source_name
        if has_bus is not unset:
            kwargs["has_bus"] = has_bus
        if region is not unset:
            kwargs["region"] = region
        if status is not unset:
            kwargs["status"] = status
        super().__init__(kwargs)
