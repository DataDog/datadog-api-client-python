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
    from datadog_api_client.v1.model.logs_exclude_attribute_processor_type import LogsExcludeAttributeProcessorType


class LogsExcludeAttributeProcessor(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.logs_exclude_attribute_processor_type import LogsExcludeAttributeProcessorType

        return {
            "attribute_to_exclude": (str,),
            "is_enabled": (bool,),
            "name": (str,),
            "type": (LogsExcludeAttributeProcessorType,),
        }

    attribute_map = {
        "attribute_to_exclude": "attribute_to_exclude",
        "is_enabled": "is_enabled",
        "name": "name",
        "type": "type",
    }

    def __init__(
        self_,
        attribute_to_exclude: str,
        type: LogsExcludeAttributeProcessorType,
        is_enabled: Union[bool, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Use this processor to remove an attribute from a log during processing.
        The processor strips the specified attribute from the log event, which is useful
        when the attribute contains sensitive data or is no longer needed downstream.

        :param attribute_to_exclude: Name of the log attribute to remove from the log event.
        :type attribute_to_exclude: str

        :param is_enabled: Whether or not the processor is enabled.
        :type is_enabled: bool, optional

        :param name: Name of the processor.
        :type name: str, optional

        :param type: Type of logs exclude attribute processor.
        :type type: LogsExcludeAttributeProcessorType
        """
        if is_enabled is not unset:
            kwargs["is_enabled"] = is_enabled
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)

        self_.attribute_to_exclude = attribute_to_exclude
        self_.type = type
