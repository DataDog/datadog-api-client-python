# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class LogsSchemaMapper(ModelComposed):
    def __init__(self, **kwargs):
        """
        Configuration of the schema processor mapper to use.

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

        :param target_format: If the `target_type` of the remapper is `attribute`, try to cast the value to a new specific type.
            If the cast is not possible, the original type is kept. `string`, `integer`, or `double` are the possible types.
            If the `target_type` is `tag`, this parameter may not be specified.
        :type target_format: TargetFormatType, optional

        :param type: Type of logs schema remapper.
        :type type: LogsSchemaRemapperType

        :param categories: Array of filters to match or not a log and their
            corresponding `name` to assign a custom value to the log.
        :type categories: [LogsSchemaCategoryMapperCategory]

        :param fallback: Used to override hardcoded category values with a value pulled from a source attribute on the log.
        :type fallback: LogsSchemaCategoryMapperFallback, optional

        :param targets: Name of the target attributes which value is defined by the matching category.
        :type targets: LogsSchemaCategoryMapperTargets
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v1.model.logs_schema_remapper import LogsSchemaRemapper
        from datadog_api_client.v1.model.logs_schema_category_mapper import LogsSchemaCategoryMapper

        return {
            "oneOf": [
                LogsSchemaRemapper,
                LogsSchemaCategoryMapper,
            ],
        }
