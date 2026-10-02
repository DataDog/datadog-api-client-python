# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_variant_results_v2_dto_data_attributes_metrics_items_analyses_items import (
        ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItems,
    )
    from datadog_api_client.v2.model.experiments_variant_results_v2_dto_data_attributes_metrics_items_coverage_summary import (
        ExperimentsVariantResultsV2DTODataAttributesMetricsItemsCoverageSummary,
    )
    from datadog_api_client.v2.model.experiments_metric_v2_dto_data_attributes_desired_change import (
        ExperimentsMetricV2DTODataAttributesDesiredChange,
    )


class ExperimentsVariantResultsV2DTODataAttributesMetricsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_variant_results_v2_dto_data_attributes_metrics_items_analyses_items import (
            ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItems,
        )
        from datadog_api_client.v2.model.experiments_variant_results_v2_dto_data_attributes_metrics_items_coverage_summary import (
            ExperimentsVariantResultsV2DTODataAttributesMetricsItemsCoverageSummary,
        )
        from datadog_api_client.v2.model.experiments_metric_v2_dto_data_attributes_desired_change import (
            ExperimentsMetricV2DTODataAttributesDesiredChange,
        )

        return {
            "analyses": ([ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItems],),
            "assignment_count": (int,),
            "coverage": (float,),
            "coverage_summary": (ExperimentsVariantResultsV2DTODataAttributesMetricsItemsCoverageSummary,),
            "coverage_unavailable_reason": (str,),
            "denominator": (float, none_type),
            "desired_change": (ExperimentsMetricV2DTODataAttributesDesiredChange,),
            "metric_id": (str,),
            "metric_name": (str,),
            "numerator": (float, none_type),
            "sub_metric_property_name": (str,),
            "sub_metric_property_value": (str,),
        }

    attribute_map = {
        "analyses": "analyses",
        "assignment_count": "assignment_count",
        "coverage": "coverage",
        "coverage_summary": "coverage_summary",
        "coverage_unavailable_reason": "coverage_unavailable_reason",
        "denominator": "denominator",
        "desired_change": "desired_change",
        "metric_id": "metric_id",
        "metric_name": "metric_name",
        "numerator": "numerator",
        "sub_metric_property_name": "sub_metric_property_name",
        "sub_metric_property_value": "sub_metric_property_value",
    }

    def __init__(
        self_,
        analyses: Union[List[ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItems], UnsetType] = unset,
        assignment_count: Union[int, UnsetType] = unset,
        coverage: Union[float, UnsetType] = unset,
        coverage_summary: Union[
            ExperimentsVariantResultsV2DTODataAttributesMetricsItemsCoverageSummary, UnsetType
        ] = unset,
        coverage_unavailable_reason: Union[str, UnsetType] = unset,
        denominator: Union[float, none_type, UnsetType] = unset,
        desired_change: Union[ExperimentsMetricV2DTODataAttributesDesiredChange, UnsetType] = unset,
        metric_id: Union[str, UnsetType] = unset,
        metric_name: Union[str, UnsetType] = unset,
        numerator: Union[float, none_type, UnsetType] = unset,
        sub_metric_property_name: Union[str, UnsetType] = unset,
        sub_metric_property_value: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Metric values and statistical results for one variant.

        :param analyses: Statistical analyses calculated for this metric and variant.
        :type analyses: [ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItems], optional

        :param assignment_count: Number of subjects assigned to this variant.
        :type assignment_count: int, optional

        :param coverage: Estimated share of the global metric total from the eligible population if that population received
            control. The estimate can exceed 1.
        :type coverage: float, optional

        :param coverage_summary: Population totals and allocation used to calculate metric coverage.
        :type coverage_summary: ExperimentsVariantResultsV2DTODataAttributesMetricsItemsCoverageSummary, optional

        :param coverage_unavailable_reason: Reason that metric coverage could not be calculated.
        :type coverage_unavailable_reason: str, optional

        :param denominator: Aggregated denominator value for this metric and variant.
        :type denominator: float, none_type, optional

        :param desired_change: Direction of metric change considered desirable.
        :type desired_change: ExperimentsMetricV2DTODataAttributesDesiredChange, optional

        :param metric_id: ID of the metric represented by this entry.
        :type metric_id: str, optional

        :param metric_name: Display name of the metric represented by this entry.
        :type metric_name: str, optional

        :param numerator: Aggregated numerator value for this metric and variant.
        :type numerator: float, none_type, optional

        :param sub_metric_property_name: Name of the property used to split this metric result.
        :type sub_metric_property_name: str, optional

        :param sub_metric_property_value: Property value represented by this split metric result.
        :type sub_metric_property_value: str, optional
        """
        if analyses is not unset:
            kwargs["analyses"] = analyses
        if assignment_count is not unset:
            kwargs["assignment_count"] = assignment_count
        if coverage is not unset:
            kwargs["coverage"] = coverage
        if coverage_summary is not unset:
            kwargs["coverage_summary"] = coverage_summary
        if coverage_unavailable_reason is not unset:
            kwargs["coverage_unavailable_reason"] = coverage_unavailable_reason
        if denominator is not unset:
            kwargs["denominator"] = denominator
        if desired_change is not unset:
            kwargs["desired_change"] = desired_change
        if metric_id is not unset:
            kwargs["metric_id"] = metric_id
        if metric_name is not unset:
            kwargs["metric_name"] = metric_name
        if numerator is not unset:
            kwargs["numerator"] = numerator
        if sub_metric_property_name is not unset:
            kwargs["sub_metric_property_name"] = sub_metric_property_name
        if sub_metric_property_value is not unset:
            kwargs["sub_metric_property_value"] = sub_metric_property_value
        super().__init__(kwargs)
