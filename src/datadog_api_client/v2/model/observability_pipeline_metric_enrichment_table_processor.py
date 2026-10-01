# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class ObservabilityPipelineMetricEnrichmentTableProcessor(ModelComposed):
    def __init__(self, **kwargs):
        """
        The ``enrichment_table`` processor enriches metrics with tags from a static CSV file or a Datadog reference table.
        It looks up a row using the metric name or a metric tag value. It then adds each column of the matching row as a
        metric tag, overwriting any existing tag with the same key. Exactly one of ``file`` or ``reference_table`` must be
        configured.

        **Supported pipeline types:** metrics

        :param display_name: The display name for a component.
        :type display_name: str, optional

        :param enabled: Indicates whether the processor is enabled.
        :type enabled: bool

        :param file: Defines a static enrichment table loaded from a CSV file for metric enrichment.
        :type file: ObservabilityPipelineMetricEnrichmentTableFile

        :param id: The unique identifier for this component. Used in other parts of the pipeline to reference this component
            (for example, as the `input` to downstream components).
        :type id: str

        :param include: A Datadog search query used to determine which metrics this processor targets.
        :type include: str

        :param type: The processor type. The value should always be `enrichment_table`.
        :type type: ObservabilityPipelineEnrichmentTableProcessorType

        :param reference_table: Uses a Datadog reference table to enrich metrics.
        :type reference_table: ObservabilityPipelineMetricEnrichmentTableReferenceTable
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
        from datadog_api_client.v2.model.observability_pipeline_metric_enrichment_table_file_processor import (
            ObservabilityPipelineMetricEnrichmentTableFileProcessor,
        )
        from datadog_api_client.v2.model.observability_pipeline_metric_enrichment_table_reference_table_processor import (
            ObservabilityPipelineMetricEnrichmentTableReferenceTableProcessor,
        )

        return {
            "oneOf": [
                ObservabilityPipelineMetricEnrichmentTableFileProcessor,
                ObservabilityPipelineMetricEnrichmentTableReferenceTableProcessor,
            ],
        }
