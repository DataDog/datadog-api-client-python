# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.logs_array_processor_operation_length_type import (
        LogsArrayProcessorOperationLengthType,
    )


class LogsArrayProcessorOperationLength(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.logs_array_processor_operation_length_type import (
            LogsArrayProcessorOperationLengthType,
        )

        return {
            "source": (str,),
            "target": (str,),
            "type": (LogsArrayProcessorOperationLengthType,),
        }

    attribute_map = {
        "source": "source",
        "target": "target",
        "type": "type",
    }

    def __init__(self_, source: str, target: str, type: LogsArrayProcessorOperationLengthType, **kwargs):
        """
        Operation that computes the length of a ``source`` array and stores the result in the ``target`` attribute.

        :param source: Attribute path of the array to measure.
        :type source: str

        :param target: Attribute that receives the computed length.
        :type target: str

        :param type: Operation type.
        :type type: LogsArrayProcessorOperationLengthType
        """
        super().__init__(kwargs)

        self_.source = source
        self_.target = target
        self_.type = type
