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
    from datadog_api_client.v2.model.rum_retention_filter_event_type import RumRetentionFilterEventType


class RumRetentionFilterUpdateAttributes(ModelNormal):
    validations = {
        "sample_rate": {
            "inclusive_maximum": 100,
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_retention_filter_event_type import RumRetentionFilterEventType

        return {
            "enabled": (bool,),
            "event_type": (RumRetentionFilterEventType,),
            "name": (str,),
            "query": (str,),
            "sample_rate": (int,),
        }

    attribute_map = {
        "enabled": "enabled",
        "event_type": "event_type",
        "name": "name",
        "query": "query",
        "sample_rate": "sample_rate",
    }

    def __init__(
        self_,
        enabled: Union[bool, UnsetType] = unset,
        event_type: Union[RumRetentionFilterEventType, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
        sample_rate: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        The object describing attributes of a RUM retention filter to update.

        :param enabled: Whether the retention filter is enabled.
        :type enabled: bool, optional

        :param event_type: The type of RUM events to filter on.
        :type event_type: RumRetentionFilterEventType, optional

        :param name: The name of a RUM retention filter.
        :type name: str, optional

        :param query: The query string for a RUM retention filter.
        :type query: str, optional

        :param sample_rate: The sample rate for a RUM retention filter, between 0 and 100.
        :type sample_rate: int, optional
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if event_type is not unset:
            kwargs["event_type"] = event_type
        if name is not unset:
            kwargs["name"] = name
        if query is not unset:
            kwargs["query"] = query
        if sample_rate is not unset:
            kwargs["sample_rate"] = sample_rate
        super().__init__(kwargs)
