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
    from datadog_api_client.v2.model.experiments_bandit_bayesian_prior_input_v2 import (
        ExperimentsBanditBayesianPriorInputV2,
    )
    from datadog_api_client.v2.model.experiments_bandit_flag_configuration_input_v2 import (
        ExperimentsBanditFlagConfigurationInputV2,
    )
    from datadog_api_client.v2.model.experiments_bandit_variant_input_v2 import ExperimentsBanditVariantInputV2


class ExperimentsCreateBanditV2RequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_bandit_bayesian_prior_input_v2 import (
            ExperimentsBanditBayesianPriorInputV2,
        )
        from datadog_api_client.v2.model.experiments_bandit_flag_configuration_input_v2 import (
            ExperimentsBanditFlagConfigurationInputV2,
        )
        from datadog_api_client.v2.model.experiments_bandit_variant_input_v2 import ExperimentsBanditVariantInputV2

        return {
            "aggregation_window_seconds": (int,),
            "bayesian_prior": (ExperimentsBanditBayesianPriorInputV2,),
            "datadog_flag_configuration": (ExperimentsBanditFlagConfigurationInputV2,),
            "description": (str,),
            "exposure_sql_model_id": (UUID,),
            "lookback_seconds": (int,),
            "metric_id": (UUID,),
            "name": (str,),
            "refresh_schedule_id": (str,),
            "scheduled_end_at": (datetime,),
            "subject_type_id": (UUID,),
            "tags": ([str],),
            "teams": ([str],),
            "variants": ([ExperimentsBanditVariantInputV2],),
            "warmup_seconds": (int,),
        }

    attribute_map = {
        "aggregation_window_seconds": "aggregation_window_seconds",
        "bayesian_prior": "bayesian_prior",
        "datadog_flag_configuration": "datadog_flag_configuration",
        "description": "description",
        "exposure_sql_model_id": "exposure_sql_model_id",
        "lookback_seconds": "lookback_seconds",
        "metric_id": "metric_id",
        "name": "name",
        "refresh_schedule_id": "refresh_schedule_id",
        "scheduled_end_at": "scheduled_end_at",
        "subject_type_id": "subject_type_id",
        "tags": "tags",
        "teams": "teams",
        "variants": "variants",
        "warmup_seconds": "warmup_seconds",
    }

    def __init__(
        self_,
        name: str,
        aggregation_window_seconds: Union[int, UnsetType] = unset,
        bayesian_prior: Union[ExperimentsBanditBayesianPriorInputV2, UnsetType] = unset,
        datadog_flag_configuration: Union[ExperimentsBanditFlagConfigurationInputV2, none_type, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        exposure_sql_model_id: Union[UUID, UnsetType] = unset,
        lookback_seconds: Union[int, UnsetType] = unset,
        metric_id: Union[UUID, UnsetType] = unset,
        refresh_schedule_id: Union[str, UnsetType] = unset,
        scheduled_end_at: Union[datetime, UnsetType] = unset,
        subject_type_id: Union[UUID, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        teams: Union[List[str], UnsetType] = unset,
        variants: Union[List[ExperimentsBanditVariantInputV2], UnsetType] = unset,
        warmup_seconds: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        The new draft's setup. Only ``name`` is required. Whether the draft is ready to run is checked when it starts.

        :param aggregation_window_seconds: The aggregation window: how long after an exposure the bandit keeps counting its reward, in seconds. Defaults to 3600 (1 hour).
        :type aggregation_window_seconds: int, optional

        :param bayesian_prior: The prior the bandit's estimates start from, in the metric's units. Omitted fields keep their current values, or their defaults on create. A change takes effect on the next refresh.
        :type bayesian_prior: ExperimentsBanditBayesianPriorInputV2, optional

        :param datadog_flag_configuration: The flag and environment the bandit serves on, and who it serves there. The server chooses the rule's ``allocation_key``. On create, ``feature_flag_id`` and ``environment_id`` are required, and ``null`` is the same as omitting it. On update, omitted fields are unchanged, and ``null`` takes a draft off its flag, which also clears its variants and scheduled end. Moving a draft to another flag clears its variants unless the request sets them. Only a draft can change it.
        :type datadog_flag_configuration: ExperimentsBanditFlagConfigurationInputV2, none_type, optional

        :param description: The bandit's description. Defaults to empty.
        :type description: str, optional

        :param exposure_sql_model_id: The exposure SQL model the bandit reads its exposures from.
        :type exposure_sql_model_id: UUID, optional

        :param lookback_seconds: How far back each refresh reads observations, in seconds. Defaults to 2592000 (30 days).
        :type lookback_seconds: int, optional

        :param metric_id: The metric the bandit optimizes. It must read a warehouse metric source.
        :type metric_id: UUID, optional

        :param name: The bandit's name.
        :type name: str

        :param refresh_schedule_id: The schedule the bandit refreshes on. Defaults to the organization's default schedule.
        :type refresh_schedule_id: str, optional

        :param scheduled_end_at: When the bandit ends and serves its fallback. Needs a fallback variant.
        :type scheduled_end_at: datetime, optional

        :param subject_type_id: The subject type the bandit randomizes and measures by.
        :type subject_type_id: UUID, optional

        :param tags: Tags for the bandit. The flag's tags are added too.
        :type tags: [str], optional

        :param teams: Handles of the teams that own the bandit.
        :type teams: [str], optional

        :param variants: The flag variants the bandit uses. Needs ``datadog_flag_configuration``. The server fills in each variant's ``key`` and ``name`` from the flag.
        :type variants: [ExperimentsBanditVariantInputV2], optional

        :param warmup_seconds: How long the bandit serves its arms equally after it starts, in seconds. Defaults to no warmup.
        :type warmup_seconds: int, optional
        """
        if aggregation_window_seconds is not unset:
            kwargs["aggregation_window_seconds"] = aggregation_window_seconds
        if bayesian_prior is not unset:
            kwargs["bayesian_prior"] = bayesian_prior
        if datadog_flag_configuration is not unset:
            kwargs["datadog_flag_configuration"] = datadog_flag_configuration
        if description is not unset:
            kwargs["description"] = description
        if exposure_sql_model_id is not unset:
            kwargs["exposure_sql_model_id"] = exposure_sql_model_id
        if lookback_seconds is not unset:
            kwargs["lookback_seconds"] = lookback_seconds
        if metric_id is not unset:
            kwargs["metric_id"] = metric_id
        if refresh_schedule_id is not unset:
            kwargs["refresh_schedule_id"] = refresh_schedule_id
        if scheduled_end_at is not unset:
            kwargs["scheduled_end_at"] = scheduled_end_at
        if subject_type_id is not unset:
            kwargs["subject_type_id"] = subject_type_id
        if tags is not unset:
            kwargs["tags"] = tags
        if teams is not unset:
            kwargs["teams"] = teams
        if variants is not unset:
            kwargs["variants"] = variants
        if warmup_seconds is not unset:
            kwargs["warmup_seconds"] = warmup_seconds
        super().__init__(kwargs)

        self_.name = name
