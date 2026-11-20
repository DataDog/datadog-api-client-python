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
    from datadog_api_client.v1_20270101.model.structured_analysis_calculated_field_type import (
        StructuredAnalysisCalculatedFieldType,
    )


class StructuredAnalysisCalculatedField(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.structured_analysis_calculated_field_type import (
            StructuredAnalysisCalculatedFieldType,
        )

        return {
            "expression": (str,),
            "name": (str,),
            "type": (StructuredAnalysisCalculatedFieldType,),
        }

    attribute_map = {
        "expression": "expression",
        "name": "name",
        "type": "type",
    }

    def __init__(self_, expression: str, name: str, type: StructuredAnalysisCalculatedFieldType, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param expression: Test-only generated schema for the dashboard versioning proof of concept.
        :type expression: str

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: StructuredAnalysisCalculatedFieldType
        """
        super().__init__(kwargs)

        self_.expression = expression
        self_.name = name
        self_.type = type
