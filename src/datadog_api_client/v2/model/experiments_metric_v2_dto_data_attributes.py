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
    from datadog_api_client.v2.model.experiments_metric_v2_dto_data_attributes_data_source_type import (
        ExperimentsMetricV2DTODataAttributesDataSourceType,
    )
    from datadog_api_client.v2.model.experiments_metric_v2_dto_data_attributes_numerator_aggregation import (
        ExperimentsMetricV2DTODataAttributesNumeratorAggregation,
    )
    from datadog_api_client.v2.model.experiments_metric_v2_dto_data_attributes_desired_change import (
        ExperimentsMetricV2DTODataAttributesDesiredChange,
    )
    from datadog_api_client.v2.model.experiments_metric_v2_dto_data_attributes_metric_type import (
        ExperimentsMetricV2DTODataAttributesMetricType,
    )
    from datadog_api_client.v2.model.experiments_metric_v2_dto_data_attributes_percentile_aggregation import (
        ExperimentsMetricV2DTODataAttributesPercentileAggregation,
    )


class ExperimentsMetricV2DTODataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_metric_v2_dto_data_attributes_data_source_type import (
            ExperimentsMetricV2DTODataAttributesDataSourceType,
        )
        from datadog_api_client.v2.model.experiments_metric_v2_dto_data_attributes_numerator_aggregation import (
            ExperimentsMetricV2DTODataAttributesNumeratorAggregation,
        )
        from datadog_api_client.v2.model.experiments_metric_v2_dto_data_attributes_desired_change import (
            ExperimentsMetricV2DTODataAttributesDesiredChange,
        )
        from datadog_api_client.v2.model.experiments_metric_v2_dto_data_attributes_metric_type import (
            ExperimentsMetricV2DTODataAttributesMetricType,
        )
        from datadog_api_client.v2.model.experiments_metric_v2_dto_data_attributes_percentile_aggregation import (
            ExperimentsMetricV2DTODataAttributesPercentileAggregation,
        )

        return {
            "certified_at": (datetime, none_type),
            "created_at": (datetime,),
            "data_source_type": (ExperimentsMetricV2DTODataAttributesDataSourceType,),
            "denominator_aggregation": (ExperimentsMetricV2DTODataAttributesNumeratorAggregation,),
            "description": (str,),
            "desired_change": (ExperimentsMetricV2DTODataAttributesDesiredChange,),
            "experiment_count": (int, none_type),
            "format_as_percent": (bool,),
            "guardrail_cutoff_threshold": (float, none_type),
            "metric_type": (ExperimentsMetricV2DTODataAttributesMetricType,),
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
            "numerator_aggregation": (ExperimentsMetricV2DTODataAttributesNumeratorAggregation,),
            "percentile_aggregation": (ExperimentsMetricV2DTODataAttributesPercentileAggregation,),
            "reference_url": (str,),
            "updated_at": (datetime,),
        }

    attribute_map = {
        "certified_at": "certified_at",
        "created_at": "created_at",
        "data_source_type": "data_source_type",
        "denominator_aggregation": "denominator_aggregation",
        "description": "description",
        "desired_change": "desired_change",
        "experiment_count": "experiment_count",
        "format_as_percent": "format_as_percent",
        "guardrail_cutoff_threshold": "guardrail_cutoff_threshold",
        "metric_type": "metric_type",
        "migration_metadata": "migration_metadata",
        "name": "name",
        "numerator_aggregation": "numerator_aggregation",
        "percentile_aggregation": "percentile_aggregation",
        "reference_url": "reference_url",
        "updated_at": "updated_at",
    }

    def __init__(
        self_,
        certified_at: Union[datetime, none_type, UnsetType] = unset,
        created_at: Union[datetime, UnsetType] = unset,
        data_source_type: Union[ExperimentsMetricV2DTODataAttributesDataSourceType, UnsetType] = unset,
        denominator_aggregation: Union[
            ExperimentsMetricV2DTODataAttributesNumeratorAggregation, none_type, UnsetType
        ] = unset,
        description: Union[str, UnsetType] = unset,
        desired_change: Union[ExperimentsMetricV2DTODataAttributesDesiredChange, UnsetType] = unset,
        experiment_count: Union[int, none_type, UnsetType] = unset,
        format_as_percent: Union[bool, UnsetType] = unset,
        guardrail_cutoff_threshold: Union[float, none_type, UnsetType] = unset,
        metric_type: Union[ExperimentsMetricV2DTODataAttributesMetricType, UnsetType] = unset,
        migration_metadata: Union[Any, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        numerator_aggregation: Union[
            ExperimentsMetricV2DTODataAttributesNumeratorAggregation, none_type, UnsetType
        ] = unset,
        percentile_aggregation: Union[
            ExperimentsMetricV2DTODataAttributesPercentileAggregation, none_type, UnsetType
        ] = unset,
        reference_url: Union[str, UnsetType] = unset,
        updated_at: Union[datetime, UnsetType] = unset,
        **kwargs,
    ):
        """
        Details of the metric.

        :param certified_at: Time when this resource was certified.
        :type certified_at: datetime, none_type, optional

        :param created_at: Time when this resource was created.
        :type created_at: datetime, optional

        :param data_source_type: Source of the data used to calculate the metric.
        :type data_source_type: ExperimentsMetricV2DTODataAttributesDataSourceType, optional

        :param denominator_aggregation: Source measure and aggregation settings for a metric value.
        :type denominator_aggregation: ExperimentsMetricV2DTODataAttributesNumeratorAggregation, none_type, optional

        :param description: Text that explains the metric.
        :type description: str, optional

        :param desired_change: Direction of metric change considered desirable.
        :type desired_change: ExperimentsMetricV2DTODataAttributesDesiredChange, optional

        :param experiment_count: Number of experiments that reference this resource.
        :type experiment_count: int, none_type, optional

        :param format_as_percent: Whether to display the metric value as a percentage.
        :type format_as_percent: bool, optional

        :param guardrail_cutoff_threshold: Threshold used when evaluating this metric as a guardrail.
        :type guardrail_cutoff_threshold: float, none_type, optional

        :param metric_type: Type of metric calculation.
        :type metric_type: ExperimentsMetricV2DTODataAttributesMetricType, optional

        :param migration_metadata: Metadata retained for resources imported from another system.
        :type migration_metadata: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param name: Display name of the metric.
        :type name: str, optional

        :param numerator_aggregation: Source measure and aggregation settings for a metric value.
        :type numerator_aggregation: ExperimentsMetricV2DTODataAttributesNumeratorAggregation, none_type, optional

        :param percentile_aggregation: Source measure and settings for a percentile metric.
        :type percentile_aggregation: ExperimentsMetricV2DTODataAttributesPercentileAggregation, none_type, optional

        :param reference_url: URL with supporting information about the metric.
        :type reference_url: str, optional

        :param updated_at: Time when this resource was last updated.
        :type updated_at: datetime, optional
        """
        if certified_at is not unset:
            kwargs["certified_at"] = certified_at
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if data_source_type is not unset:
            kwargs["data_source_type"] = data_source_type
        if denominator_aggregation is not unset:
            kwargs["denominator_aggregation"] = denominator_aggregation
        if description is not unset:
            kwargs["description"] = description
        if desired_change is not unset:
            kwargs["desired_change"] = desired_change
        if experiment_count is not unset:
            kwargs["experiment_count"] = experiment_count
        if format_as_percent is not unset:
            kwargs["format_as_percent"] = format_as_percent
        if guardrail_cutoff_threshold is not unset:
            kwargs["guardrail_cutoff_threshold"] = guardrail_cutoff_threshold
        if metric_type is not unset:
            kwargs["metric_type"] = metric_type
        if migration_metadata is not unset:
            kwargs["migration_metadata"] = migration_metadata
        if name is not unset:
            kwargs["name"] = name
        if numerator_aggregation is not unset:
            kwargs["numerator_aggregation"] = numerator_aggregation
        if percentile_aggregation is not unset:
            kwargs["percentile_aggregation"] = percentile_aggregation
        if reference_url is not unset:
            kwargs["reference_url"] = reference_url
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        super().__init__(kwargs)
