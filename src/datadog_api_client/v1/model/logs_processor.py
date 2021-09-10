# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
)


def lazy_import():
    from datadog_api_client.v1.model.logs_arithmetic_processor import LogsArithmeticProcessor
    from datadog_api_client.v1.model.logs_attribute_remapper import LogsAttributeRemapper
    from datadog_api_client.v1.model.logs_category_processor import LogsCategoryProcessor
    from datadog_api_client.v1.model.logs_category_processor_category import LogsCategoryProcessorCategory
    from datadog_api_client.v1.model.logs_date_remapper import LogsDateRemapper
    from datadog_api_client.v1.model.logs_filter import LogsFilter
    from datadog_api_client.v1.model.logs_geo_ip_parser import LogsGeoIPParser
    from datadog_api_client.v1.model.logs_grok_parser import LogsGrokParser
    from datadog_api_client.v1.model.logs_grok_parser_rules import LogsGrokParserRules
    from datadog_api_client.v1.model.logs_lookup_processor import LogsLookupProcessor
    from datadog_api_client.v1.model.logs_message_remapper import LogsMessageRemapper
    from datadog_api_client.v1.model.logs_pipeline_processor import LogsPipelineProcessor
    from datadog_api_client.v1.model.logs_service_remapper import LogsServiceRemapper
    from datadog_api_client.v1.model.logs_status_remapper import LogsStatusRemapper
    from datadog_api_client.v1.model.logs_string_builder_processor import LogsStringBuilderProcessor
    from datadog_api_client.v1.model.logs_trace_remapper import LogsTraceRemapper
    from datadog_api_client.v1.model.logs_trace_remapper_type import LogsTraceRemapperType
    from datadog_api_client.v1.model.logs_url_parser import LogsURLParser
    from datadog_api_client.v1.model.logs_user_agent_parser import LogsUserAgentParser
    from datadog_api_client.v1.model.target_format_type import TargetFormatType

    globals()["LogsArithmeticProcessor"] = LogsArithmeticProcessor
    globals()["LogsAttributeRemapper"] = LogsAttributeRemapper
    globals()["LogsCategoryProcessor"] = LogsCategoryProcessor
    globals()["LogsCategoryProcessorCategory"] = LogsCategoryProcessorCategory
    globals()["LogsDateRemapper"] = LogsDateRemapper
    globals()["LogsFilter"] = LogsFilter
    globals()["LogsGeoIPParser"] = LogsGeoIPParser
    globals()["LogsGrokParser"] = LogsGrokParser
    globals()["LogsGrokParserRules"] = LogsGrokParserRules
    globals()["LogsLookupProcessor"] = LogsLookupProcessor
    globals()["LogsMessageRemapper"] = LogsMessageRemapper
    globals()["LogsPipelineProcessor"] = LogsPipelineProcessor
    globals()["LogsServiceRemapper"] = LogsServiceRemapper
    globals()["LogsStatusRemapper"] = LogsStatusRemapper
    globals()["LogsStringBuilderProcessor"] = LogsStringBuilderProcessor
    globals()["LogsTraceRemapper"] = LogsTraceRemapper
    globals()["LogsTraceRemapperType"] = LogsTraceRemapperType
    globals()["LogsURLParser"] = LogsURLParser
    globals()["LogsUserAgentParser"] = LogsUserAgentParser
    globals()["TargetFormatType"] = TargetFormatType


class LogsProcessor(ModelComposed):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {}

    validations = {
        ("samples",): {
            "max_items": 5,
        },
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {}

    discriminator = None

    attribute_map = {}

    read_only_vars = {}

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """LogsProcessor - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            is_enabled (bool): Whether or not the processor is enabled.. [optional] if omitted the server will use the default value of False  # noqa: E501
            name (str): Name of the processor.. [optional]  # noqa: E501
            samples ([str]): List of sample logs to test this grok parser.. [optional]  # noqa: E501
            override_on_conflict (bool): Override or not the target element if already set,. [optional] if omitted the server will use the default value of False  # noqa: E501
            preserve_source (bool): Remove or preserve the remapped source element.. [optional] if omitted the server will use the default value of False  # noqa: E501
            source_type (str): Defines if the sources are from log `attribute` or `tag`.. [optional] if omitted the server will use the default value of "attribute"  # noqa: E501
            target_format (TargetFormatType): [optional]  # noqa: E501
            target_type (str): Defines if the final attribute or tag name is from log `attribute` or `tag`.. [optional] if omitted the server will use the default value of "attribute"  # noqa: E501
            normalize_ending_slashes (bool, none_type): Normalize the ending slashes or not.. [optional] if omitted the server will use the default value of False  # noqa: E501
            is_encoded (bool): Define if the source attribute is URL encoded or not.. [optional] if omitted the server will use the default value of False  # noqa: E501
            is_replace_missing (bool): If true, it replaces all missing attributes of `template` by an empty string. If `false` (default), skips the operation for missing attributes.. [optional] if omitted the server will use the default value of False  # noqa: E501
            filter (LogsFilter): [optional]  # noqa: E501
            processors ([LogsProcessor]): Ordered list of processors in this pipeline.. [optional]  # noqa: E501
            default_lookup (str): Value to set the target attribute if the source value is not found in the list.. [optional]  # noqa: E501
            grok (LogsGrokParserRules): [optional]  # noqa: E501
            source (str): Source attribute used to perform the lookup.. [optional]  # noqa: E501
            type (LogsTraceRemapperType): [optional]  # noqa: E501
            sources ([str]): Array of source attributes.. [optional] if omitted the server will use the default value of ["dd.trace_id"]  # noqa: E501
            target (str): Name of the attribute that contains the corresponding value in the mapping list or the `default_lookup` if not found in the mapping list.. [optional]  # noqa: E501
            categories ([LogsCategoryProcessorCategory]): Array of filters to match or not a log and their corresponding `name`to assign a custom value to the log.. [optional]  # noqa: E501
            expression (str): Arithmetic operation between one or more log attributes.. [optional]  # noqa: E501
            template (str): A formula with one or more attributes and raw text.. [optional]  # noqa: E501
            lookup_table ([str]): Mapping table of values for the source attribute and their associated target attribute values, formatted as `[\"source_key1,target_value1\", \"source_key2,target_value2\"]`. [optional]  # noqa: E501
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Helper creating a new instance from a response."""

        self = super(LogsProcessor, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self

    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
            "anyOf": [],
            "allOf": [],
            "oneOf": [
                LogsArithmeticProcessor,
                LogsAttributeRemapper,
                LogsCategoryProcessor,
                LogsDateRemapper,
                LogsGeoIPParser,
                LogsGrokParser,
                LogsLookupProcessor,
                LogsMessageRemapper,
                LogsPipelineProcessor,
                LogsServiceRemapper,
                LogsStatusRemapper,
                LogsStringBuilderProcessor,
                LogsTraceRemapper,
                LogsURLParser,
                LogsUserAgentParser,
            ],
        }
