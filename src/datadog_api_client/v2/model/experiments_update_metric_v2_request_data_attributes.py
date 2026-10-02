# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_create_metric_v2_request_data_attributes_data_source_type import (
        ExperimentsCreateMetricV2RequestDataAttributesDataSourceType,
    )
    from datadog_api_client.v2.model.experiments_create_metric_v2_request_data_attributes_numerator_aggregation import (
        ExperimentsCreateMetricV2RequestDataAttributesNumeratorAggregation,
    )
    from datadog_api_client.v2.model.experiments_create_metric_v2_request_data_attributes_desired_change import (
        ExperimentsCreateMetricV2RequestDataAttributesDesiredChange,
    )
    from datadog_api_client.v2.model.experiments_create_metric_v2_request_data_attributes_percentile_aggregation import (
        ExperimentsCreateMetricV2RequestDataAttributesPercentileAggregation,
    )
    from datadog_api_client.v2.model.experiments_warehouse_metric_aggregation_input import (
        ExperimentsWarehouseMetricAggregationInput,
    )
    from datadog_api_client.v2.model.experiments_datadog_metric_aggregation_input import (
        ExperimentsDatadogMetricAggregationInput,
    )
    from datadog_api_client.v2.model.experiments_warehouse_percentile_aggregation_input import (
        ExperimentsWarehousePercentileAggregationInput,
    )
    from datadog_api_client.v2.model.experiments_datadog_percentile_aggregation_input import (
        ExperimentsDatadogPercentileAggregationInput,
    )


class ExperimentsUpdateMetricV2RequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_create_metric_v2_request_data_attributes_data_source_type import (
            ExperimentsCreateMetricV2RequestDataAttributesDataSourceType,
        )
        from datadog_api_client.v2.model.experiments_create_metric_v2_request_data_attributes_numerator_aggregation import (
            ExperimentsCreateMetricV2RequestDataAttributesNumeratorAggregation,
        )
        from datadog_api_client.v2.model.experiments_create_metric_v2_request_data_attributes_desired_change import (
            ExperimentsCreateMetricV2RequestDataAttributesDesiredChange,
        )
        from datadog_api_client.v2.model.experiments_create_metric_v2_request_data_attributes_percentile_aggregation import (
            ExperimentsCreateMetricV2RequestDataAttributesPercentileAggregation,
        )

        return {
            "data_source_type": (ExperimentsCreateMetricV2RequestDataAttributesDataSourceType,),
            "denominator_aggregation": (ExperimentsCreateMetricV2RequestDataAttributesNumeratorAggregation,),
            "description": (str, none_type),
            "desired_change": (ExperimentsCreateMetricV2RequestDataAttributesDesiredChange,),
            "format_as_percent": (bool,),
            "guardrail_cutoff_threshold": (float, none_type),
            "migration_metadata": (
                bool,
                date,
                datetime,
                dict,
                float,
                int,
                list,
                str,
                UUID,
                none_type,
            ),
            "name": (str,),
            "numerator_aggregation": (ExperimentsCreateMetricV2RequestDataAttributesNumeratorAggregation,),
            "percentile_aggregation": (ExperimentsCreateMetricV2RequestDataAttributesPercentileAggregation,),
        }

    attribute_map = {
        "data_source_type": "data_source_type",
        "denominator_aggregation": "denominator_aggregation",
        "description": "description",
        "desired_change": "desired_change",
        "format_as_percent": "format_as_percent",
        "guardrail_cutoff_threshold": "guardrail_cutoff_threshold",
        "migration_metadata": "migration_metadata",
        "name": "name",
        "numerator_aggregation": "numerator_aggregation",
        "percentile_aggregation": "percentile_aggregation",
    }

    def __init__(
        self_,
        data_source_type: Union[ExperimentsCreateMetricV2RequestDataAttributesDataSourceType, UnsetType] = unset,
        denominator_aggregation: Union[
            ExperimentsCreateMetricV2RequestDataAttributesNumeratorAggregation,
            ExperimentsWarehouseMetricAggregationInput,
            ExperimentsDatadogMetricAggregationInput,
            UnsetType,
        ] = unset,
        description: Union[str, none_type, UnsetType] = unset,
        desired_change: Union[ExperimentsCreateMetricV2RequestDataAttributesDesiredChange, UnsetType] = unset,
        format_as_percent: Union[bool, UnsetType] = unset,
        guardrail_cutoff_threshold: Union[float, none_type, UnsetType] = unset,
        migration_metadata: Union[Any, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        numerator_aggregation: Union[
            ExperimentsCreateMetricV2RequestDataAttributesNumeratorAggregation,
            ExperimentsWarehouseMetricAggregationInput,
            ExperimentsDatadogMetricAggregationInput,
            UnsetType,
        ] = unset,
        percentile_aggregation: Union[
            ExperimentsCreateMetricV2RequestDataAttributesPercentileAggregation,
            ExperimentsWarehousePercentileAggregationInput,
            ExperimentsDatadogPercentileAggregationInput,
            UnsetType,
        ] = unset,
        **kwargs,
    ):
        """
        Fields supplied to update the metric. Every attribute is optional; omit an attribute to leave it unchanged.

        :param data_source_type: Source of the data backing this metric.
        :type data_source_type: ExperimentsCreateMetricV2RequestDataAttributesDataSourceType, optional

        :param denominator_aggregation: Measure and calculation settings for a numerator or denominator aggregation. Supply exactly one non-null measure.
        :type denominator_aggregation: ExperimentsCreateMetricV2RequestDataAttributesNumeratorAggregation, optional

        :param description: Send null to clear the description. Omit to leave it unchanged.
        :type description: str, none_type, optional

        :param desired_change: Direction of change that represents an improvement for this metric.
        :type desired_change: ExperimentsCreateMetricV2RequestDataAttributesDesiredChange, optional

        :param format_as_percent: Whether results render as a percentage. Omit to leave it unchanged.
        :type format_as_percent: bool, optional

        :param guardrail_cutoff_threshold: Send null to clear a stored threshold. Omit to leave it unchanged.
        :type guardrail_cutoff_threshold: float, none_type, optional

        :param migration_metadata: Metadata retained for resources imported from another system.
        :type migration_metadata: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param name: Name of the metric. Omit to leave it unchanged.
        :type name: str, optional

        :param numerator_aggregation: Measure and calculation settings for a numerator or denominator aggregation. Supply exactly one non-null measure.
        :type numerator_aggregation: ExperimentsCreateMetricV2RequestDataAttributesNumeratorAggregation, optional

        :param percentile_aggregation: Measure and percentile to calculate for the metric. Supply exactly one non-null measure.
        :type percentile_aggregation: ExperimentsCreateMetricV2RequestDataAttributesPercentileAggregation, optional
        """
        if data_source_type is not unset:
            kwargs["data_source_type"] = data_source_type
        if denominator_aggregation is not unset:
            kwargs["denominator_aggregation"] = denominator_aggregation
        if description is not unset:
            kwargs["description"] = description
        if desired_change is not unset:
            kwargs["desired_change"] = desired_change
        if format_as_percent is not unset:
            kwargs["format_as_percent"] = format_as_percent
        if guardrail_cutoff_threshold is not unset:
            kwargs["guardrail_cutoff_threshold"] = guardrail_cutoff_threshold
        if migration_metadata is not unset:
            kwargs["migration_metadata"] = migration_metadata
        if name is not unset:
            kwargs["name"] = name
        if numerator_aggregation is not unset:
            kwargs["numerator_aggregation"] = numerator_aggregation
        if percentile_aggregation is not unset:
            kwargs["percentile_aggregation"] = percentile_aggregation
        super().__init__(kwargs)
