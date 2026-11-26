# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class StructuredAnalysisTransformation(ModelComposed):
    def __init__(self, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param filter: Test-only generated schema for the dashboard versioning proof of concept.
        :type filter: str

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: StructuredAnalysisFilterType

        :param grok_expression: Test-only generated schema for the dashboard versioning proof of concept.
        :type grok_expression: str

        :param keep_nulls: Test-only generated schema for the dashboard versioning proof of concept.
        :type keep_nulls: bool, optional

        :param source_column: Test-only generated schema for the dashboard versioning proof of concept.
        :type source_column: str

        :param compute: Test-only generated schema for the dashboard versioning proof of concept.
        :type compute: [StructuredAnalysisCompute], optional

        :param group_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type group_by: [StructuredAnalysisGroupBy], optional

        :param limit: Test-only generated schema for the dashboard versioning proof of concept.
        :type limit: float, optional

        :param sort: Test-only generated schema for the dashboard versioning proof of concept.
        :type sort: AnalysisAggregationSort, optional

        :param time_aggregation: Test-only generated schema for the dashboard versioning proof of concept.
        :type time_aggregation: StructuredAnalysisTimeAggregation, optional

        :param column: Test-only generated schema for the dashboard versioning proof of concept.
        :type column: str

        :param order: Test-only generated schema for the dashboard versioning proof of concept.
        :type order: SortOrder2

        :param expression: Test-only generated schema for the dashboard versioning proof of concept.
        :type expression: str

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param target_column: Test-only generated schema for the dashboard versioning proof of concept.
        :type target_column: str

        :param target_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type target_type: StructuredAnalysisCastTargetType

        :param join_conditions: Test-only generated schema for the dashboard versioning proof of concept.
        :type join_conditions: [StructuredAnalysisJoinCondition]

        :param join_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type join_type: StructuredAnalysisJoinJoinType

        :param target_columns: Test-only generated schema for the dashboard versioning proof of concept.
        :type target_columns: [str]

        :param target_dataset: Test-only generated schema for the dashboard versioning proof of concept.
        :type target_dataset: str

        :param columns: Test-only generated schema for the dashboard versioning proof of concept.
        :type columns: [StructuredAnalysisProjectionColumnsItems]
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
        from datadog_api_client.v1_20270101.model.structured_analysis_filter import StructuredAnalysisFilter
        from datadog_api_client.v1_20270101.model.structured_analysis_column_extraction import (
            StructuredAnalysisColumnExtraction,
        )
        from datadog_api_client.v1_20270101.model.structured_analysis_aggregation import StructuredAnalysisAggregation
        from datadog_api_client.v1_20270101.model.structured_analysis_sort import StructuredAnalysisSort
        from datadog_api_client.v1_20270101.model.structured_analysis_limit import StructuredAnalysisLimit
        from datadog_api_client.v1_20270101.model.structured_analysis_calculated_field import (
            StructuredAnalysisCalculatedField,
        )
        from datadog_api_client.v1_20270101.model.structured_analysis_cast import StructuredAnalysisCast
        from datadog_api_client.v1_20270101.model.structured_analysis_join import StructuredAnalysisJoin
        from datadog_api_client.v1_20270101.model.structured_analysis_projection import StructuredAnalysisProjection
        from datadog_api_client.v1_20270101.model.structured_analysis_destructure import StructuredAnalysisDestructure

        return {
            "oneOf": [
                StructuredAnalysisFilter,
                StructuredAnalysisColumnExtraction,
                StructuredAnalysisAggregation,
                StructuredAnalysisSort,
                StructuredAnalysisLimit,
                StructuredAnalysisCalculatedField,
                StructuredAnalysisCast,
                StructuredAnalysisJoin,
                StructuredAnalysisProjection,
                StructuredAnalysisDestructure,
            ],
        }
