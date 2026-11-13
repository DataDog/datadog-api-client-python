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
    from datadog_api_client.v2.model.experiments_bandit_policy_v2 import ExperimentsBanditPolicyV2
    from datadog_api_client.v2.model.experiments_bandit_bayesian_prior_v2 import ExperimentsBanditBayesianPriorV2
    from datadog_api_client.v2.model.experiments_bandit_flag_configuration_v2 import (
        ExperimentsBanditFlagConfigurationV2,
    )
    from datadog_api_client.v2.model.experiments_bandit_refresh_v2 import ExperimentsBanditRefreshV2
    from datadog_api_client.v2.model.experiments_bandit_optimal_variant_unavailable_reason import (
        ExperimentsBanditOptimalVariantUnavailableReason,
    )
    from datadog_api_client.v2.model.experiments_bandit_scheduled_end_failure_v2 import (
        ExperimentsBanditScheduledEndFailureV2,
    )
    from datadog_api_client.v2.model.experiments_bandit_status import ExperimentsBanditStatus
    from datadog_api_client.v2.model.experiments_bandit_variant_v2 import ExperimentsBanditVariantV2


class ExperimentsBanditV2DTODataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_bandit_policy_v2 import ExperimentsBanditPolicyV2
        from datadog_api_client.v2.model.experiments_bandit_bayesian_prior_v2 import ExperimentsBanditBayesianPriorV2
        from datadog_api_client.v2.model.experiments_bandit_flag_configuration_v2 import (
            ExperimentsBanditFlagConfigurationV2,
        )
        from datadog_api_client.v2.model.experiments_bandit_refresh_v2 import ExperimentsBanditRefreshV2
        from datadog_api_client.v2.model.experiments_bandit_optimal_variant_unavailable_reason import (
            ExperimentsBanditOptimalVariantUnavailableReason,
        )
        from datadog_api_client.v2.model.experiments_bandit_scheduled_end_failure_v2 import (
            ExperimentsBanditScheduledEndFailureV2,
        )
        from datadog_api_client.v2.model.experiments_bandit_status import ExperimentsBanditStatus
        from datadog_api_client.v2.model.experiments_bandit_variant_v2 import ExperimentsBanditVariantV2

        return {
            "active_policy": (ExperimentsBanditPolicyV2,),
            "aggregation_window_seconds": (int,),
            "bayesian_prior": (ExperimentsBanditBayesianPriorV2,),
            "config_version": (int,),
            "created_at": (datetime,),
            "datadog_flag_configuration": (ExperimentsBanditFlagConfigurationV2,),
            "description": (str,),
            "ended_at": (datetime, none_type),
            "exposure_sql_model_id": (UUID, none_type),
            "latest_refresh": (ExperimentsBanditRefreshV2,),
            "lookback_seconds": (int,),
            "metric_id": (UUID, none_type),
            "name": (str,),
            "optimal_variant_key": (str, none_type),
            "optimal_variant_unavailable_reason": (ExperimentsBanditOptimalVariantUnavailableReason,),
            "refresh_schedule_id": (str, none_type),
            "scheduled_end_at": (datetime, none_type),
            "scheduled_end_failure": (ExperimentsBanditScheduledEndFailureV2,),
            "started_at": (datetime, none_type),
            "status": (ExperimentsBanditStatus,),
            "subject_type_id": (UUID, none_type),
            "tags": ([str],),
            "teams": ([str],),
            "updated_at": (datetime,),
            "variants": ([ExperimentsBanditVariantV2],),
            "warmup_seconds": (int, none_type),
        }

    attribute_map = {
        "active_policy": "active_policy",
        "aggregation_window_seconds": "aggregation_window_seconds",
        "bayesian_prior": "bayesian_prior",
        "config_version": "config_version",
        "created_at": "created_at",
        "datadog_flag_configuration": "datadog_flag_configuration",
        "description": "description",
        "ended_at": "ended_at",
        "exposure_sql_model_id": "exposure_sql_model_id",
        "latest_refresh": "latest_refresh",
        "lookback_seconds": "lookback_seconds",
        "metric_id": "metric_id",
        "name": "name",
        "optimal_variant_key": "optimal_variant_key",
        "optimal_variant_unavailable_reason": "optimal_variant_unavailable_reason",
        "refresh_schedule_id": "refresh_schedule_id",
        "scheduled_end_at": "scheduled_end_at",
        "scheduled_end_failure": "scheduled_end_failure",
        "started_at": "started_at",
        "status": "status",
        "subject_type_id": "subject_type_id",
        "tags": "tags",
        "teams": "teams",
        "updated_at": "updated_at",
        "variants": "variants",
        "warmup_seconds": "warmup_seconds",
    }

    def __init__(
        self_,
        active_policy: Union[ExperimentsBanditPolicyV2, none_type],
        aggregation_window_seconds: int,
        bayesian_prior: ExperimentsBanditBayesianPriorV2,
        config_version: int,
        created_at: datetime,
        description: str,
        ended_at: Union[datetime, none_type],
        exposure_sql_model_id: Union[UUID, none_type],
        latest_refresh: Union[ExperimentsBanditRefreshV2, none_type],
        lookback_seconds: int,
        metric_id: Union[UUID, none_type],
        name: str,
        optimal_variant_key: Union[str, none_type],
        refresh_schedule_id: Union[str, none_type],
        scheduled_end_at: Union[datetime, none_type],
        started_at: Union[datetime, none_type],
        status: ExperimentsBanditStatus,
        subject_type_id: Union[UUID, none_type],
        tags: List[str],
        teams: List[str],
        updated_at: datetime,
        variants: List[ExperimentsBanditVariantV2],
        warmup_seconds: Union[int, none_type],
        datadog_flag_configuration: Union[ExperimentsBanditFlagConfigurationV2, UnsetType] = unset,
        optimal_variant_unavailable_reason: Union[ExperimentsBanditOptimalVariantUnavailableReason, UnsetType] = unset,
        scheduled_end_failure: Union[ExperimentsBanditScheduledEndFailureV2, UnsetType] = unset,
        **kwargs,
    ):
        """
        A bandit's setup, the policy it serves, and its latest refresh.

        :param active_policy: The policy the bandit serves. Null until the bandit starts.
        :type active_policy: ExperimentsBanditPolicyV2, none_type

        :param aggregation_window_seconds: How long after an exposure its reward is counted, in seconds.
        :type aggregation_window_seconds: int

        :param bayesian_prior: The prior the bandit's estimates start from.
        :type bayesian_prior: ExperimentsBanditBayesianPriorV2

        :param config_version: The version of the bandit's configuration. Each saved change adds one.
        :type config_version: int

        :param created_at: When the bandit was created.
        :type created_at: datetime

        :param datadog_flag_configuration: The flag rule the bandit serves through. Absent until a draft is put on a flag, and when the caller lacks feature flag and environment read permissions ( ``meta.warnings`` then says so).
        :type datadog_flag_configuration: ExperimentsBanditFlagConfigurationV2, optional

        :param description: The bandit's description.
        :type description: str

        :param ended_at: When the bandit was stopped or reached its scheduled end. Null while it hasn't ended.
        :type ended_at: datetime, none_type

        :param exposure_sql_model_id: The exposure SQL model the bandit reads its exposures from. Null until set on a draft.
        :type exposure_sql_model_id: UUID, none_type

        :param latest_refresh: The most recently started refresh. Null until one starts.
        :type latest_refresh: ExperimentsBanditRefreshV2, none_type

        :param lookback_seconds: How far back each refresh reads observations, in seconds.
        :type lookback_seconds: int

        :param metric_id: The metric the bandit optimizes. Null until set on a draft.
        :type metric_id: UUID, none_type

        :param name: The bandit's name.
        :type name: str

        :param optimal_variant_key: The key of the arm most likely to be best, when one arm leads and the bandit is outside warmup. Null otherwise. Matches Get bandit results.
        :type optimal_variant_key: str, none_type

        :param optimal_variant_unavailable_reason: Why no optimal variant is reported. Absent when one is, or when the cause isn't known.
        :type optimal_variant_unavailable_reason: ExperimentsBanditOptimalVariantUnavailableReason, optional

        :param refresh_schedule_id: The schedule the bandit refreshes on.
        :type refresh_schedule_id: str, none_type

        :param scheduled_end_at: When the bandit ends and serves its fallback. Null when it has no scheduled end.
        :type scheduled_end_at: datetime, none_type

        :param scheduled_end_failure: Why the scheduled end couldn't run. It isn't retried until the end or fallback changes. Absent when there's no failure.
        :type scheduled_end_failure: ExperimentsBanditScheduledEndFailureV2, optional

        :param started_at: When the bandit started. Null until it starts.
        :type started_at: datetime, none_type

        :param status: The bandit's status. STOPPED means the bandit was stopped and serves the variant chosen then. COMPLETED means it reached its scheduled end and serves its fallback.
        :type status: ExperimentsBanditStatus

        :param subject_type_id: The subject type the bandit randomizes and measures by. Null until set on a draft.
        :type subject_type_id: UUID, none_type

        :param tags: The bandit's tags, without team tags.
        :type tags: [str]

        :param teams: Handles of the teams that own the bandit.
        :type teams: [str]

        :param updated_at: When the bandit was last changed.
        :type updated_at: datetime

        :param variants: The flag variants the bandit uses: its arms in arm order, then its fallback when the fallback isn't an arm.
        :type variants: [ExperimentsBanditVariantV2]

        :param warmup_seconds: How long after starting the bandit serves its arms equally, in seconds. Null when it has no warmup.
        :type warmup_seconds: int, none_type
        """
        if datadog_flag_configuration is not unset:
            kwargs["datadog_flag_configuration"] = datadog_flag_configuration
        if optimal_variant_unavailable_reason is not unset:
            kwargs["optimal_variant_unavailable_reason"] = optimal_variant_unavailable_reason
        if scheduled_end_failure is not unset:
            kwargs["scheduled_end_failure"] = scheduled_end_failure
        super().__init__(kwargs)

        self_.active_policy = active_policy
        self_.aggregation_window_seconds = aggregation_window_seconds
        self_.bayesian_prior = bayesian_prior
        self_.config_version = config_version
        self_.created_at = created_at
        self_.description = description
        self_.ended_at = ended_at
        self_.exposure_sql_model_id = exposure_sql_model_id
        self_.latest_refresh = latest_refresh
        self_.lookback_seconds = lookback_seconds
        self_.metric_id = metric_id
        self_.name = name
        self_.optimal_variant_key = optimal_variant_key
        self_.refresh_schedule_id = refresh_schedule_id
        self_.scheduled_end_at = scheduled_end_at
        self_.started_at = started_at
        self_.status = status
        self_.subject_type_id = subject_type_id
        self_.tags = tags
        self_.teams = teams
        self_.updated_at = updated_at
        self_.variants = variants
        self_.warmup_seconds = warmup_seconds
