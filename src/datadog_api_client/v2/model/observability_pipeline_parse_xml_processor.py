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
    from datadog_api_client.v2.model.observability_pipeline_parse_xml_processor_type import (
        ObservabilityPipelineParseXMLProcessorType,
    )


class ObservabilityPipelineParseXMLProcessor(ModelNormal):
    validations = {
        "text_key": {
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_parse_xml_processor_type import (
            ObservabilityPipelineParseXMLProcessorType,
        )

        return {
            "always_use_text_key": (bool,),
            "attr_prefix": (str,),
            "display_name": (str,),
            "enabled": (bool,),
            "field": (str,),
            "id": (str,),
            "include": (str,),
            "include_attr": (bool,),
            "parse_bool": (bool,),
            "parse_null": (bool,),
            "parse_number": (bool,),
            "text_key": (str,),
            "type": (ObservabilityPipelineParseXMLProcessorType,),
        }

    attribute_map = {
        "always_use_text_key": "always_use_text_key",
        "attr_prefix": "attr_prefix",
        "display_name": "display_name",
        "enabled": "enabled",
        "field": "field",
        "id": "id",
        "include": "include",
        "include_attr": "include_attr",
        "parse_bool": "parse_bool",
        "parse_null": "parse_null",
        "parse_number": "parse_number",
        "text_key": "text_key",
        "type": "type",
    }

    def __init__(
        self_,
        enabled: bool,
        field: str,
        id: str,
        include: str,
        type: ObservabilityPipelineParseXMLProcessorType,
        always_use_text_key: Union[bool, UnsetType] = unset,
        attr_prefix: Union[str, UnsetType] = unset,
        display_name: Union[str, UnsetType] = unset,
        include_attr: Union[bool, UnsetType] = unset,
        parse_bool: Union[bool, UnsetType] = unset,
        parse_null: Union[bool, UnsetType] = unset,
        parse_number: Union[bool, UnsetType] = unset,
        text_key: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``parse_xml`` processor parses XML from a specified field and extracts it into the event.

        **Supported pipeline types:** logs

        :param always_use_text_key: Whether to always use a text key for element content.
        :type always_use_text_key: bool, optional

        :param attr_prefix: The prefix to use for XML attributes in the parsed output.
        :type attr_prefix: str, optional

        :param display_name: The display name for a component.
        :type display_name: str, optional

        :param enabled: Whether this processor is enabled.
        :type enabled: bool

        :param field: The name of the log field that contains an XML string.
        :type field: str

        :param id: The unique identifier for this component. Used to reference this component in other parts of the pipeline (for example, as the ``input`` to downstream components).
        :type id: str

        :param include: A Datadog search query used to determine which logs this processor targets.
        :type include: str

        :param include_attr: Whether to include XML attributes in the parsed output.
        :type include_attr: bool, optional

        :param parse_bool: Whether to parse boolean values from strings.
        :type parse_bool: bool, optional

        :param parse_null: Whether to parse null values.
        :type parse_null: bool, optional

        :param parse_number: Whether to parse numeric values from strings.
        :type parse_number: bool, optional

        :param text_key: The key name to use for text content within XML elements. Must be at least 1 character if specified.
        :type text_key: str, optional

        :param type: The processor type. The value should always be ``parse_xml``.
        :type type: ObservabilityPipelineParseXMLProcessorType
        """
        if always_use_text_key is not unset:
            kwargs["always_use_text_key"] = always_use_text_key
        if attr_prefix is not unset:
            kwargs["attr_prefix"] = attr_prefix
        if display_name is not unset:
            kwargs["display_name"] = display_name
        if include_attr is not unset:
            kwargs["include_attr"] = include_attr
        if parse_bool is not unset:
            kwargs["parse_bool"] = parse_bool
        if parse_null is not unset:
            kwargs["parse_null"] = parse_null
        if parse_number is not unset:
            kwargs["parse_number"] = parse_number
        if text_key is not unset:
            kwargs["text_key"] = text_key
        super().__init__(kwargs)

        self_.enabled = enabled
        self_.field = field
        self_.id = id
        self_.include = include
        self_.type = type
