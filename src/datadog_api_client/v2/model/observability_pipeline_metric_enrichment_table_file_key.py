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
    from datadog_api_client.v2.model.observability_pipeline_metric_enrichment_table_lookup_source import (
        ObservabilityPipelineMetricEnrichmentTableLookupSource,
    )
    from datadog_api_client.v2.model.observability_pipeline_metric_enrichment_table_metric_name_lookup import (
        ObservabilityPipelineMetricEnrichmentTableMetricNameLookup,
    )
    from datadog_api_client.v2.model.observability_pipeline_metric_enrichment_table_tag_lookup import (
        ObservabilityPipelineMetricEnrichmentTableTagLookup,
    )


class ObservabilityPipelineMetricEnrichmentTableFileKey(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_metric_enrichment_table_lookup_source import (
            ObservabilityPipelineMetricEnrichmentTableLookupSource,
        )

        return {
            "column": (str,),
            "source": (ObservabilityPipelineMetricEnrichmentTableLookupSource,),
        }

    attribute_map = {
        "column": "column",
        "source": "source",
    }

    def __init__(
        self_,
        column: str,
        source: Union[
            ObservabilityPipelineMetricEnrichmentTableLookupSource,
            ObservabilityPipelineMetricEnrichmentTableMetricNameLookup,
            ObservabilityPipelineMetricEnrichmentTableTagLookup,
        ],
        **kwargs,
    ):
        """
        Defines how to map a metric lookup value to a CSV column during enrichment table lookups.

        :param column: The CSV column name or index to match against the lookup value.
        :type column: str

        :param source: Specifies the source of the key value used for metric enrichment table lookups.
            The lookup key can be either the metric name or a metric tag.
        :type source: ObservabilityPipelineMetricEnrichmentTableLookupSource
        """
        super().__init__(kwargs)

        self_.column = column
        self_.source = source
