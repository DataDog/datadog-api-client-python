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
    from datadog_api_client.v2.model.monitor_downtime_match_attribute_response import (
        MonitorDowntimeMatchAttributeResponse,
    )
    from datadog_api_client.v2.model.monitor_downtime_match_resource_type import MonitorDowntimeMatchResourceType


class MonitorDowntimeMatchResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.monitor_downtime_match_attribute_response import (
            MonitorDowntimeMatchAttributeResponse,
        )
        from datadog_api_client.v2.model.monitor_downtime_match_resource_type import MonitorDowntimeMatchResourceType

        return {
            "attributes": (MonitorDowntimeMatchAttributeResponse,),
            "id": (str,),
            "type": (MonitorDowntimeMatchResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[MonitorDowntimeMatchAttributeResponse, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[MonitorDowntimeMatchResourceType, UnsetType] = unset,
        **kwargs,
    ):
        """
        A downtime match.

        :param attributes: Downtime match details.
        :type attributes: MonitorDowntimeMatchAttributeResponse, optional

        :param id: The downtime ID.
        :type id: str, optional

        :param type: Monitor Downtime Match resource type.
        :type type: MonitorDowntimeMatchResourceType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
