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
    from datadog_api_client.v2.model.experiments_create_metric_v2_request_data_attributes_desired_change import (
        ExperimentsCreateMetricV2RequestDataAttributesDesiredChange,
    )
    from datadog_api_client.v2.model.experiments_create_metric_v2_request_data_attributes_percentile_aggregation import (
        ExperimentsCreateMetricV2RequestDataAttributesPercentileAggregation,
    )
    from datadog_api_client.v2.model.experiments_warehouse_percentile_aggregation_input import (
        ExperimentsWarehousePercentileAggregationInput,
    )
    from datadog_api_client.v2.model.experiments_datadog_percentile_aggregation_input import (
        ExperimentsDatadogPercentileAggregationInput,
    )


class ExperimentsCreateMetricPercentileAttributes(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_create_metric_v2_request_data_attributes_data_source_type import (
            ExperimentsCreateMetricV2RequestDataAttributesDataSourceType,
        )
        from datadog_api_client.v2.model.experiments_create_metric_v2_request_data_attributes_desired_change import (
            ExperimentsCreateMetricV2RequestDataAttributesDesiredChange,
        )
        from datadog_api_client.v2.model.experiments_create_metric_v2_request_data_attributes_percentile_aggregation import (
            ExperimentsCreateMetricV2RequestDataAttributesPercentileAggregation,
        )

        return {
            "data_source_type": (ExperimentsCreateMetricV2RequestDataAttributesDataSourceType,),
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
            "percentile_aggregation": (ExperimentsCreateMetricV2RequestDataAttributesPercentileAggregation,),
        }

    attribute_map = {
        "data_source_type": "data_source_type",
        "description": "description",
        "desired_change": "desired_change",
        "format_as_percent": "format_as_percent",
        "guardrail_cutoff_threshold": "guardrail_cutoff_threshold",
        "migration_metadata": "migration_metadata",
        "name": "name",
        "percentile_aggregation": "percentile_aggregation",
    }

    def __init__(
        self_,
        data_source_type: ExperimentsCreateMetricV2RequestDataAttributesDataSourceType,
        desired_change: ExperimentsCreateMetricV2RequestDataAttributesDesiredChange,
        name: str,
        percentile_aggregation: Union[
            ExperimentsCreateMetricV2RequestDataAttributesPercentileAggregation,
            ExperimentsWarehousePercentileAggregationInput,
            ExperimentsDatadogPercentileAggregationInput,
        ],
        description: Union[str, none_type, UnsetType] = unset,
        format_as_percent: Union[bool, UnsetType] = unset,
        guardrail_cutoff_threshold: Union[float, none_type, UnsetType] = unset,
        migration_metadata: Union[Any, UnsetType] = unset,
        **kwargs,
    ):
        """
        Configuration for a percentile metric. Omit numerator_aggregation and denominator_aggregation.

        :param data_source_type: Source of the data backing this metric.
        :type data_source_type: ExperimentsCreateMetricV2RequestDataAttributesDataSourceType

        :param description: Description of the metric. Send null to leave it unset.
        :type description: str, none_type, optional

        :param desired_change: Direction of change that represents an improvement for this metric.
        :type desired_change: ExperimentsCreateMetricV2RequestDataAttributesDesiredChange

        :param format_as_percent: Whether results render as a percentage. Defaults to false when omitted.
        :type format_as_percent: bool, optional

        :param guardrail_cutoff_threshold: Guardrail cutoff threshold. Send null to leave it unset.
        :type guardrail_cutoff_threshold: float, none_type, optional

        :param migration_metadata: Metadata associated with migration of this resource.
        :type migration_metadata: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param name: Name of the metric.
        :type name: str

        :param percentile_aggregation: Measure and percentile to calculate for the metric. Supply exactly one non-null measure.
        :type percentile_aggregation: ExperimentsCreateMetricV2RequestDataAttributesPercentileAggregation
        """
        if description is not unset:
            kwargs["description"] = description
        if format_as_percent is not unset:
            kwargs["format_as_percent"] = format_as_percent
        if guardrail_cutoff_threshold is not unset:
            kwargs["guardrail_cutoff_threshold"] = guardrail_cutoff_threshold
        if migration_metadata is not unset:
            kwargs["migration_metadata"] = migration_metadata
        super().__init__(kwargs)

        self_.data_source_type = data_source_type
        self_.desired_change = desired_change
        self_.name = name
        self_.percentile_aggregation = percentile_aggregation
