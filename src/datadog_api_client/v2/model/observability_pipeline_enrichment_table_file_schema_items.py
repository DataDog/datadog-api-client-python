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
    from datadog_api_client.v2.model.observability_pipeline_enrichment_table_file_schema_items_type import (
        ObservabilityPipelineEnrichmentTableFileSchemaItemsType,
    )


class ObservabilityPipelineEnrichmentTableFileSchemaItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_enrichment_table_file_schema_items_type import (
            ObservabilityPipelineEnrichmentTableFileSchemaItemsType,
        )

        return {
            "column": (str,),
            "type": (ObservabilityPipelineEnrichmentTableFileSchemaItemsType,),
        }

    attribute_map = {
        "column": "column",
        "type": "type",
    }

    def __init__(self_, column: str, type: ObservabilityPipelineEnrichmentTableFileSchemaItemsType, **kwargs):
        """
        Describes a single column and its type in an enrichment table schema.

        :param column: The ``items`` ``column``.
        :type column: str

        :param type: Declares allowed data types for enrichment table columns.
        :type type: ObservabilityPipelineEnrichmentTableFileSchemaItemsType
        """
        super().__init__(kwargs)

        self_.column = column
        self_.type = type
