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
    from datadog_api_client.v1.model.logs_schema_mapper import LogsSchemaMapper
    from datadog_api_client.v1.model.logs_schema_data import LogsSchemaData
    from datadog_api_client.v1.model.logs_schema_processor_type import LogsSchemaProcessorType
    from datadog_api_client.v1.model.logs_schema_remapper import LogsSchemaRemapper
    from datadog_api_client.v1.model.logs_schema_category_mapper import LogsSchemaCategoryMapper


class LogsSchemaProcessor(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.logs_schema_mapper import LogsSchemaMapper
        from datadog_api_client.v1.model.logs_schema_data import LogsSchemaData
        from datadog_api_client.v1.model.logs_schema_processor_type import LogsSchemaProcessorType

        return {
            "is_enabled": (bool,),
            "mappers": ([LogsSchemaMapper],),
            "name": (str,),
            "schema": (LogsSchemaData,),
            "type": (LogsSchemaProcessorType,),
        }

    attribute_map = {
        "is_enabled": "is_enabled",
        "mappers": "mappers",
        "name": "name",
        "schema": "schema",
        "type": "type",
    }

    def __init__(
        self_,
        mappers: List[Union[LogsSchemaMapper, LogsSchemaRemapper, LogsSchemaCategoryMapper]],
        name: str,
        schema: LogsSchemaData,
        type: LogsSchemaProcessorType,
        is_enabled: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        A processor that has additional validations and checks for a given schema. Currently supported schema types include OCSF.

        :param is_enabled: Whether or not the processor is enabled.
        :type is_enabled: bool, optional

        :param mappers: The ``LogsSchemaProcessor`` ``mappers``.
        :type mappers: [LogsSchemaMapper]

        :param name: Name of the processor.
        :type name: str

        :param schema: Configuration of the schema data to use.
        :type schema: LogsSchemaData

        :param type: Type of logs schema processor.
        :type type: LogsSchemaProcessorType
        """
        if is_enabled is not unset:
            kwargs["is_enabled"] = is_enabled
        super().__init__(kwargs)

        self_.mappers = mappers
        self_.name = name
        self_.schema = schema
        self_.type = type
