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
    from datadog_api_client.v1.model.target_format_type import TargetFormatType
    from datadog_api_client.v1.model.logs_schema_remapper_type import LogsSchemaRemapperType


class LogsSchemaRemapper(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.target_format_type import TargetFormatType
        from datadog_api_client.v1.model.logs_schema_remapper_type import LogsSchemaRemapperType

        return {
            "name": (str,),
            "override_on_conflict": (bool,),
            "preserve_source": (bool,),
            "sources": ([str],),
            "target": (str,),
            "target_format": (TargetFormatType,),
            "type": (LogsSchemaRemapperType,),
        }

    attribute_map = {
        "name": "name",
        "override_on_conflict": "override_on_conflict",
        "preserve_source": "preserve_source",
        "sources": "sources",
        "target": "target",
        "target_format": "target_format",
        "type": "type",
    }

    def __init__(
        self_,
        name: str,
        sources: List[str],
        target: str,
        type: LogsSchemaRemapperType,
        override_on_conflict: Union[bool, UnsetType] = unset,
        preserve_source: Union[bool, UnsetType] = unset,
        target_format: Union[TargetFormatType, UnsetType] = unset,
        **kwargs,
    ):
        """
        The schema remapper maps source log fields to their correct fields.

        :param name: Name of the logs schema remapper.
        :type name: str

        :param override_on_conflict: Override or not the target element if already set.
        :type override_on_conflict: bool, optional

        :param preserve_source: Remove or preserve the remapped source element.
        :type preserve_source: bool, optional

        :param sources: Array of source attributes.
        :type sources: [str]

        :param target: Target field to map log source field to.
        :type target: str

        :param target_format: If the ``target_type`` of the remapper is ``attribute`` , try to cast the value to a new specific type.
            If the cast is not possible, the original type is kept. ``string`` , ``integer`` , or ``double`` are the possible types.
            If the ``target_type`` is ``tag`` , this parameter may not be specified.
        :type target_format: TargetFormatType, optional

        :param type: Type of logs schema remapper.
        :type type: LogsSchemaRemapperType
        """
        if override_on_conflict is not unset:
            kwargs["override_on_conflict"] = override_on_conflict
        if preserve_source is not unset:
            kwargs["preserve_source"] = preserve_source
        if target_format is not unset:
            kwargs["target_format"] = target_format
        super().__init__(kwargs)

        self_.name = name
        self_.sources = sources
        self_.target = target
        self_.type = type
