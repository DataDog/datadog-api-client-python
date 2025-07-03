# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class LogsArrayProcessorOperation(ModelComposed):
    def __init__(self, **kwargs):
        """
        Configuration of the array processor operation to perform.

        :param preserve_source: Remove or preserve the remapped source element.
        :type preserve_source: bool, optional

        :param source: Attribute path containing the value to append.
        :type source: str

        :param target: Attribute path of the array to append to.
        :type target: str

        :param type: Operation type.
        :type type: LogsArrayProcessorOperationAppendType

        :param filter: Filter condition expressed as `key:value` used to find the matching element.
        :type filter: str

        :param value_to_extract: Key of the value to extract from the matching element.
        :type value_to_extract: str
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
        from datadog_api_client.v1.model.logs_array_processor_operation_append import LogsArrayProcessorOperationAppend
        from datadog_api_client.v1.model.logs_array_processor_operation_length import LogsArrayProcessorOperationLength
        from datadog_api_client.v1.model.logs_array_processor_operation_select import LogsArrayProcessorOperationSelect

        return {
            "oneOf": [
                LogsArrayProcessorOperationAppend,
                LogsArrayProcessorOperationLength,
                LogsArrayProcessorOperationSelect,
            ],
        }
