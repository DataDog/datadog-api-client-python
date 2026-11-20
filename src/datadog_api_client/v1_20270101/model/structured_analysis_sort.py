# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.sort_order2 import SortOrder2
    from datadog_api_client.v1_20270101.model.structured_analysis_sort_type import StructuredAnalysisSortType


class StructuredAnalysisSort(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.sort_order2 import SortOrder2
        from datadog_api_client.v1_20270101.model.structured_analysis_sort_type import StructuredAnalysisSortType

        return {
            "column": (str,),
            "order": (SortOrder2,),
            "type": (StructuredAnalysisSortType,),
        }

    attribute_map = {
        "column": "column",
        "order": "order",
        "type": "type",
    }

    def __init__(self_, column: str, order: SortOrder2, type: StructuredAnalysisSortType, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param column: Test-only generated schema for the dashboard versioning proof of concept.
        :type column: str

        :param order: Test-only generated schema for the dashboard versioning proof of concept.
        :type order: SortOrder2

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: StructuredAnalysisSortType
        """
        super().__init__(kwargs)

        self_.column = column
        self_.order = order
        self_.type = type
