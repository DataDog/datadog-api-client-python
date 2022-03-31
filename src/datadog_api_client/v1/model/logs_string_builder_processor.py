# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.logs_string_builder_processor_type import LogsStringBuilderProcessorType

    globals()["LogsStringBuilderProcessorType"] = LogsStringBuilderProcessorType


class LogsStringBuilderProcessor(ModelNormal):
    @cached_property
    def openapi_types(_):
        lazy_import()
        return {
            "is_enabled": (bool,),
            "is_replace_missing": (bool,),
            "name": (str,),
            "target": (str,),
            "template": (str,),
            "type": (LogsStringBuilderProcessorType,),
        }

    attribute_map = {
        "is_enabled": "is_enabled",
        "is_replace_missing": "is_replace_missing",
        "name": "name",
        "target": "target",
        "template": "template",
        "type": "type",
    }

    def __init__(self, target, template, type, *args, **kwargs):
        """
        Use the string builder processor to add a new attribute (without spaces or special characters)
        to a log with the result of the provided template.
        This enables aggregation of different attributes or raw strings into a single attribute.

        The template is defined by both raw text and blocks with the syntax `%{attribute_path}`.

        **Notes**:

        - The processor only accepts attributes with values or an array of values in the blocks.
        - If an attribute cannot be used (object or array of object),
          it is replaced by an empty string or the entire operation is skipped depending on your selection.
        - If the target attribute already exists, it is overwritten by the result of the template.
        - Results of the template cannot exceed 256 characters.

        :param is_enabled: Whether or not the processor is enabled.
        :type is_enabled: bool, optional

        :param is_replace_missing: If true, it replaces all missing attributes of `template` by an empty string.
            If `false` (default), skips the operation for missing attributes.
        :type is_replace_missing: bool, optional

        :param name: Name of the processor.
        :type name: str, optional

        :param target: The name of the attribute that contains the result of the template.
        :type target: str

        :param template: A formula with one or more attributes and raw text.
        :type template: str

        :param type: Type of logs string builder processor.
        :type type: LogsStringBuilderProcessorType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.target = target
        self.template = template
        self.type = type

    @classmethod
    def _from_openapi_data(cls, target, template, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsStringBuilderProcessor, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.target = target
        self.template = template
        self.type = type
        return self
