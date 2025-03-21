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
    from datadog_api_client.v1.model.logs_span_remapper_type import LogsSpanRemapperType


class LogsSpanRemapper(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.logs_span_remapper_type import LogsSpanRemapperType

        return {
            "is_enabled": (bool,),
            "name": (str,),
            "sources": ([str],),
            "type": (LogsSpanRemapperType,),
        }

    attribute_map = {
        "is_enabled": "is_enabled",
        "name": "name",
        "sources": "sources",
        "type": "type",
    }

    def __init__(
        self_,
        type: LogsSpanRemapperType,
        is_enabled: Union[bool, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        sources: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        There are two ways to define correlation between application spans and logs:

        #.
           Follow the documentation on `how to inject a span ID in the application logs <https://docs.datadoghq.com/tracing/connect_logs_and_traces>`_.
           Log integrations automatically handle all remaining setup steps by default.

        #.
           Use the span remapper processor to define a log attribute as its associated span ID.

        :param is_enabled: Whether or not the processor is enabled.
        :type is_enabled: bool, optional

        :param name: Name of the processor.
        :type name: str, optional

        :param sources: Array of source attributes.
        :type sources: [str], optional

        :param type: Type of logs span remapper.
        :type type: LogsSpanRemapperType
        """
        if is_enabled is not unset:
            kwargs["is_enabled"] = is_enabled
        if name is not unset:
            kwargs["name"] = name
        if sources is not unset:
            kwargs["sources"] = sources
        super().__init__(kwargs)

        self_.type = type
