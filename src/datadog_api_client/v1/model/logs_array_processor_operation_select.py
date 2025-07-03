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
    from datadog_api_client.v1.model.logs_array_processor_operation_select_type import (
        LogsArrayProcessorOperationSelectType,
    )


class LogsArrayProcessorOperationSelect(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.logs_array_processor_operation_select_type import (
            LogsArrayProcessorOperationSelectType,
        )

        return {
            "filter": (str,),
            "source": (str,),
            "target": (str,),
            "type": (LogsArrayProcessorOperationSelectType,),
            "value_to_extract": (str,),
        }

    attribute_map = {
        "filter": "filter",
        "source": "source",
        "target": "target",
        "type": "type",
        "value_to_extract": "value_to_extract",
    }

    def __init__(
        self_,
        filter: str,
        source: str,
        target: str,
        type: LogsArrayProcessorOperationSelectType,
        value_to_extract: str,
        **kwargs,
    ):
        """
        Operation that finds an object in a ``source`` array using a ``filter`` , and then extracts a specific value into the ``target`` attribute.

        :param filter: Filter condition expressed as ``key:value`` used to find the matching element.
        :type filter: str

        :param source: Attribute path of the array to search into.
        :type source: str

        :param target: Attribute that receives the extracted value.
        :type target: str

        :param type: Operation type.
        :type type: LogsArrayProcessorOperationSelectType

        :param value_to_extract: Key of the value to extract from the matching element.
        :type value_to_extract: str
        """
        super().__init__(kwargs)

        self_.filter = filter
        self_.source = source
        self_.target = target
        self_.type = type
        self_.value_to_extract = value_to_extract
