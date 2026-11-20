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
    from datadog_api_client.v1_20270101.model.structured_analysis_limit_type import StructuredAnalysisLimitType


class StructuredAnalysisLimit(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.structured_analysis_limit_type import StructuredAnalysisLimitType

        return {
            "limit": (float,),
            "type": (StructuredAnalysisLimitType,),
        }

    attribute_map = {
        "limit": "limit",
        "type": "type",
    }

    def __init__(self_, limit: float, type: StructuredAnalysisLimitType, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param limit: Test-only generated schema for the dashboard versioning proof of concept.
        :type limit: float

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: StructuredAnalysisLimitType
        """
        super().__init__(kwargs)

        self_.limit = limit
        self_.type = type
