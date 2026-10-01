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
    from datadog_api_client.v2.model.observability_pipeline_metric_enrichment_table_metric_name_lookup_type import (
        ObservabilityPipelineMetricEnrichmentTableMetricNameLookupType,
    )


class ObservabilityPipelineMetricEnrichmentTableMetricNameLookup(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_metric_enrichment_table_metric_name_lookup_type import (
            ObservabilityPipelineMetricEnrichmentTableMetricNameLookupType,
        )

        return {
            "type": (ObservabilityPipelineMetricEnrichmentTableMetricNameLookupType,),
        }

    attribute_map = {
        "type": "type",
    }

    def __init__(self_, type: ObservabilityPipelineMetricEnrichmentTableMetricNameLookupType, **kwargs):
        """
        Uses the metric name as the lookup key for enrichment table matching.

        :param type: The lookup source type. The value should always be ``metric_name``.
        :type type: ObservabilityPipelineMetricEnrichmentTableMetricNameLookupType
        """
        super().__init__(kwargs)

        self_.type = type
