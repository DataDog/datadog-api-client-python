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
    from datadog_api_client.v2.model.observability_pipeline_tag_cardinality_limit_processor_override_type import (
        ObservabilityPipelineTagCardinalityLimitProcessorOverrideType,
    )


class ObservabilityPipelineTagCardinalityLimitProcessorPerTagLimit(ModelNormal):
    validations = {
        "value_limit": {
            "inclusive_maximum": 1000000,
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_tag_cardinality_limit_processor_override_type import (
            ObservabilityPipelineTagCardinalityLimitProcessorOverrideType,
        )

        return {
            "override_type": (ObservabilityPipelineTagCardinalityLimitProcessorOverrideType,),
            "tag_key": (str,),
            "value_limit": (int,),
        }

    attribute_map = {
        "override_type": "override_type",
        "tag_key": "tag_key",
        "value_limit": "value_limit",
    }

    def __init__(
        self_,
        override_type: ObservabilityPipelineTagCardinalityLimitProcessorOverrideType,
        tag_key: str,
        value_limit: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        A cardinality override for a specific tag key within a per-metric limit.

        :param override_type: How the override is applied. ``limit_override`` enforces a custom limit; ``excluded`` omits the metric or tag from cardinality tracking.
        :type override_type: ObservabilityPipelineTagCardinalityLimitProcessorOverrideType

        :param tag_key: The tag key this override applies to.
        :type tag_key: str

        :param value_limit: The maximum number of distinct values allowed for this tag. Required when ``override_type`` is ``limit_override``. Must be omitted when ``override_type`` is ``excluded``.
        :type value_limit: int, optional
        """
        if value_limit is not unset:
            kwargs["value_limit"] = value_limit
        super().__init__(kwargs)

        self_.override_type = override_type
        self_.tag_key = tag_key
