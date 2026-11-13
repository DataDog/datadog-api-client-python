# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_bandit_desired_change import ExperimentsBanditDesiredChange
    from datadog_api_client.v2.model.experiments_bandit_optimal_variant_unavailable_reason import (
        ExperimentsBanditOptimalVariantUnavailableReason,
    )
    from datadog_api_client.v2.model.experiments_bandit_point_estimate_v2 import ExperimentsBanditPointEstimateV2
    from datadog_api_client.v2.model.experiments_bandit_results_state import ExperimentsBanditResultsState
    from datadog_api_client.v2.model.experiments_bandit_statistics_status import ExperimentsBanditStatisticsStatus
    from datadog_api_client.v2.model.experiments_bandit_variant_result_v2 import ExperimentsBanditVariantResultV2


class ExperimentsBanditResultsV2DTODataAttributes(ModelNormal):
    validations = {
        "confidence_level": {
            "inclusive_maximum": 1,
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_bandit_desired_change import ExperimentsBanditDesiredChange
        from datadog_api_client.v2.model.experiments_bandit_optimal_variant_unavailable_reason import (
            ExperimentsBanditOptimalVariantUnavailableReason,
        )
        from datadog_api_client.v2.model.experiments_bandit_point_estimate_v2 import ExperimentsBanditPointEstimateV2
        from datadog_api_client.v2.model.experiments_bandit_results_state import ExperimentsBanditResultsState
        from datadog_api_client.v2.model.experiments_bandit_statistics_status import ExperimentsBanditStatisticsStatus
        from datadog_api_client.v2.model.experiments_bandit_variant_result_v2 import ExperimentsBanditVariantResultV2

        return {
            "confidence_level": (float,),
            "config_version": (int, none_type),
            "data_as_of": (datetime, none_type),
            "desired_change": (ExperimentsBanditDesiredChange,),
            "next_refresh_at": (datetime, none_type),
            "optimal_variant_key": (str, none_type),
            "optimal_variant_unavailable_reason": (ExperimentsBanditOptimalVariantUnavailableReason,),
            "point_estimates": ([ExperimentsBanditPointEstimateV2],),
            "refresh_id": (UUID, none_type),
            "results_last_updated": (datetime, none_type),
            "state": (ExperimentsBanditResultsState,),
            "statistics_status": (ExperimentsBanditStatisticsStatus,),
            "variants": ([ExperimentsBanditVariantResultV2],),
        }

    attribute_map = {
        "confidence_level": "confidence_level",
        "config_version": "config_version",
        "data_as_of": "data_as_of",
        "desired_change": "desired_change",
        "next_refresh_at": "next_refresh_at",
        "optimal_variant_key": "optimal_variant_key",
        "optimal_variant_unavailable_reason": "optimal_variant_unavailable_reason",
        "point_estimates": "point_estimates",
        "refresh_id": "refresh_id",
        "results_last_updated": "results_last_updated",
        "state": "state",
        "statistics_status": "statistics_status",
        "variants": "variants",
    }

    def __init__(
        self_,
        confidence_level: float,
        config_version: Union[int, none_type],
        data_as_of: Union[datetime, none_type],
        desired_change: Union[ExperimentsBanditDesiredChange, none_type],
        next_refresh_at: Union[datetime, none_type],
        optimal_variant_key: Union[str, none_type],
        point_estimates: List[ExperimentsBanditPointEstimateV2],
        refresh_id: Union[UUID, none_type],
        results_last_updated: Union[datetime, none_type],
        state: ExperimentsBanditResultsState,
        variants: List[ExperimentsBanditVariantResultV2],
        optimal_variant_unavailable_reason: Union[ExperimentsBanditOptimalVariantUnavailableReason, UnsetType] = unset,
        statistics_status: Union[ExperimentsBanditStatisticsStatus, UnsetType] = unset,
        **kwargs,
    ):
        """
        What the bandit's refreshes have learned.

        :param confidence_level: The probability mass of each confidence interval.
        :type confidence_level: float

        :param config_version: The configuration version the latest saved refresh used. It can be older than the bandit's, because changes such as a new end date don't invalidate results.
        :type config_version: int, none_type

        :param data_as_of: The latest warehouse data the latest saved refresh read.
        :type data_as_of: datetime, none_type

        :param desired_change: The direction the bandit optimizes the metric in. It's fixed when the bandit starts. Null before the first saved refresh.
        :type desired_change: ExperimentsBanditDesiredChange, none_type

        :param next_refresh_at: An estimate of when the next scheduled refresh starts. Null when the bandit isn't running or the time can't be estimated. Only daily and hourly schedules get an estimate.
        :type next_refresh_at: datetime, none_type

        :param optimal_variant_key: The key of the arm most likely to be best, when one arm leads and the bandit is outside warmup. Null otherwise.
        :type optimal_variant_key: str, none_type

        :param optimal_variant_unavailable_reason: Why no optimal variant is reported. Absent when one is, or when the cause isn't known.
        :type optimal_variant_unavailable_reason: ExperimentsBanditOptimalVariantUnavailableReason, optional

        :param point_estimates: Each arm's point estimate from up to the latest 400 saved refreshes in the requested range, oldest first.
        :type point_estimates: [ExperimentsBanditPointEstimateV2]

        :param refresh_id: The latest refresh that saved results. The estimates come from it.
        :type refresh_id: UUID, none_type

        :param results_last_updated: When the latest saved refresh saved its results.
        :type results_last_updated: datetime, none_type

        :param state: WAITING_FOR_FIRST_REFRESH until a refresh saves results. STATS_UNAVAILABLE when the latest saved refresh has no complete probabilities of being optimal. ENDED once the bandit is stopped or completed; its last estimates stay. Otherwise WARMUP or OPTIMIZING says which policy the bandit serves. A paused bandit keeps its state.
        :type state: ExperimentsBanditResultsState

        :param statistics_status: Whether the latest saved refresh calculated its statistics. Absent for older refreshes.
        :type statistics_status: ExperimentsBanditStatisticsStatus, optional

        :param variants: One row per arm, in arm order.
        :type variants: [ExperimentsBanditVariantResultV2]
        """
        if optimal_variant_unavailable_reason is not unset:
            kwargs["optimal_variant_unavailable_reason"] = optimal_variant_unavailable_reason
        if statistics_status is not unset:
            kwargs["statistics_status"] = statistics_status
        super().__init__(kwargs)

        self_.confidence_level = confidence_level
        self_.config_version = config_version
        self_.data_as_of = data_as_of
        self_.desired_change = desired_change
        self_.next_refresh_at = next_refresh_at
        self_.optimal_variant_key = optimal_variant_key
        self_.point_estimates = point_estimates
        self_.refresh_id = refresh_id
        self_.results_last_updated = results_last_updated
        self_.state = state
        self_.variants = variants
