# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.observability_pipeline_parse_json_processor_type import (
        ObservabilityPipelineParseJSONProcessorType,
    )


class ObservabilityPipelineParseJSONProcessor(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_parse_json_processor_type import (
            ObservabilityPipelineParseJSONProcessorType,
        )

        return {
            "display_name": (str,),
            "enabled": (bool,),
            "field": (str,),
            "id": (str,),
            "include": (str,),
            "type": (ObservabilityPipelineParseJSONProcessorType,),
        }

    attribute_map = {
        "display_name": "display_name",
        "enabled": "enabled",
        "field": "field",
        "id": "id",
        "include": "include",
        "type": "type",
    }

    def __init__(
        self_,
        enabled: bool,
        field: str,
        id: str,
        include: str,
        type: ObservabilityPipelineParseJSONProcessorType,
        display_name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``parse_json`` processor extracts JSON from a specified field and flattens it into the event. This is useful when logs contain embedded JSON as a string.

        :param display_name: The display name for a component.
        :type display_name: str, optional

        :param enabled: Whether this processor is enabled.
        :type enabled: bool

        :param field: The name of the log field that contains a JSON string.
        :type field: str

        :param id: A unique identifier for this component. Used to reference this component in other parts of the pipeline (e.g., as input to downstream components).
        :type id: str

        :param include: A Datadog search query used to determine which logs this processor targets.
        :type include: str

        :param type: The processor type. The value should always be ``parse_json``.
        :type type: ObservabilityPipelineParseJSONProcessorType
        """
        if display_name is not unset:
            kwargs["display_name"] = display_name
        super().__init__(kwargs)

        self_.enabled = enabled
        self_.field = field
        self_.id = id
        self_.include = include
        self_.type = type
