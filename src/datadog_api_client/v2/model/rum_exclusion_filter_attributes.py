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
    from datadog_api_client.v2.model.rum_exclusion_filter_event_type import RumExclusionFilterEventType


class RumExclusionFilterAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_exclusion_filter_event_type import RumExclusionFilterEventType

        return {
            "enabled": (bool,),
            "event_type": (RumExclusionFilterEventType,),
            "name": (str,),
            "query": (str,),
        }

    attribute_map = {
        "enabled": "enabled",
        "event_type": "event_type",
        "name": "name",
        "query": "query",
    }

    def __init__(
        self_,
        enabled: Union[bool, UnsetType] = unset,
        event_type: Union[RumExclusionFilterEventType, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes of an exclusion filter.

        :param enabled: Whether the exclusion filter is active.
        :type enabled: bool, optional

        :param event_type: The type of RUM events to filter on.
        :type event_type: RumExclusionFilterEventType, optional

        :param name: The name of the exclusion filter.
        :type name: str, optional

        :param query: Additional query used to further restrict which RUM events are excluded.
            Combined with ``event_type`` when both are provided.
        :type query: str, optional
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if event_type is not unset:
            kwargs["event_type"] = event_type
        if name is not unset:
            kwargs["name"] = name
        if query is not unset:
            kwargs["query"] = query
        super().__init__(kwargs)
