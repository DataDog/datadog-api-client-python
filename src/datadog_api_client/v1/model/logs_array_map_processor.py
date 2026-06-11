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
    from datadog_api_client.v1.model.logs_array_map_sub_processor import LogsArrayMapSubProcessor
    from datadog_api_client.v1.model.logs_array_map_processor_type import LogsArrayMapProcessorType
    from datadog_api_client.v1.model.logs_attribute_remapper import LogsAttributeRemapper
    from datadog_api_client.v1.model.logs_string_builder_processor import LogsStringBuilderProcessor
    from datadog_api_client.v1.model.logs_arithmetic_processor import LogsArithmeticProcessor
    from datadog_api_client.v1.model.logs_category_processor import LogsCategoryProcessor


class LogsArrayMapProcessor(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.logs_array_map_sub_processor import LogsArrayMapSubProcessor
        from datadog_api_client.v1.model.logs_array_map_processor_type import LogsArrayMapProcessorType

        return {
            "is_enabled": (bool,),
            "name": (str,),
            "preserve_source": (bool,),
            "processors": ([LogsArrayMapSubProcessor],),
            "source": (str,),
            "target": (str,),
            "type": (LogsArrayMapProcessorType,),
        }

    attribute_map = {
        "is_enabled": "is_enabled",
        "name": "name",
        "preserve_source": "preserve_source",
        "processors": "processors",
        "source": "source",
        "target": "target",
        "type": "type",
    }

    def __init__(
        self_,
        processors: List[
            Union[
                LogsArrayMapSubProcessor,
                LogsAttributeRemapper,
                LogsStringBuilderProcessor,
                LogsArithmeticProcessor,
                LogsCategoryProcessor,
            ]
        ],
        source: str,
        target: str,
        type: LogsArrayMapProcessorType,
        is_enabled: Union[bool, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        preserve_source: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        The array-map processor transforms each element of a source array by running
        sub-processors against it and writing results to a target array.
        Sub-processors reference the current element via ``$sourceElem`` (read) and
        ``$targetElem`` (write). Parent log attributes are read via plain paths as usual.
        Supported sub-processor types: ``attribute-remapper`` , ``string-builder-processor`` ,
        ``arithmetic-processor`` , ``category-processor``.
        ``is_enabled`` on sub-processors is ignored; sub-processor execution is gated
        entirely by the parent array-map's ``is_enabled`` flag.

        :param is_enabled: Whether or not the processor is enabled.
        :type is_enabled: bool, optional

        :param name: Name of the processor.
        :type name: str, optional

        :param preserve_source: When ``false`` and ``source != target`` , the source attribute is removed after
            processing. Cannot be ``false`` when ``source == target``.
        :type preserve_source: bool, optional

        :param processors: Sub-processors applied to each element. Allowed types: ``attribute-remapper`` ,
            ``string-builder-processor`` , ``arithmetic-processor`` , ``category-processor``.
        :type processors: [LogsArrayMapSubProcessor]

        :param source: Attribute path of the source array. Elements are read-only via ``$sourceElem``
            inside sub-processors.
        :type source: str

        :param target: Attribute path of the output array. Sub-processors write to ``$targetElem``
            (or ``$targetElem.<field>`` ) to build each output element.
        :type target: str

        :param type: Type of logs array-map processor.
        :type type: LogsArrayMapProcessorType
        """
        if is_enabled is not unset:
            kwargs["is_enabled"] = is_enabled
        if name is not unset:
            kwargs["name"] = name
        if preserve_source is not unset:
            kwargs["preserve_source"] = preserve_source
        super().__init__(kwargs)

        self_.processors = processors
        self_.source = source
        self_.target = target
        self_.type = type
