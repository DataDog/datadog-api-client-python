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
        "type": "type",
    }

    def __init__(
        self_,
        drop_events: bool,
        id: str,
        include: str,
        inputs: List[str],
        limit: ObservabilityPipelineQuotaProcessorLimit,
        name: str,
        type: ObservabilityPipelineQuotaProcessorType,
        ignore_when_missing_partitions: Union[bool, UnsetType] = unset,
        overflow_action: Union[ObservabilityPipelineQuotaProcessorOverflowAction, UnsetType] = unset,
        overrides: Union[List[ObservabilityPipelineQuotaProcessorOverride], UnsetType] = unset,
        partition_fields: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        The Quota Processor measures logging traffic for logs that match a specified filter. When the configured daily quota is met, the processor can drop or alert.

        :param drop_events: If set to ``true`` , logs that matched the quota filter and sent after the quota has been met are dropped; only logs that did not match the filter query continue through the pipeline.
        :type drop_events: bool

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

        :param overflow_action: The action to take when the quota is exceeded. Options:

            * ``drop`` : Drop the event.
            * ``no_action`` : Let the event pass through.
            * ``overflow_routing`` : Route to an overflow destination.
        :type overflow_action: ObservabilityPipelineQuotaProcessorOverflowAction, optional

        :param overrides: A list of alternate quota rules that apply to specific sets of events, identified by matching field values. Each override can define a custom limit.
        :type overrides: [ObservabilityPipelineQuotaProcessorOverride], optional

        :param partition_fields: A list of fields used to segment log traffic for quota enforcement. Quotas are tracked independently by unique combinations of these field values.
        :type partition_fields: [str], optional

        :param type: The processor type. The value should always be ``quota``.
        :type type: ObservabilityPipelineQuotaProcessorType
        """
        if ignore_when_missing_partitions is not unset:
            kwargs["ignore_when_missing_partitions"] = ignore_when_missing_partitions
        if overflow_action is not unset:
            kwargs["overflow_action"] = overflow_action
        if overrides is not unset:
            kwargs["overrides"] = overrides
        if partition_fields is not unset:
            kwargs["partition_fields"] = partition_fields
        super().__init__(kwargs)

        self_.drop_events = drop_events
        self_.id = id
        self_.include = include
        self_.inputs = inputs
        self_.limit = limit
        self_.name = name
        self_.type = type
