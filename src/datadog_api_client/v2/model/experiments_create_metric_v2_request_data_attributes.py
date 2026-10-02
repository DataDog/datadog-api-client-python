# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class ExperimentsCreateMetricV2RequestDataAttributes(ModelComposed):
    def __init__(self, **kwargs):
        """
        Configuration for the new metric. Supply either numerator_aggregation or percentile_aggregation. A denominator_aggregation requires numerator_aggregation. Omit unused aggregation fields; do not send them as null.

        :param data_source_type: Source of the data backing this metric.
        :type data_source_type: ExperimentsCreateMetricV2RequestDataAttributesDataSourceType

        :param denominator_aggregation: Measure and calculation settings for a numerator or denominator aggregation. Supply exactly one non-null measure.
        :type denominator_aggregation: ExperimentsCreateMetricV2RequestDataAttributesNumeratorAggregation, optional

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

        :param numerator_aggregation: Measure and calculation settings for a numerator or denominator aggregation. Supply exactly one non-null measure.
        :type numerator_aggregation: ExperimentsCreateMetricV2RequestDataAttributesNumeratorAggregation

        :param percentile_aggregation: Measure and percentile to calculate for the metric. Supply exactly one non-null measure.
        :type percentile_aggregation: ExperimentsCreateMetricV2RequestDataAttributesPercentileAggregation
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.experiments_create_metric_numerator_attributes import (
            ExperimentsCreateMetricNumeratorAttributes,
        )
        from datadog_api_client.v2.model.experiments_create_metric_percentile_attributes import (
            ExperimentsCreateMetricPercentileAttributes,
        )

        return {
            "oneOf": [
                ExperimentsCreateMetricNumeratorAttributes,
                ExperimentsCreateMetricPercentileAttributes,
            ],
        }
