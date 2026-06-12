# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class LogsArrayMapSubProcessor(ModelComposed):
    def __init__(self, **kwargs):
        """
        A sub-processor used inside an array-map processor.
        Allowed types: ``attribute-remapper`` , ``string-builder-processor`` ,
        ``arithmetic-processor`` , ``category-processor``.

        :param is_enabled: Whether or not the processor is enabled.
        :type is_enabled: bool, optional

        :param name: Name of the processor.
        :type name: str, optional

        :param override_on_conflict: Override or not the target element if already set,
        :type override_on_conflict: bool, optional

        :param preserve_source: Remove or preserve the remapped source element.
        :type preserve_source: bool, optional

        :param source_type: Defines if the sources are from log `attribute` or `tag`.
        :type source_type: str, optional

        :param sources: Array of source attributes.
        :type sources: [str]

        :param target: Final attribute or tag name to remap the sources to.
        :type target: str

        :param target_format: If the `target_type` of the remapper is `attribute`, try to cast the value to a new specific type.
            If the cast is not possible, the original type is kept. `string`, `integer`, or `double` are the possible types.
            If the `target_type` is `tag`, this parameter may not be specified.
        :type target_format: TargetFormatType, optional

        :param target_type: Defines if the final attribute or tag name is from log `attribute` or `tag`.
        :type target_type: str, optional

        :param type: Type of logs attribute remapper.
        :type type: LogsAttributeRemapperType

        :param is_replace_missing: If true, it replaces all missing attributes of `template` by an empty string.
            If `false` (default), skips the operation for missing attributes.
        :type is_replace_missing: bool, optional

        :param template: A formula with one or more attributes and raw text.
        :type template: str

        :param expression: Arithmetic operation between one or more log attributes.
        :type expression: str

        :param categories: Array of filters to match or not a log and their
            corresponding `name` to assign a custom value to the log.
        :type categories: [LogsCategoryProcessorCategory]
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
        from datadog_api_client.v1.model.logs_attribute_remapper import LogsAttributeRemapper
        from datadog_api_client.v1.model.logs_string_builder_processor import LogsStringBuilderProcessor
        from datadog_api_client.v1.model.logs_arithmetic_processor import LogsArithmeticProcessor
        from datadog_api_client.v1.model.logs_category_processor import LogsCategoryProcessor

        return {
            "oneOf": [
                LogsAttributeRemapper,
                LogsStringBuilderProcessor,
                LogsArithmeticProcessor,
                LogsCategoryProcessor,
            ],
        }
