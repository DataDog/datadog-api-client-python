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
    from datadog_api_client.v2.model.aggregated_high_frozen_frame_rate import AggregatedHighFrozenFrameRate
    from datadog_api_client.v2.model.aggregated_high_script_eval import AggregatedHighScriptEval
    from datadog_api_client.v2.model.aggregated_low_cache_hit_rate import AggregatedLowCacheHitRate
    from datadog_api_client.v2.model.aggregated_mobile_scroll_friction import AggregatedMobileScrollFriction
    from datadog_api_client.v2.model.aggregated_slow_fcp_high_bytes import AggregatedSlowFCPHighBytes
    from datadog_api_client.v2.model.aggregated_slow_interaction_long_task import AggregatedSlowInteractionLongTask
    from datadog_api_client.v2.model.aggregated_uncompressed_resource import AggregatedUncompressedResource


class SignalsProblemsDetections(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aggregated_high_frozen_frame_rate import AggregatedHighFrozenFrameRate
        from datadog_api_client.v2.model.aggregated_high_script_eval import AggregatedHighScriptEval
        from datadog_api_client.v2.model.aggregated_low_cache_hit_rate import AggregatedLowCacheHitRate
        from datadog_api_client.v2.model.aggregated_mobile_scroll_friction import AggregatedMobileScrollFriction
        from datadog_api_client.v2.model.aggregated_slow_fcp_high_bytes import AggregatedSlowFCPHighBytes
        from datadog_api_client.v2.model.aggregated_slow_interaction_long_task import AggregatedSlowInteractionLongTask
        from datadog_api_client.v2.model.aggregated_uncompressed_resource import AggregatedUncompressedResource

        return {
            "high_frozen_frame_rates": ([AggregatedHighFrozenFrameRate],),
            "high_script_evaluations": ([AggregatedHighScriptEval],),
            "low_cache_hit_rates": ([AggregatedLowCacheHitRate],),
            "mobile_scroll_frictions": ([AggregatedMobileScrollFriction],),
            "slow_fcp_high_bytes": ([AggregatedSlowFCPHighBytes],),
            "slow_interaction_long_tasks": ([AggregatedSlowInteractionLongTask],),
            "uncompressed_resources": ([AggregatedUncompressedResource],),
        }

    attribute_map = {
        "high_frozen_frame_rates": "high_frozen_frame_rates",
        "high_script_evaluations": "high_script_evaluations",
        "low_cache_hit_rates": "low_cache_hit_rates",
        "mobile_scroll_frictions": "mobile_scroll_frictions",
        "slow_fcp_high_bytes": "slow_fcp_high_bytes",
        "slow_interaction_long_tasks": "slow_interaction_long_tasks",
        "uncompressed_resources": "uncompressed_resources",
    }

    def __init__(
        self_,
        high_frozen_frame_rates: Union[List[AggregatedHighFrozenFrameRate], UnsetType] = unset,
        high_script_evaluations: Union[List[AggregatedHighScriptEval], UnsetType] = unset,
        low_cache_hit_rates: Union[List[AggregatedLowCacheHitRate], UnsetType] = unset,
        mobile_scroll_frictions: Union[List[AggregatedMobileScrollFriction], UnsetType] = unset,
        slow_fcp_high_bytes: Union[List[AggregatedSlowFCPHighBytes], UnsetType] = unset,
        slow_interaction_long_tasks: Union[List[AggregatedSlowInteractionLongTask], UnsetType] = unset,
        uncompressed_resources: Union[List[AggregatedUncompressedResource], UnsetType] = unset,
        **kwargs,
    ):
        """
        Grouped detection results by detection type.

        :param high_frozen_frame_rates: Detected high frozen frame rate issues.
        :type high_frozen_frame_rates: [AggregatedHighFrozenFrameRate], optional

        :param high_script_evaluations: Detected high script evaluation issues.
        :type high_script_evaluations: [AggregatedHighScriptEval], optional

        :param low_cache_hit_rates: Detected low cache hit rate issues.
        :type low_cache_hit_rates: [AggregatedLowCacheHitRate], optional

        :param mobile_scroll_frictions: Detected mobile scroll friction issues.
        :type mobile_scroll_frictions: [AggregatedMobileScrollFriction], optional

        :param slow_fcp_high_bytes: Detected slow first contentful paint with high byte count issues.
        :type slow_fcp_high_bytes: [AggregatedSlowFCPHighBytes], optional

        :param slow_interaction_long_tasks: Detected slow interaction with long task issues.
        :type slow_interaction_long_tasks: [AggregatedSlowInteractionLongTask], optional

        :param uncompressed_resources: Detected uncompressed resource issues.
        :type uncompressed_resources: [AggregatedUncompressedResource], optional
        """
        if high_frozen_frame_rates is not unset:
            kwargs["high_frozen_frame_rates"] = high_frozen_frame_rates
        if high_script_evaluations is not unset:
            kwargs["high_script_evaluations"] = high_script_evaluations
        if low_cache_hit_rates is not unset:
            kwargs["low_cache_hit_rates"] = low_cache_hit_rates
        if mobile_scroll_frictions is not unset:
            kwargs["mobile_scroll_frictions"] = mobile_scroll_frictions
        if slow_fcp_high_bytes is not unset:
            kwargs["slow_fcp_high_bytes"] = slow_fcp_high_bytes
        if slow_interaction_long_tasks is not unset:
            kwargs["slow_interaction_long_tasks"] = slow_interaction_long_tasks
        if uncompressed_resources is not unset:
            kwargs["uncompressed_resources"] = uncompressed_resources
        super().__init__(kwargs)
