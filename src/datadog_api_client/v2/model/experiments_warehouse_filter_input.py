# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class ExperimentsWarehouseFilterInput(ModelComposed):
    def __init__(self, **kwargs):
        """
        A property or measure comparison for a Warehouse numerator or denominator. Set exactly one target ID that is not blank. Measure comparisons require numeric measures and numeric values. BETWEEN bounds must be in ascending order.

        :param measure_id: Omit this target or use null or a blank string.
        :type measure_id: str, none_type, optional

        :param operation: Comparison applied by the warehouse entry-point filter.
        :type operation: ExperimentsPatchExperimentV2ResponseDataAttributesWarehouseExposureConfigurationEntryPointFiltersItemsOperation

        :param property_id: ID of the property on the aggregation source.
        :type property_id: UUID

        :param values: Values used by the comparison.
        :type values: [str]
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
        from datadog_api_client.v2.model.experiments_property_filter_input import ExperimentsPropertyFilterInput
        from datadog_api_client.v2.model.experiments_property_null_filter_input import (
            ExperimentsPropertyNullFilterInput,
        )
        from datadog_api_client.v2.model.experiments_measure_comparison_filter_input import (
            ExperimentsMeasureComparisonFilterInput,
        )
        from datadog_api_client.v2.model.experiments_measure_range_filter_input import (
            ExperimentsMeasureRangeFilterInput,
        )
        from datadog_api_client.v2.model.experiments_measure_null_filter_input import ExperimentsMeasureNullFilterInput

        return {
            "oneOf": [
                ExperimentsPropertyFilterInput,
                ExperimentsPropertyNullFilterInput,
                ExperimentsMeasureComparisonFilterInput,
                ExperimentsMeasureRangeFilterInput,
                ExperimentsMeasureNullFilterInput,
            ],
        }
