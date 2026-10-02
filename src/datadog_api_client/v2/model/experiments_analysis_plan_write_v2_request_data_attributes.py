# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_analysis_plan_write_v2_request_data_attributes_bayesian_prior import (
        ExperimentsAnalysisPlanWriteV2RequestDataAttributesBayesianPrior,
    )
    from datadog_api_client.v2.model.experiments_analysis_plan_v2_dto_data_attributes_confidence_interval_method import (
        ExperimentsAnalysisPlanV2DTODataAttributesConfidenceIntervalMethod,
    )


class ExperimentsAnalysisPlanWriteV2RequestDataAttributes(ModelNormal):
    validations = {
        "cuped_lookback_period_days": {
            "inclusive_maximum": 30,
            "inclusive_minimum": 30,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_analysis_plan_write_v2_request_data_attributes_bayesian_prior import (
            ExperimentsAnalysisPlanWriteV2RequestDataAttributesBayesianPrior,
        )
        from datadog_api_client.v2.model.experiments_analysis_plan_v2_dto_data_attributes_confidence_interval_method import (
            ExperimentsAnalysisPlanV2DTODataAttributesConfidenceIntervalMethod,
        )

        return {
            "bayesian_prior": (ExperimentsAnalysisPlanWriteV2RequestDataAttributesBayesianPrior,),
            "confidence_interval_method": (ExperimentsAnalysisPlanV2DTODataAttributesConfidenceIntervalMethod,),
            "confidence_level": (float,),
            "cuped_lookback_period_days": (int,),
            "experiment_auto_end_days": (int,),
            "experiment_min_duration": (int,),
            "experiment_min_sample_size": (int,),
            "is_cuped_enabled": (bool,),
            "is_multiple_testing_correction_enabled": (bool,),
            "preferential_bonferroni_primary_metric_weight": (float,),
            "target_duration_days": (int, none_type),
        }

    attribute_map = {
        "bayesian_prior": "bayesian_prior",
        "confidence_interval_method": "confidence_interval_method",
        "confidence_level": "confidence_level",
        "cuped_lookback_period_days": "cuped_lookback_period_days",
        "experiment_auto_end_days": "experiment_auto_end_days",
        "experiment_min_duration": "experiment_min_duration",
        "experiment_min_sample_size": "experiment_min_sample_size",
        "is_cuped_enabled": "is_cuped_enabled",
        "is_multiple_testing_correction_enabled": "is_multiple_testing_correction_enabled",
        "preferential_bonferroni_primary_metric_weight": "preferential_bonferroni_primary_metric_weight",
        "target_duration_days": "target_duration_days",
    }

    def __init__(
        self_,
        bayesian_prior: Union[ExperimentsAnalysisPlanWriteV2RequestDataAttributesBayesianPrior, UnsetType] = unset,
        confidence_interval_method: Union[
            ExperimentsAnalysisPlanV2DTODataAttributesConfidenceIntervalMethod, UnsetType
        ] = unset,
        confidence_level: Union[float, UnsetType] = unset,
        cuped_lookback_period_days: Union[int, UnsetType] = unset,
        experiment_auto_end_days: Union[int, UnsetType] = unset,
        experiment_min_duration: Union[int, UnsetType] = unset,
        experiment_min_sample_size: Union[int, UnsetType] = unset,
        is_cuped_enabled: Union[bool, UnsetType] = unset,
        is_multiple_testing_correction_enabled: Union[bool, UnsetType] = unset,
        preferential_bonferroni_primary_metric_weight: Union[float, UnsetType] = unset,
        target_duration_days: Union[int, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Statistical settings and duration targets to apply to the experiment.

        :param bayesian_prior: Parameters of the prior distribution to use for Bayesian analysis.
        :type bayesian_prior: ExperimentsAnalysisPlanWriteV2RequestDataAttributesBayesianPrior, optional

        :param confidence_interval_method: Statistical method used to calculate the experiment results.
        :type confidence_interval_method: ExperimentsAnalysisPlanV2DTODataAttributesConfidenceIntervalMethod, optional

        :param confidence_level: Confidence level used for statistical analysis, expressed as a fraction.
        :type confidence_level: float, optional

        :param cuped_lookback_period_days: Only a 30-day CUPED lookback is supported.
        :type cuped_lookback_period_days: int, optional

        :param experiment_auto_end_days: Number of days configured for the experiment to end automatically.
        :type experiment_auto_end_days: int, optional

        :param experiment_min_duration: Minimum experiment duration in days configured in the analysis plan.
        :type experiment_min_duration: int, optional

        :param experiment_min_sample_size: Minimum sample size configured in the analysis plan.
        :type experiment_min_sample_size: int, optional

        :param is_cuped_enabled: Whether CUPED uses pre-experiment data to reduce variance in the analysis.
        :type is_cuped_enabled: bool, optional

        :param is_multiple_testing_correction_enabled: Whether the analysis adjusts for testing multiple hypotheses.
        :type is_multiple_testing_correction_enabled: bool, optional

        :param preferential_bonferroni_primary_metric_weight: Weight assigned to the primary metric in the preferential Bonferroni correction.
        :type preferential_bonferroni_primary_metric_weight: float, optional

        :param target_duration_days: Planned experiment duration in days.
        :type target_duration_days: int, none_type, optional
        """
        if bayesian_prior is not unset:
            kwargs["bayesian_prior"] = bayesian_prior
        if confidence_interval_method is not unset:
            kwargs["confidence_interval_method"] = confidence_interval_method
        if confidence_level is not unset:
            kwargs["confidence_level"] = confidence_level
        if cuped_lookback_period_days is not unset:
            kwargs["cuped_lookback_period_days"] = cuped_lookback_period_days
        if experiment_auto_end_days is not unset:
            kwargs["experiment_auto_end_days"] = experiment_auto_end_days
        if experiment_min_duration is not unset:
            kwargs["experiment_min_duration"] = experiment_min_duration
        if experiment_min_sample_size is not unset:
            kwargs["experiment_min_sample_size"] = experiment_min_sample_size
        if is_cuped_enabled is not unset:
            kwargs["is_cuped_enabled"] = is_cuped_enabled
        if is_multiple_testing_correction_enabled is not unset:
            kwargs["is_multiple_testing_correction_enabled"] = is_multiple_testing_correction_enabled
        if preferential_bonferroni_primary_metric_weight is not unset:
            kwargs["preferential_bonferroni_primary_metric_weight"] = preferential_bonferroni_primary_metric_weight
        if target_duration_days is not unset:
            kwargs["target_duration_days"] = target_duration_days
        super().__init__(kwargs)
