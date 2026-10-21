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
    from datadog_api_client.v2.model.observability_pipeline_spike_protection_processor_action_when_missing_partitions import (
        ObservabilityPipelineSpikeProtectionProcessorActionWhenMissingPartitions,
    )
    from datadog_api_client.v2.model.observability_pipeline_spike_protection_processor_threshold_override import (
        ObservabilityPipelineSpikeProtectionProcessorThresholdOverride,
    )
    from datadog_api_client.v2.model.observability_pipeline_spike_protection_processor_spike_action import (
        ObservabilityPipelineSpikeProtectionProcessorSpikeAction,
    )
    from datadog_api_client.v2.model.observability_pipeline_spike_protection_processor_type import (
        ObservabilityPipelineSpikeProtectionProcessorType,
    )


class ObservabilityPipelineSpikeProtectionProcessor(ModelNormal):
    validations = {
        "partition_fields": {
            "max_items": 5,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_spike_protection_processor_action_when_missing_partitions import (
            ObservabilityPipelineSpikeProtectionProcessorActionWhenMissingPartitions,
        )
        from datadog_api_client.v2.model.observability_pipeline_spike_protection_processor_threshold_override import (
            ObservabilityPipelineSpikeProtectionProcessorThresholdOverride,
        )
        from datadog_api_client.v2.model.observability_pipeline_spike_protection_processor_spike_action import (
            ObservabilityPipelineSpikeProtectionProcessorSpikeAction,
        )
        from datadog_api_client.v2.model.observability_pipeline_spike_protection_processor_type import (
            ObservabilityPipelineSpikeProtectionProcessorType,
        )

        return {
            "action_when_missing_partitions": (
                ObservabilityPipelineSpikeProtectionProcessorActionWhenMissingPartitions,
            ),
            "display_name": (str,),
            "enabled": (bool,),
            "id": (str,),
            "include": (str,),
            "minimal_threshold": (int,),
            "minimal_threshold_overrides": ([ObservabilityPipelineSpikeProtectionProcessorThresholdOverride],),
            "name": (str,),
            "partition_fields": ([str],),
            "spike_action": (ObservabilityPipelineSpikeProtectionProcessorSpikeAction,),
            "spike_threshold": (float,),
            "type": (ObservabilityPipelineSpikeProtectionProcessorType,),
        }

    attribute_map = {
        "action_when_missing_partitions": "action_when_missing_partitions",
        "display_name": "display_name",
        "enabled": "enabled",
        "id": "id",
        "include": "include",
        "minimal_threshold": "minimal_threshold",
        "minimal_threshold_overrides": "minimal_threshold_overrides",
        "name": "name",
        "partition_fields": "partition_fields",
        "spike_action": "spike_action",
        "spike_threshold": "spike_threshold",
        "type": "type",
    }

    def __init__(
        self_,
        enabled: bool,
        id: str,
        include: str,
        name: str,
        spike_action: ObservabilityPipelineSpikeProtectionProcessorSpikeAction,
        type: ObservabilityPipelineSpikeProtectionProcessorType,
        action_when_missing_partitions: Union[
            ObservabilityPipelineSpikeProtectionProcessorActionWhenMissingPartitions, UnsetType
        ] = unset,
        display_name: Union[str, UnsetType] = unset,
        minimal_threshold: Union[int, UnsetType] = unset,
        minimal_threshold_overrides: Union[
            List[ObservabilityPipelineSpikeProtectionProcessorThresholdOverride], UnsetType
        ] = unset,
        partition_fields: Union[List[str], UnsetType] = unset,
        spike_threshold: Union[float, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``spike_protection`` processor learns the normal ingestion volume for the logs that match a specified filter and takes action when the volume spikes unexpectedly.

        **Supported pipeline types:** logs

        :param action_when_missing_partitions: How to handle logs that are missing one of the ``partition_fields``. Options:

            * ``ignore`` : Forward the event without applying spike protection.
            * ``default_bucket`` : Assign the event to a default partition.
        :type action_when_missing_partitions: ObservabilityPipelineSpikeProtectionProcessorActionWhenMissingPartitions, optional

        :param display_name: The display name for a component.
        :type display_name: str, optional

        :param enabled: Indicates whether the processor is enabled.
        :type enabled: bool

        :param id: The unique identifier for this component. Used in other parts of the pipeline to reference this component (for example, as the ``input`` to downstream components).
        :type id: str

        :param include: A Datadog search query used to determine which logs this processor targets.
        :type include: str

        :param minimal_threshold: The minimum volume, in bytes, that must be observed within 24 hours before spike protection can activate. Defaults to 100 GiB.
        :type minimal_threshold: int, optional

        :param minimal_threshold_overrides: A list of per-partition overrides for the minimal threshold, identified by matching field values. Requires ``partition_fields`` to be set.
        :type minimal_threshold_overrides: [ObservabilityPipelineSpikeProtectionProcessorThresholdOverride], optional

        :param name: Name of the spike protection rule.
        :type name: str

        :param partition_fields: A list of fields used to segment log traffic. Volume is learned and evaluated independently for each unique combination of these field values. A maximum of five fields is supported.
        :type partition_fields: [str], optional

        :param spike_action: The action to take with matching logs while spike protection is active. Options:

            * ``drop`` : Drop the event.
            * ``no_action`` : Let the event pass through.
            * ``overflow_routing`` : Route to an overflow destination.

            When ``overflow_routing`` is used, there must be a destination whose ``inputs`` reference this processor with the ``<processor-id>.overflow_events`` suffix to route the overflowing events.
        :type spike_action: ObservabilityPipelineSpikeProtectionProcessorSpikeAction

        :param spike_threshold: The number of standard deviations above the learned mean volume that must be exceeded before a spike is detected. Defaults to ``5``.
        :type spike_threshold: float, optional

        :param type: The processor type. The value should always be ``spike_protection``.
        :type type: ObservabilityPipelineSpikeProtectionProcessorType
        """
        if action_when_missing_partitions is not unset:
            kwargs["action_when_missing_partitions"] = action_when_missing_partitions
        if display_name is not unset:
            kwargs["display_name"] = display_name
        if minimal_threshold is not unset:
            kwargs["minimal_threshold"] = minimal_threshold
        if minimal_threshold_overrides is not unset:
            kwargs["minimal_threshold_overrides"] = minimal_threshold_overrides
        if partition_fields is not unset:
            kwargs["partition_fields"] = partition_fields
        if spike_threshold is not unset:
            kwargs["spike_threshold"] = spike_threshold
        super().__init__(kwargs)

        self_.enabled = enabled
        self_.id = id
        self_.include = include
        self_.name = name
        self_.spike_action = spike_action
        self_.type = type
