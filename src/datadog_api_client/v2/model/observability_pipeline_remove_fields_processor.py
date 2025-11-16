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
    from datadog_api_client.v2.model.observability_pipeline_remove_fields_processor_type import (
        ObservabilityPipelineRemoveFieldsProcessorType,
    )


class ObservabilityPipelineRemoveFieldsProcessor(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_remove_fields_processor_type import (
            ObservabilityPipelineRemoveFieldsProcessorType,
        )

        return {
            "enabled": (bool,),
            "fields": ([str],),
            "id": (str,),
            "include": (str,),
            "inputs": ([str],),
            "type": (ObservabilityPipelineRemoveFieldsProcessorType,),
        }

    attribute_map = {
        "enabled": "enabled",
        "fields": "fields",
        "id": "id",
        "include": "include",
        "inputs": "inputs",
        "type": "type",
    }

    def __init__(
        self_,
        fields: List[str],
        id: str,
        include: str,
        type: ObservabilityPipelineRemoveFieldsProcessorType,
        enabled: Union[bool, UnsetType] = unset,
        inputs: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``remove_fields`` processor deletes specified fields from logs.

        :param enabled: Whether this processor is enabled.
        :type enabled: bool, optional

        :param fields: A list of field names to be removed from each log event.
        :type fields: [str]

        :param id: The unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
        :type id: str

        :param include: A Datadog search query used to determine which logs this processor targets.
        :type include: str

        :param inputs: A list of component IDs whose output is used as input for this processor. Required when used as a standalone processor, omit when used within a processor group.
        :type inputs: [str], optional

        :param type: The processor type. The value should always be ``remove_fields``.
        :type type: ObservabilityPipelineRemoveFieldsProcessorType
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if inputs is not unset:
            kwargs["inputs"] = inputs
        super().__init__(kwargs)

        self_.fields = fields
        self_.id = id
        self_.include = include
        self_.type = type
