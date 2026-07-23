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
    from datadog_api_client.v1.model.logs_array_processor_operation_extract_key_value_type import (
        LogsArrayProcessorOperationExtractKeyValueType,
    )


class LogsArrayProcessorOperationExtractKeyValue(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.logs_array_processor_operation_extract_key_value_type import (
            LogsArrayProcessorOperationExtractKeyValueType,
        )

        return {
            "key_to_extract": (str,),
            "override_on_conflict": (bool,),
            "source": (str,),
            "target": (str,),
            "type": (LogsArrayProcessorOperationExtractKeyValueType,),
            "value_to_extract": (str,),
        }

    attribute_map = {
        "key_to_extract": "key_to_extract",
        "override_on_conflict": "override_on_conflict",
        "source": "source",
        "target": "target",
        "type": "type",
        "value_to_extract": "value_to_extract",
    }

    def __init__(
        self_,
        key_to_extract: str,
        source: str,
        type: LogsArrayProcessorOperationExtractKeyValueType,
        value_to_extract: str,
        override_on_conflict: Union[bool, UnsetType] = unset,
        target: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Operation that extracts key-value pairs from a ``source`` array and stores the result in the ``target`` attribute.

        :param key_to_extract: Key of the attribute in each array element that holds the name to use for the extracted attribute.
        :type key_to_extract: str

        :param override_on_conflict: Whether to override the target element if it's already set.
        :type override_on_conflict: bool, optional

        :param source: Attribute path of the array to extract key-value pairs from.
        :type source: str

        :param target: Attribute that receives the extracted key-value pairs. If not specified, the extracted attributes are added at the root level of the log.
        :type target: str, optional

        :param type: Operation type.
        :type type: LogsArrayProcessorOperationExtractKeyValueType

        :param value_to_extract: Key of the attribute in each array element that holds the value to use for the extracted attribute.
        :type value_to_extract: str
        """
        if override_on_conflict is not unset:
            kwargs["override_on_conflict"] = override_on_conflict
        if target is not unset:
            kwargs["target"] = target
        super().__init__(kwargs)

        self_.key_to_extract = key_to_extract
        self_.source = source
        self_.type = type
        self_.value_to_extract = value_to_extract
