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
    from datadog_api_client.v2.model.observability_pipeline_parse_grok_processor_rule import (
        ObservabilityPipelineParseGrokProcessorRule,
    )
    from datadog_api_client.v2.model.observability_pipeline_parse_grok_processor_type import (
        ObservabilityPipelineParseGrokProcessorType,
    )


class ObservabilityPipelineParseGrokProcessor(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_parse_grok_processor_rule import (
            ObservabilityPipelineParseGrokProcessorRule,
        )
        from datadog_api_client.v2.model.observability_pipeline_parse_grok_processor_type import (
            ObservabilityPipelineParseGrokProcessorType,
        )

        return {
            "disable_library_rules": (bool,),
            "id": (str,),
            "include": (str,),
            "inputs": ([str],),
            "rules": ([ObservabilityPipelineParseGrokProcessorRule],),
            "type": (ObservabilityPipelineParseGrokProcessorType,),
        }

    attribute_map = {
        "disable_library_rules": "disable_library_rules",
        "id": "id",
        "include": "include",
        "inputs": "inputs",
        "rules": "rules",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        include: str,
        inputs: List[str],
        rules: List[ObservabilityPipelineParseGrokProcessorRule],
        type: ObservabilityPipelineParseGrokProcessorType,
        disable_library_rules: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``parse_grok`` processor extracts structured fields from unstructured log messages using Grok patterns.

        :param disable_library_rules: If set to ``true`` , disables the default Grok rules provided by Datadog.
        :type disable_library_rules: bool, optional

        :param id: A unique identifier for this processor.
        :type id: str

        :param include: A Datadog search query used to determine which logs this processor targets.
        :type include: str

        :param inputs: A list of component IDs whose output is used as the ``input`` for this component.
        :type inputs: [str]

        :param rules: The list of Grok parsing rules. If multiple matching rules are provided, they are evaluated in order. The first successful match is applied.
        :type rules: [ObservabilityPipelineParseGrokProcessorRule]

        :param type: The processor type. The value should always be ``parse_grok``.
        :type type: ObservabilityPipelineParseGrokProcessorType
        """
        if disable_library_rules is not unset:
            kwargs["disable_library_rules"] = disable_library_rules
        super().__init__(kwargs)

        self_.id = id
        self_.include = include
        self_.inputs = inputs
        self_.rules = rules
        self_.type = type
