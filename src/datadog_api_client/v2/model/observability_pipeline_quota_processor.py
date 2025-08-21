# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.observability_pipeline_quota_processor_limit import (
        ObservabilityPipelineQuotaProcessorLimit,
    )
    from datadog_api_client.v2.model.observability_pipeline_quota_processor_overflow_action import (
        ObservabilityPipelineQuotaProcessorOverflowAction,
    )
    from datadog_api_client.v2.model.observability_pipeline_quota_processor_override import (
        ObservabilityPipelineQuotaProcessorOverride,
    )
    from datadog_api_client.v2.model.observability_pipeline_quota_processor_type import (
        ObservabilityPipelineQuotaProcessorType,
    )


class ObservabilityPipelineQuotaProcessor(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_quota_processor_limit import (
            ObservabilityPipelineQuotaProcessorLimit,
        )
        from datadog_api_client.v2.model.observability_pipeline_quota_processor_overflow_action import (
            ObservabilityPipelineQuotaProcessorOverflowAction,
        )
        from datadog_api_client.v2.model.observability_pipeline_quota_processor_override import (
            ObservabilityPipelineQuotaProcessorOverride,
        )
        from datadog_api_client.v2.model.observability_pipeline_quota_processor_type import (
            ObservabilityPipelineQuotaProcessorType,
        )

        return {
            "drop_events": (bool,),
            "id": (str,),
            "ignore_when_missing_partitions": (bool,),
            "include": (str,),
            "inputs": ([str],),
            "limit": (ObservabilityPipelineQuotaProcessorLimit,),
            "name": (str,),
            "overflow_action": (ObservabilityPipelineQuotaProcessorOverflowAction,),
            "overrides": ([ObservabilityPipelineQuotaProcessorOverride],),
            "partition_fields": ([str],),
            "too_many_buckets_action": (ObservabilityPipelineQuotaProcessorOverflowAction,),
            "type": (ObservabilityPipelineQuotaProcessorType,),
        }

    attribute_map = {
        "drop_events": "drop_events",
        "id": "id",
        "ignore_when_missing_partitions": "ignore_when_missing_partitions",
        "include": "include",
        "inputs": "inputs",
        "limit": "limit",
        "name": "name",
        "overflow_action": "overflow_action",
        "overrides": "overrides",
        "partition_fields": "partition_fields",
        "too_many_buckets_action": "too_many_buckets_action",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        include: str,
        inputs: List[str],
        limit: ObservabilityPipelineQuotaProcessorLimit,
        name: str,
        type: ObservabilityPipelineQuotaProcessorType,
        drop_events: Union[bool, UnsetType] = unset,
        ignore_when_missing_partitions: Union[bool, UnsetType] = unset,
        overflow_action: Union[ObservabilityPipelineQuotaProcessorOverflowAction, UnsetType] = unset,
        overrides: Union[List[ObservabilityPipelineQuotaProcessorOverride], UnsetType] = unset,
        partition_fields: Union[List[str], UnsetType] = unset,
        too_many_buckets_action: Union[ObservabilityPipelineQuotaProcessorOverflowAction, UnsetType] = unset,
        **kwargs,
    ):
        """
        The Quota Processor measures logging traffic for logs that match a specified filter. When the configured daily quota is met, the processor can drop or alert.

        :param drop_events: If set to ``true`` , logs that match the quota filter and are sent after the quota is exceeded are dropped. Logs that do not match the filter continue through the pipeline. **Note** : You can set either ``drop_events`` or ``overflow_action`` , but not both.
        :type drop_events: bool, optional

        :param id: The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the ``input`` to downstream components).
        :type id: str

        :param ignore_when_missing_partitions: If ``true`` , the processor skips quota checks when partition fields are missing from the logs.
        :type ignore_when_missing_partitions: bool, optional

        :param include: A Datadog search query used to determine which logs this processor targets.
        :type include: str

        :param inputs: A list of component IDs whose output is used as the ``input`` for this component.
        :type inputs: [str]

        :param limit: The maximum amount of data or number of events allowed before the quota is enforced. Can be specified in bytes or events.
        :type limit: ObservabilityPipelineQuotaProcessorLimit

        :param name: Name of the quota.
        :type name: str

        :param overflow_action: The action to take when the quota or bucket limit is exceeded. Options:

            * ``drop`` : Drop the event.
            * ``no_action`` : Let the event pass through.
            * ``overflow_routing`` : Route to an overflow destination.
        :type overflow_action: ObservabilityPipelineQuotaProcessorOverflowAction, optional

        :param overrides: A list of alternate quota rules that apply to specific sets of events, identified by matching field values. Each override can define a custom limit.
        :type overrides: [ObservabilityPipelineQuotaProcessorOverride], optional

        :param partition_fields: A list of fields used to segment log traffic for quota enforcement. Quotas are tracked independently by unique combinations of these field values.
        :type partition_fields: [str], optional

        :param too_many_buckets_action: The action to take when the quota or bucket limit is exceeded. Options:

            * ``drop`` : Drop the event.
            * ``no_action`` : Let the event pass through.
            * ``overflow_routing`` : Route to an overflow destination.
        :type too_many_buckets_action: ObservabilityPipelineQuotaProcessorOverflowAction, optional

        :param type: The processor type. The value should always be ``quota``.
        :type type: ObservabilityPipelineQuotaProcessorType
        """
        if drop_events is not unset:
            kwargs["drop_events"] = drop_events
        if ignore_when_missing_partitions is not unset:
            kwargs["ignore_when_missing_partitions"] = ignore_when_missing_partitions
        if overflow_action is not unset:
            kwargs["overflow_action"] = overflow_action
        if overrides is not unset:
            kwargs["overrides"] = overrides
        if partition_fields is not unset:
            kwargs["partition_fields"] = partition_fields
        if too_many_buckets_action is not unset:
            kwargs["too_many_buckets_action"] = too_many_buckets_action
        super().__init__(kwargs)

        self_.id = id
        self_.include = include
        self_.inputs = inputs
        self_.limit = limit
        self_.name = name
        self_.type = type
