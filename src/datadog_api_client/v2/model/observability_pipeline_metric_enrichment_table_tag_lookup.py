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
    from datadog_api_client.v2.model.observability_pipeline_metric_enrichment_table_tag_lookup_type import (
        ObservabilityPipelineMetricEnrichmentTableTagLookupType,
    )


class ObservabilityPipelineMetricEnrichmentTableTagLookup(ModelNormal):
    validations = {
        "name": {
            "max_length": 200,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_metric_enrichment_table_tag_lookup_type import (
            ObservabilityPipelineMetricEnrichmentTableTagLookupType,
        )

        return {
            "name": (str,),
            "type": (ObservabilityPipelineMetricEnrichmentTableTagLookupType,),
        }

    attribute_map = {
        "name": "name",
        "type": "type",
    }

    def __init__(self_, name: str, type: ObservabilityPipelineMetricEnrichmentTableTagLookupType, **kwargs):
        """
        Uses a metric tag as the lookup key for enrichment table matching.

        :param name: The Datadog tag key used as the lookup key.
        :type name: str

        :param type: The lookup source type. The value should always be ``tag``.
        :type type: ObservabilityPipelineMetricEnrichmentTableTagLookupType
        """
        super().__init__(kwargs)

        self_.name = name
        self_.type = type
