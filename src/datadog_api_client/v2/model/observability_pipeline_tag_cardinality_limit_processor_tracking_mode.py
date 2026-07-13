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
    from datadog_api_client.v2.model.observability_pipeline_tag_cardinality_limit_processor_tracking_mode_mode import (
        ObservabilityPipelineTagCardinalityLimitProcessorTrackingModeMode,
    )


class ObservabilityPipelineTagCardinalityLimitProcessorTrackingMode(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_tag_cardinality_limit_processor_tracking_mode_mode import (
            ObservabilityPipelineTagCardinalityLimitProcessorTrackingModeMode,
        )

        return {
            "mode": (ObservabilityPipelineTagCardinalityLimitProcessorTrackingModeMode,),
        }

    attribute_map = {
        "mode": "mode",
    }

    def __init__(self_, mode: ObservabilityPipelineTagCardinalityLimitProcessorTrackingModeMode, **kwargs):
        """
        Controls whether the processor uses exact or probabilistic tag tracking.

        :param mode: The cardinality tracking algorithm to use.
        :type mode: ObservabilityPipelineTagCardinalityLimitProcessorTrackingModeMode
        """
        super().__init__(kwargs)

        self_.mode = mode
