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
    from datadog_api_client.v1.model.logs_string_builder_processor_type import LogsStringBuilderProcessorType


class LogsArrayMapStringBuilderSubProcessor(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.logs_string_builder_processor_type import LogsStringBuilderProcessorType

        return {
            "is_replace_missing": (bool,),
            "name": (str,),
            "target": (str,),
            "template": (str,),
            "type": (LogsStringBuilderProcessorType,),
        }

    attribute_map = {
        "is_replace_missing": "is_replace_missing",
        "name": "name",
        "target": "target",
        "template": "template",
        "type": "type",
    }

    def __init__(
        self_,
        target: str,
        template: str,
        type: LogsStringBuilderProcessorType,
        is_replace_missing: Union[bool, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A string builder sub-processor for use inside an array-map processor.
        Unlike the top-level string builder processor, ``is_enabled`` is not supported.

        :param is_replace_missing: Replace missing attribute values with an empty string.
        :type is_replace_missing: bool, optional

        :param name: Name of the sub-processor.
        :type name: str, optional

        :param target: Target attribute path for the result.
        :type target: str

        :param template: Formula with one or more attributes and raw text.
        :type template: str

        :param type: Type of logs string builder processor.
        :type type: LogsStringBuilderProcessorType
        """
        if is_replace_missing is not unset:
            kwargs["is_replace_missing"] = is_replace_missing
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)

        self_.target = target
        self_.template = template
        self_.type = type
