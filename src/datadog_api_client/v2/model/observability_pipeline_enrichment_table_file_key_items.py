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
    from datadog_api_client.v2.model.observability_pipeline_enrichment_table_file_key_items_comparison import (
        ObservabilityPipelineEnrichmentTableFileKeyItemsComparison,
    )


class ObservabilityPipelineEnrichmentTableFileKeyItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_enrichment_table_file_key_items_comparison import (
            ObservabilityPipelineEnrichmentTableFileKeyItemsComparison,
        )

        return {
            "column": (str,),
            "comparison": (ObservabilityPipelineEnrichmentTableFileKeyItemsComparison,),
            "field": (str,),
        }

    attribute_map = {
        "column": "column",
        "comparison": "comparison",
        "field": "field",
    }

    def __init__(
        self_, column: str, comparison: ObservabilityPipelineEnrichmentTableFileKeyItemsComparison, field: str, **kwargs
    ):
        """
        Defines how to map log fields to enrichment table columns during lookups.

        :param column: The ``items`` ``column``.
        :type column: str

        :param comparison: Defines how to compare key fields for enrichment table lookups.
        :type comparison: ObservabilityPipelineEnrichmentTableFileKeyItemsComparison

        :param field: The ``items`` ``field``.
        :type field: str
        """
        super().__init__(kwargs)

        self_.column = column
        self_.comparison = comparison
        self_.field = field
