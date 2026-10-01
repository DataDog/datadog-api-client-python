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
    from datadog_api_client.v2.model.observability_pipeline_enrichment_table_file_encoding import (
        ObservabilityPipelineEnrichmentTableFileEncoding,
    )
    from datadog_api_client.v2.model.observability_pipeline_metric_enrichment_table_file_key import (
        ObservabilityPipelineMetricEnrichmentTableFileKey,
    )


class ObservabilityPipelineMetricEnrichmentTableFile(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_enrichment_table_file_encoding import (
            ObservabilityPipelineEnrichmentTableFileEncoding,
        )
        from datadog_api_client.v2.model.observability_pipeline_metric_enrichment_table_file_key import (
            ObservabilityPipelineMetricEnrichmentTableFileKey,
        )

        return {
            "encoding": (ObservabilityPipelineEnrichmentTableFileEncoding,),
            "key": (ObservabilityPipelineMetricEnrichmentTableFileKey,),
            "path": (str,),
        }

    attribute_map = {
        "encoding": "encoding",
        "key": "key",
        "path": "path",
    }

    def __init__(
        self_,
        encoding: ObservabilityPipelineEnrichmentTableFileEncoding,
        key: ObservabilityPipelineMetricEnrichmentTableFileKey,
        path: str,
        **kwargs,
    ):
        """
        Defines a static enrichment table loaded from a CSV file for metric enrichment.

        :param encoding: File encoding format.
        :type encoding: ObservabilityPipelineEnrichmentTableFileEncoding

        :param key: Defines how to map a metric lookup value to a CSV column during enrichment table lookups.
        :type key: ObservabilityPipelineMetricEnrichmentTableFileKey

        :param path: Path to the CSV file.
        :type path: str
        """
        super().__init__(kwargs)

        self_.encoding = encoding
        self_.key = key
        self_.path = path
