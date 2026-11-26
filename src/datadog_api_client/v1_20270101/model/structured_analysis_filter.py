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
    from datadog_api_client.v1_20270101.model.structured_analysis_filter_type import StructuredAnalysisFilterType


class StructuredAnalysisFilter(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.structured_analysis_filter_type import StructuredAnalysisFilterType

        return {
            "filter": (str,),
            "type": (StructuredAnalysisFilterType,),
        }

    attribute_map = {
        "filter": "filter",
        "type": "type",
    }

    def __init__(self_, filter: str, type: StructuredAnalysisFilterType, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param filter: Test-only generated schema for the dashboard versioning proof of concept.
        :type filter: str

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: StructuredAnalysisFilterType
        """
        super().__init__(kwargs)

        self_.filter = filter
        self_.type = type
