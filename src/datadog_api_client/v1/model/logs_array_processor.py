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
    from datadog_api_client.v1.model.logs_array_processor_operation import LogsArrayProcessorOperation
    from datadog_api_client.v1.model.logs_array_processor_type import LogsArrayProcessorType
    from datadog_api_client.v1.model.logs_array_processor_operation_append import LogsArrayProcessorOperationAppend
    from datadog_api_client.v1.model.logs_array_processor_operation_length import LogsArrayProcessorOperationLength
    from datadog_api_client.v1.model.logs_array_processor_operation_select import LogsArrayProcessorOperationSelect


class LogsArrayProcessor(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.logs_array_processor_operation import LogsArrayProcessorOperation
        from datadog_api_client.v1.model.logs_array_processor_type import LogsArrayProcessorType

        return {
            "is_enabled": (bool,),
            "name": (str,),
            "operation": (LogsArrayProcessorOperation,),
            "type": (LogsArrayProcessorType,),
        }

    attribute_map = {
        "is_enabled": "is_enabled",
        "name": "name",
        "operation": "operation",
        "type": "type",
    }

    def __init__(
        self_,
        operation: Union[
            LogsArrayProcessorOperation,
            LogsArrayProcessorOperationAppend,
            LogsArrayProcessorOperationLength,
            LogsArrayProcessorOperationSelect,
        ],
        type: LogsArrayProcessorType,
        is_enabled: Union[bool, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A processor for extracting, aggregating, or transforming values from JSON arrays within your logs.
        Supported operations are:

        * Select value from matching element
        * Compute array length
        * Append a value to an array

        :param is_enabled: Whether or not the processor is enabled.
        :type is_enabled: bool, optional

        :param name: Name of the processor.
        :type name: str, optional

        :param operation: Configuration of the array processor operation to perform.
        :type operation: LogsArrayProcessorOperation

        :param type: Type of logs array processor.
        :type type: LogsArrayProcessorType
        """
        if is_enabled is not unset:
            kwargs["is_enabled"] = is_enabled
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)

        self_.operation = operation
        self_.type = type
