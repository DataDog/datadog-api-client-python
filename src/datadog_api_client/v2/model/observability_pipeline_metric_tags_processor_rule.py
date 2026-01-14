# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.observability_pipeline_metric_tags_processor_rule_action import (
        ObservabilityPipelineMetricTagsProcessorRuleAction,
    )
    from datadog_api_client.v2.model.observability_pipeline_metric_tags_processor_rule_mode import (
        ObservabilityPipelineMetricTagsProcessorRuleMode,
    )


class ObservabilityPipelineMetricTagsProcessorRule(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_metric_tags_processor_rule_action import (
            ObservabilityPipelineMetricTagsProcessorRuleAction,
        )
        from datadog_api_client.v2.model.observability_pipeline_metric_tags_processor_rule_mode import (
            ObservabilityPipelineMetricTagsProcessorRuleMode,
        )

        return {
            "action": (ObservabilityPipelineMetricTagsProcessorRuleAction,),
            "include": (str,),
            "keys": ([str],),
            "mode": (ObservabilityPipelineMetricTagsProcessorRuleMode,),
        }

    attribute_map = {
        "action": "action",
        "include": "include",
        "keys": "keys",
        "mode": "mode",
    }

    def __init__(
        self_,
        action: ObservabilityPipelineMetricTagsProcessorRuleAction,
        include: str,
        keys: List[str],
        mode: ObservabilityPipelineMetricTagsProcessorRuleMode,
        **kwargs,
    ):
        """
        Defines a rule for filtering metric tags based on key patterns.

        :param action: The action to take on tags with matching keys.
        :type action: ObservabilityPipelineMetricTagsProcessorRuleAction

        :param include: A Datadog search query used to determine which metrics this rule targets.
        :type include: str

        :param keys: A list of tag keys to include or exclude.
        :type keys: [str]

        :param mode: The processing mode for tag filtering.
        :type mode: ObservabilityPipelineMetricTagsProcessorRuleMode
        """
        super().__init__(kwargs)

        self_.action = action
        self_.include = include
        self_.keys = keys
        self_.mode = mode
