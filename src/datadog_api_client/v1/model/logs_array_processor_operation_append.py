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
    from datadog_api_client.v1.model.logs_array_processor_operation_append_type import (
        LogsArrayProcessorOperationAppendType,
    )


class LogsArrayProcessorOperationAppend(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.logs_array_processor_operation_append_type import (
            LogsArrayProcessorOperationAppendType,
        )

        return {
            "preserve_source": (bool,),
            "source": (str,),
            "target": (str,),
            "type": (LogsArrayProcessorOperationAppendType,),
        }

    attribute_map = {
        "preserve_source": "preserve_source",
        "source": "source",
        "target": "target",
        "type": "type",
    }

    def __init__(
        self_,
        source: str,
        target: str,
        type: LogsArrayProcessorOperationAppendType,
        preserve_source: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Operation that appends a value to a target array attribute.

        :param preserve_source: Remove or preserve the remapped source element.
        :type preserve_source: bool, optional

        :param source: Attribute path containing the value to append.
        :type source: str

        :param target: Attribute path of the array to append to.
        :type target: str

        :param type: Operation type.
        :type type: LogsArrayProcessorOperationAppendType
        """
        if preserve_source is not unset:
            kwargs["preserve_source"] = preserve_source
        super().__init__(kwargs)

        self_.source = source
        self_.target = target
        self_.type = type
