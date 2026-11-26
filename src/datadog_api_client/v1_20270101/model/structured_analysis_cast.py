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
    from datadog_api_client.v1_20270101.model.structured_analysis_cast_target_type import (
        StructuredAnalysisCastTargetType,
    )
    from datadog_api_client.v1_20270101.model.structured_analysis_cast_type import StructuredAnalysisCastType


class StructuredAnalysisCast(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.structured_analysis_cast_target_type import (
            StructuredAnalysisCastTargetType,
        )
        from datadog_api_client.v1_20270101.model.structured_analysis_cast_type import StructuredAnalysisCastType

        return {
            "source_column": (str,),
            "target_column": (str,),
            "target_type": (StructuredAnalysisCastTargetType,),
            "type": (StructuredAnalysisCastType,),
        }

    attribute_map = {
        "source_column": "source_column",
        "target_column": "target_column",
        "target_type": "target_type",
        "type": "type",
    }

    def __init__(
        self_,
        source_column: str,
        target_column: str,
        target_type: StructuredAnalysisCastTargetType,
        type: StructuredAnalysisCastType,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param source_column: Test-only generated schema for the dashboard versioning proof of concept.
        :type source_column: str

        :param target_column: Test-only generated schema for the dashboard versioning proof of concept.
        :type target_column: str

        :param target_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type target_type: StructuredAnalysisCastTargetType

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: StructuredAnalysisCastType
        """
        super().__init__(kwargs)

        self_.source_column = source_column
        self_.target_column = target_column
        self_.target_type = target_type
        self_.type = type
