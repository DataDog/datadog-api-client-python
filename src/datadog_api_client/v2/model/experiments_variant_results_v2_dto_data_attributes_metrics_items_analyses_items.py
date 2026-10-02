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
    from datadog_api_client.v2.model.experiments_variant_results_v2_dto_data_attributes_metrics_items_analyses_items_confidence_interval import (
        ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsConfidenceInterval,
    )
    from datadog_api_client.v2.model.experiments_variant_results_v2_dto_data_attributes_metrics_items_analyses_items_lift_type import (
        ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsLiftType,
    )
    from datadog_api_client.v2.model.experiments_variant_results_v2_dto_data_attributes_metrics_items_analyses_items_method import (
        ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsMethod,
    )
    from datadog_api_client.v2.model.experiments_variant_results_v2_dto_data_attributes_metrics_items_analyses_items_unreliable_reason import (
        ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsUnreliableReason,
    )


class ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_variant_results_v2_dto_data_attributes_metrics_items_analyses_items_confidence_interval import (
            ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsConfidenceInterval,
        )
        from datadog_api_client.v2.model.experiments_variant_results_v2_dto_data_attributes_metrics_items_analyses_items_lift_type import (
            ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsLiftType,
        )
        from datadog_api_client.v2.model.experiments_variant_results_v2_dto_data_attributes_metrics_items_analyses_items_method import (
            ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsMethod,
        )
        from datadog_api_client.v2.model.experiments_variant_results_v2_dto_data_attributes_metrics_items_analyses_items_unreliable_reason import (
            ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsUnreliableReason,
        )

        return {
            "confidence_interval": (
                ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsConfidenceInterval,
            ),
            "confidence_level": (float,),
            "evsi": (float,),
            "expectation_above_zero": (float,),
            "expectation_below_zero": (float,),
            "global_lift": (float,),
            "global_lift_lower_bound": (float,),
            "global_lift_upper_bound": (float,),
            "is_cuped_adjusted": (bool,),
            "is_unreliable": (bool,),
            "lift_type": (ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsLiftType,),
            "method": (ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsMethod,),
            "minimum_expected_regret": (float,),
            "p_value": (float,),
            "point_estimate": (float,),
            "probability_above_zero": (float,),
            "probability_below_zero": (float,),
            "standard_error": (float,),
            "unreliable_reason": (
                ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsUnreliableReason,
            ),
            "variant_metric_value": (float, none_type),
            "z_score": (float,),
        }

    attribute_map = {
        "confidence_interval": "confidence_interval",
        "confidence_level": "confidence_level",
        "evsi": "evsi",
        "expectation_above_zero": "expectation_above_zero",
        "expectation_below_zero": "expectation_below_zero",
        "global_lift": "global_lift",
        "global_lift_lower_bound": "global_lift_lower_bound",
        "global_lift_upper_bound": "global_lift_upper_bound",
        "is_cuped_adjusted": "is_cuped_adjusted",
        "is_unreliable": "is_unreliable",
        "lift_type": "lift_type",
        "method": "method",
        "minimum_expected_regret": "minimum_expected_regret",
        "p_value": "p_value",
        "point_estimate": "point_estimate",
        "probability_above_zero": "probability_above_zero",
        "probability_below_zero": "probability_below_zero",
        "standard_error": "standard_error",
        "unreliable_reason": "unreliable_reason",
        "variant_metric_value": "variant_metric_value",
        "z_score": "z_score",
    }

    def __init__(
        self_,
        confidence_interval: Union[
            ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsConfidenceInterval, UnsetType
        ] = unset,
        confidence_level: Union[float, UnsetType] = unset,
        evsi: Union[float, UnsetType] = unset,
        expectation_above_zero: Union[float, UnsetType] = unset,
        expectation_below_zero: Union[float, UnsetType] = unset,
        global_lift: Union[float, UnsetType] = unset,
        global_lift_lower_bound: Union[float, UnsetType] = unset,
        global_lift_upper_bound: Union[float, UnsetType] = unset,
        is_cuped_adjusted: Union[bool, UnsetType] = unset,
        is_unreliable: Union[bool, UnsetType] = unset,
        lift_type: Union[
            ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsLiftType, UnsetType
        ] = unset,
        method: Union[ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsMethod, UnsetType] = unset,
        minimum_expected_regret: Union[float, UnsetType] = unset,
        p_value: Union[float, UnsetType] = unset,
        point_estimate: Union[float, UnsetType] = unset,
        probability_above_zero: Union[float, UnsetType] = unset,
        probability_below_zero: Union[float, UnsetType] = unset,
        standard_error: Union[float, UnsetType] = unset,
        unreliable_reason: Union[
            ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsUnreliableReason, UnsetType
        ] = unset,
        variant_metric_value: Union[float, none_type, UnsetType] = unset,
        z_score: Union[float, UnsetType] = unset,
        **kwargs,
    ):
        """
        One statistical comparison for a metric and variant.

        :param confidence_interval: Lower and upper bounds of the reported statistical interval.
        :type confidence_interval: ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsConfidenceInterval, optional

        :param confidence_level: Configured nominal confidence level. Interval bounds can use an adjusted level for multiple testing or hybrid methods.
        :type confidence_level: float, optional

        :param evsi: Expected reduction in minimum expected regret from collecting more sample data.
        :type evsi: float, optional

        :param expectation_above_zero: Expected effect when the effect is positive.
        :type expectation_above_zero: float, optional

        :param expectation_below_zero: Expected effect when the effect is negative.
        :type expectation_below_zero: float, optional

        :param global_lift: Estimated lift across the population. Calculated as metric coverage multiplied by the experiment lift.
        :type global_lift: float, optional

        :param global_lift_lower_bound: Lower bound of the estimated lift across the population.
        :type global_lift_lower_bound: float, optional

        :param global_lift_upper_bound: Upper bound of the estimated lift across the population.
        :type global_lift_upper_bound: float, optional

        :param is_cuped_adjusted: Whether CUPED used pre-experiment data to reduce variance in this result.
        :type is_cuped_adjusted: bool, optional

        :param is_unreliable: Whether the statistical result is marked as unreliable.
        :type is_unreliable: bool, optional

        :param lift_type: Whether the reported lift is relative or absolute.
        :type lift_type: ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsLiftType, optional

        :param method: Statistical method used to calculate this result.
        :type method: ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsMethod, optional

        :param minimum_expected_regret: The smaller expected opportunity cost of choosing treatment or control.
        :type minimum_expected_regret: float, optional

        :param p_value: Probability, under the no-effect hypothesis, of a result at least as extreme as the observed result.
        :type p_value: float, optional

        :param point_estimate: Estimated difference between the variant and control for this metric.
        :type point_estimate: float, optional

        :param probability_above_zero: Estimated probability that the effect is greater than zero.
        :type probability_above_zero: float, optional

        :param probability_below_zero: Estimated probability that the effect is less than zero.
        :type probability_below_zero: float, optional

        :param standard_error: Estimated uncertainty in the effect estimate.
        :type standard_error: float, optional

        :param unreliable_reason: Reason that the statistical result is marked as unreliable.
        :type unreliable_reason: ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsUnreliableReason, optional

        :param variant_metric_value: Metric value calculated for this variant.
        :type variant_metric_value: float, none_type, optional

        :param z_score: Standardized statistic used to compare the observed effect with zero.
        :type z_score: float, optional
        """
        if confidence_interval is not unset:
            kwargs["confidence_interval"] = confidence_interval
        if confidence_level is not unset:
            kwargs["confidence_level"] = confidence_level
        if evsi is not unset:
            kwargs["evsi"] = evsi
        if expectation_above_zero is not unset:
            kwargs["expectation_above_zero"] = expectation_above_zero
        if expectation_below_zero is not unset:
            kwargs["expectation_below_zero"] = expectation_below_zero
        if global_lift is not unset:
            kwargs["global_lift"] = global_lift
        if global_lift_lower_bound is not unset:
            kwargs["global_lift_lower_bound"] = global_lift_lower_bound
        if global_lift_upper_bound is not unset:
            kwargs["global_lift_upper_bound"] = global_lift_upper_bound
        if is_cuped_adjusted is not unset:
            kwargs["is_cuped_adjusted"] = is_cuped_adjusted
        if is_unreliable is not unset:
            kwargs["is_unreliable"] = is_unreliable
        if lift_type is not unset:
            kwargs["lift_type"] = lift_type
        if method is not unset:
            kwargs["method"] = method
        if minimum_expected_regret is not unset:
            kwargs["minimum_expected_regret"] = minimum_expected_regret
        if p_value is not unset:
            kwargs["p_value"] = p_value
        if point_estimate is not unset:
            kwargs["point_estimate"] = point_estimate
        if probability_above_zero is not unset:
            kwargs["probability_above_zero"] = probability_above_zero
        if probability_below_zero is not unset:
            kwargs["probability_below_zero"] = probability_below_zero
        if standard_error is not unset:
            kwargs["standard_error"] = standard_error
        if unreliable_reason is not unset:
            kwargs["unreliable_reason"] = unreliable_reason
        if variant_metric_value is not unset:
            kwargs["variant_metric_value"] = variant_metric_value
        if z_score is not unset:
            kwargs["z_score"] = z_score
        super().__init__(kwargs)
