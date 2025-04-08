# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class ObservabilityPipelineConfigProcessorItem(ModelComposed):
    def __init__(self, **kwargs):
        """
        A processor for the pipeline.

        :param id: The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the `input` to downstream components).
        :type id: str

        :param include: A Datadog search query used to determine which logs should pass through the filter. Logs that match this query continue to downstream components; others are dropped.
        :type include: str

        :param inputs: A list of component IDs whose output is used as the `input` for this component.
        :type inputs: [str]

        :param type: The processor type. The value should always be `filter`.
        :type type: ObservabilityPipelineFilterProcessorType

        :param field: The name of the log field that contains a JSON string.
        :type field: str

        :param drop_events: If set to `true`, logs that matched the quota filter and sent after the quota has been met are dropped; only logs that did not match the filter query continue through the pipeline.
        :type drop_events: bool

        :param ignore_when_missing_partitions: If `true`, the processor skips quota checks when partition fields are missing from the logs.
        :type ignore_when_missing_partitions: bool, optional

        :param limit: The maximum amount of data or number of events allowed before the quota is enforced. Can be specified in bytes or events.
        :type limit: ObservabilityPipelineQuotaProcessorLimit

        :param name: Name for identifying the processor.
        :type name: str

        :param overrides: A list of alternate quota rules that apply to specific sets of events, identified by matching field values. Each override can define a custom limit.
        :type overrides: [ObservabilityPipelineQuotaProcessorOverride], optional

        :param partition_fields: A list of fields used to segment log traffic for quota enforcement. Quotas are tracked independently by unique combinations of these field values.
        :type partition_fields: [str], optional

        :param fields: A list of static fields (key-value pairs) that is added to each log event processed by this component.
        :type fields: [ObservabilityPipelineFieldValue]
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
        from datadog_api_client.v2.model.observability_pipeline_filter_processor import (
            ObservabilityPipelineFilterProcessor,
        )
        from datadog_api_client.v2.model.observability_pipeline_parse_json_processor import (
            ObservabilityPipelineParseJSONProcessor,
        )
        from datadog_api_client.v2.model.observability_pipeline_quota_processor import (
            ObservabilityPipelineQuotaProcessor,
        )
        from datadog_api_client.v2.model.observability_pipeline_add_fields_processor import (
            ObservabilityPipelineAddFieldsProcessor,
        )
        from datadog_api_client.v2.model.observability_pipeline_remove_fields_processor import (
            ObservabilityPipelineRemoveFieldsProcessor,
        )
        from datadog_api_client.v2.model.observability_pipeline_rename_fields_processor import (
            ObservabilityPipelineRenameFieldsProcessor,
        )

        return {
            "oneOf": [
                ObservabilityPipelineFilterProcessor,
                ObservabilityPipelineParseJSONProcessor,
                ObservabilityPipelineQuotaProcessor,
                ObservabilityPipelineAddFieldsProcessor,
                ObservabilityPipelineRemoveFieldsProcessor,
                ObservabilityPipelineRenameFieldsProcessor,
            ],
        }
