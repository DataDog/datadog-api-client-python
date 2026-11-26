# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.structured_analysis_destructure_columns_items import (
        StructuredAnalysisDestructureColumnsItems,
    )
    from datadog_api_client.v1_20270101.model.structured_analysis_destructure_type import (
        StructuredAnalysisDestructureType,
    )


class StructuredAnalysisDestructure(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.structured_analysis_destructure_columns_items import (
            StructuredAnalysisDestructureColumnsItems,
        )
        from datadog_api_client.v1_20270101.model.structured_analysis_destructure_type import (
            StructuredAnalysisDestructureType,
        )

        return {
            "columns": ([StructuredAnalysisDestructureColumnsItems],),
            "type": (StructuredAnalysisDestructureType,),
        }

    attribute_map = {
        "columns": "columns",
        "type": "type",
    }

    def __init__(
        self_,
        columns: List[StructuredAnalysisDestructureColumnsItems],
        type: StructuredAnalysisDestructureType,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param columns: Test-only generated schema for the dashboard versioning proof of concept.
        :type columns: [StructuredAnalysisDestructureColumnsItems]

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: StructuredAnalysisDestructureType
        """
        super().__init__(kwargs)

        self_.columns = columns
        self_.type = type
