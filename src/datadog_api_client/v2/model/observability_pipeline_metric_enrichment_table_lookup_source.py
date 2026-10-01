# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class ObservabilityPipelineMetricEnrichmentTableLookupSource(ModelComposed):
    def __init__(self, **kwargs):
        """
        Specifies the source of the key value used for metric enrichment table lookups.
        The lookup key can be either the metric name or a metric tag.

        :param type: The lookup source type. The value should always be `metric_name`.
        :type type: ObservabilityPipelineMetricEnrichmentTableMetricNameLookupType

        :param name: The Datadog tag key used as the lookup key.
        :type name: str
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.observability_pipeline_metric_enrichment_table_metric_name_lookup import (
            ObservabilityPipelineMetricEnrichmentTableMetricNameLookup,
        )
        from datadog_api_client.v2.model.observability_pipeline_metric_enrichment_table_tag_lookup import (
            ObservabilityPipelineMetricEnrichmentTableTagLookup,
        )

        return {
            "oneOf": [
                ObservabilityPipelineMetricEnrichmentTableMetricNameLookup,
                ObservabilityPipelineMetricEnrichmentTableTagLookup,
            ],
        }
