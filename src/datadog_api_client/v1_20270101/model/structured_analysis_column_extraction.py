# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.structured_analysis_column_extraction_type import (
        StructuredAnalysisColumnExtractionType,
    )


class StructuredAnalysisColumnExtraction(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.structured_analysis_column_extraction_type import (
            StructuredAnalysisColumnExtractionType,
        )

        return {
            "grok_expression": (str,),
            "keep_nulls": (bool,),
            "source_column": (str,),
            "type": (StructuredAnalysisColumnExtractionType,),
        }

    attribute_map = {
        "grok_expression": "grok_expression",
        "keep_nulls": "keep_nulls",
        "source_column": "source_column",
        "type": "type",
    }

    def __init__(
        self_,
        grok_expression: str,
        source_column: str,
        type: StructuredAnalysisColumnExtractionType,
        keep_nulls: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param grok_expression: Test-only generated schema for the dashboard versioning proof of concept.
        :type grok_expression: str

        :param keep_nulls: Test-only generated schema for the dashboard versioning proof of concept.
        :type keep_nulls: bool, optional

        :param source_column: Test-only generated schema for the dashboard versioning proof of concept.
        :type source_column: str

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: StructuredAnalysisColumnExtractionType
        """
        if keep_nulls is not unset:
            kwargs["keep_nulls"] = keep_nulls
        super().__init__(kwargs)

        self_.grok_expression = grok_expression
        self_.source_column = source_column
        self_.type = type
