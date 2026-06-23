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
    from datadog_api_client.v1.model.logs_arithmetic_processor_type import LogsArithmeticProcessorType


class LogsArrayMapArithmeticSubProcessor(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.logs_arithmetic_processor_type import LogsArithmeticProcessorType

        return {
            "expression": (str,),
            "is_replace_missing": (bool,),
            "name": (str,),
            "target": (str,),
            "type": (LogsArithmeticProcessorType,),
        }

    attribute_map = {
        "expression": "expression",
        "is_replace_missing": "is_replace_missing",
        "name": "name",
        "target": "target",
        "type": "type",
    }

    def __init__(
        self_,
        expression: str,
        target: str,
        type: LogsArithmeticProcessorType,
        is_replace_missing: Union[bool, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        An arithmetic sub-processor for use inside an array-map processor.
        Unlike the top-level arithmetic processor, ``is_enabled`` is not supported.

        :param expression: Arithmetic operation to perform.
        :type expression: str

        :param is_replace_missing: Replace missing attribute values with 0.
        :type is_replace_missing: bool, optional

        :param name: Name of the sub-processor.
        :type name: str, optional

        :param target: Target attribute path for the result.
        :type target: str

        :param type: Type of logs arithmetic processor.
        :type type: LogsArithmeticProcessorType
        """
        if is_replace_missing is not unset:
            kwargs["is_replace_missing"] = is_replace_missing
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)

        self_.expression = expression
        self_.target = target
        self_.type = type
