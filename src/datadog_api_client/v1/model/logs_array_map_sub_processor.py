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

        :param name: Name of the sub-processor.
        :type name: str, optional

        :param override_on_conflict: Override the target element if already set.
        :type override_on_conflict: bool, optional

        :param preserve_source: Remove or preserve the remapped source element.
        :type preserve_source: bool, optional

        :param sources: Array of source attribute paths.
        :type sources: [str]

        :param target: Target attribute path.
        :type target: str

        :param target_format: If the `target_type` of the remapper is `attribute`, try to cast the value to a new specific type.
            If the cast is not possible, the original type is kept. `string`, `integer`, or `double` are the possible types.
            If the `target_type` is `tag`, this parameter may not be specified.
        :type target_format: TargetFormatType, optional

        :param type: Type of logs attribute remapper.
        :type type: LogsAttributeRemapperType

        :param expression: Arithmetic operation to perform.
        :type expression: str

        :param is_replace_missing: Replace missing attribute values with 0.
        :type is_replace_missing: bool, optional

        :param template: Formula with one or more attributes and raw text.
        :type template: str

        :param categories: Array of filters to match against a log and the corresponding value to assign.
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
        from datadog_api_client.v1.model.logs_array_map_attribute_remapper import LogsArrayMapAttributeRemapper
        from datadog_api_client.v1.model.logs_array_map_arithmetic_sub_processor import (
            LogsArrayMapArithmeticSubProcessor,
        )
        from datadog_api_client.v1.model.logs_array_map_string_builder_sub_processor import (
            LogsArrayMapStringBuilderSubProcessor,
        )
        from datadog_api_client.v1.model.logs_array_map_category_sub_processor import LogsArrayMapCategorySubProcessor

        return {
            "oneOf": [
                LogsArrayMapAttributeRemapper,
                LogsArrayMapArithmeticSubProcessor,
                LogsArrayMapStringBuilderSubProcessor,
                LogsArrayMapCategorySubProcessor,
            ],
        }
