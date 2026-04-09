# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.observability_pipeline_enrichment_table_file_key_items_comparison import (
        ObservabilityPipelineEnrichmentTableFileKeyItemsComparison,
    )
    from datadog_api_client.v2.model.observability_pipeline_enrichment_table_file_key_item_field import (
        ObservabilityPipelineEnrichmentTableFileKeyItemField,
    )
    from datadog_api_client.v2.model.observability_pipeline_enrichment_table_field_event_lookup import (
        ObservabilityPipelineEnrichmentTableFieldEventLookup,
    )
    from datadog_api_client.v2.model.observability_pipeline_enrichment_table_field_vrl_lookup import (
        ObservabilityPipelineEnrichmentTableFieldVrlLookup,
    )
    from datadog_api_client.v2.model.observability_pipeline_enrichment_table_field_secret_lookup import (
        ObservabilityPipelineEnrichmentTableFieldSecretLookup,
    )


class ObservabilityPipelineEnrichmentTableFileKeyItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_enrichment_table_file_key_items_comparison import (
            ObservabilityPipelineEnrichmentTableFileKeyItemsComparison,
        )
        from datadog_api_client.v2.model.observability_pipeline_enrichment_table_file_key_item_field import (
            ObservabilityPipelineEnrichmentTableFileKeyItemField,
        )

        return {
            "column": (str,),
            "comparison": (ObservabilityPipelineEnrichmentTableFileKeyItemsComparison,),
            "field": (ObservabilityPipelineEnrichmentTableFileKeyItemField,),
        }

    attribute_map = {
        "column": "column",
        "comparison": "comparison",
        "field": "field",
    }

    def __init__(
        self_,
        column: str,
        comparison: ObservabilityPipelineEnrichmentTableFileKeyItemsComparison,
        field: Union[
            ObservabilityPipelineEnrichmentTableFileKeyItemField,
            str,
            ObservabilityPipelineEnrichmentTableFieldEventLookup,
            ObservabilityPipelineEnrichmentTableFieldVrlLookup,
            ObservabilityPipelineEnrichmentTableFieldSecretLookup,
        ],
        **kwargs,
    ):
        """
        Defines how to map log fields to enrichment table columns during lookups.

        :param column: The ``items`` ``column``.
        :type column: str

        :param comparison: Defines how to compare key fields for enrichment table lookups.
        :type comparison: ObservabilityPipelineEnrichmentTableFileKeyItemsComparison

        :param field: Specifies the source of the key value used for enrichment table lookups.
            Can be a plain field path string or an object specifying ``event`` , ``vrl`` , or ``secret``.
        :type field: ObservabilityPipelineEnrichmentTableFileKeyItemField
        """
        super().__init__(kwargs)

        self_.column = column
        self_.comparison = comparison
        self_.field = field
