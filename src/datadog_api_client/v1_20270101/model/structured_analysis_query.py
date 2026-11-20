# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.structured_analysis_transformation import StructuredAnalysisTransformation
    from datadog_api_client.v1_20270101.model.structured_analysis_query_type import StructuredAnalysisQueryType
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


class StructuredAnalysisQuery(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.structured_analysis_transformation import (
            StructuredAnalysisTransformation,
        )
        from datadog_api_client.v1_20270101.model.structured_analysis_query_type import StructuredAnalysisQueryType

        return {
            "source_dataset": (str,),
            "transformations": ([StructuredAnalysisTransformation],),
            "type": (StructuredAnalysisQueryType,),
        }

    attribute_map = {
        "source_dataset": "source_dataset",
        "transformations": "transformations",
        "type": "type",
    }

    def __init__(
        self_,
        source_dataset: str,
        transformations: List[
            Union[
                StructuredAnalysisTransformation,
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
            ]
        ],
        type: StructuredAnalysisQueryType,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param source_dataset: Test-only generated schema for the dashboard versioning proof of concept.
        :type source_dataset: str

        :param transformations: Test-only generated schema for the dashboard versioning proof of concept.
        :type transformations: [StructuredAnalysisTransformation]

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: StructuredAnalysisQueryType
        """
        super().__init__(kwargs)

        self_.source_dataset = source_dataset
        self_.transformations = transformations
        self_.type = type
