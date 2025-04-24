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
    from datadog_api_client.v2.model.observability_pipeline_enrichment_table_file_encoding import (
        ObservabilityPipelineEnrichmentTableFileEncoding,
    )
    from datadog_api_client.v2.model.observability_pipeline_enrichment_table_file_key_items import (
        ObservabilityPipelineEnrichmentTableFileKeyItems,
    )
    from datadog_api_client.v2.model.observability_pipeline_enrichment_table_file_schema_items import (
        ObservabilityPipelineEnrichmentTableFileSchemaItems,
    )


class ObservabilityPipelineEnrichmentTableFile(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_enrichment_table_file_encoding import (
            ObservabilityPipelineEnrichmentTableFileEncoding,
        )
        from datadog_api_client.v2.model.observability_pipeline_enrichment_table_file_key_items import (
            ObservabilityPipelineEnrichmentTableFileKeyItems,
        )
        from datadog_api_client.v2.model.observability_pipeline_enrichment_table_file_schema_items import (
            ObservabilityPipelineEnrichmentTableFileSchemaItems,
        )

        return {
            "encoding": (ObservabilityPipelineEnrichmentTableFileEncoding,),
            "key": ([ObservabilityPipelineEnrichmentTableFileKeyItems],),
            "path": (str,),
            "schema": ([ObservabilityPipelineEnrichmentTableFileSchemaItems],),
        }

    attribute_map = {
        "encoding": "encoding",
        "key": "key",
        "path": "path",
        "schema": "schema",
    }

    def __init__(
        self_,
        encoding: ObservabilityPipelineEnrichmentTableFileEncoding,
        key: List[ObservabilityPipelineEnrichmentTableFileKeyItems],
        path: str,
        schema: List[ObservabilityPipelineEnrichmentTableFileSchemaItems],
        **kwargs,
    ):
        """
        Defines a static enrichment table loaded from a CSV file.

        :param encoding: File encoding format.
        :type encoding: ObservabilityPipelineEnrichmentTableFileEncoding

        :param key: Key fields used to look up enrichment values.
        :type key: [ObservabilityPipelineEnrichmentTableFileKeyItems]

        :param path: Path to the CSV file.
        :type path: str

        :param schema: Schema defining column names and their types.
        :type schema: [ObservabilityPipelineEnrichmentTableFileSchemaItems]
        """
        super().__init__(kwargs)

        self_.encoding = encoding
        self_.key = key
        self_.path = path
        self_.schema = schema
