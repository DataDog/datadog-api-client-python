# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.observability_pipeline_throttle_processor_type import (
        ObservabilityPipelineThrottleProcessorType,
    )


class ObservabilityPipelineThrottleProcessor(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_throttle_processor_type import (
            ObservabilityPipelineThrottleProcessorType,
        )

        return {
            "display_name": (str,),
            "enabled": (bool,),
            "group_by": ([str],),
            "id": (str,),
            "include": (str,),
            "threshold": (int,),
            "type": (ObservabilityPipelineThrottleProcessorType,),
            "window": (float,),
        }

    attribute_map = {
        "display_name": "display_name",
        "enabled": "enabled",
        "group_by": "group_by",
        "id": "id",
        "include": "include",
        "threshold": "threshold",
        "type": "type",
        "window": "window",
    }

    def __init__(
        self_,
        enabled: bool,
        id: str,
        include: str,
        threshold: int,
        type: ObservabilityPipelineThrottleProcessorType,
        window: float,
        display_name: Union[str, UnsetType] = unset,
        group_by: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``throttle`` processor limits the number of events that pass through over a given time window.

        :param display_name: The display name for a component.
        :type display_name: str, optional

        :param enabled: Whether this processor is enabled.
        :type enabled: bool

        :param group_by: Optional list of fields used to group events before the threshold has been reached.
        :type group_by: [str], optional

        :param id: The unique identifier for this processor.
        :type id: str

        :param include: A Datadog search query used to determine which logs this processor targets.
        :type include: str

        :param threshold: the number of events allowed in a given time window. Events sent after the threshold has been reached, are dropped.
        :type threshold: int

        :param type: The processor type. The value should always be ``throttle``.
        :type type: ObservabilityPipelineThrottleProcessorType

        :param window: The time window in seconds over which the threshold applies.
        :type window: float
        """
        if display_name is not unset:
            kwargs["display_name"] = display_name
        if group_by is not unset:
            kwargs["group_by"] = group_by
        super().__init__(kwargs)

        self_.enabled = enabled
        self_.id = id
        self_.include = include
        self_.threshold = threshold
        self_.type = type
        self_.window = window
