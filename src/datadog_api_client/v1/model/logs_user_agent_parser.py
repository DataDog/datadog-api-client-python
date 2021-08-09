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
    from datadog_api_client.v1.model.logs_user_agent_parser_type import LogsUserAgentParserType

    globals()["LogsUserAgentParserType"] = LogsUserAgentParserType


class LogsUserAgentParser(ModelNormal):
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

    validations = {}

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
        lazy_import()
        return {
            "sources": ([str],),  # noqa: E501
            "target": (str,),  # noqa: E501
            "type": (LogsUserAgentParserType,),  # noqa: E501
            "is_enabled": (bool,),  # noqa: E501
            "is_encoded": (bool,),  # noqa: E501
            "name": (str,),  # noqa: E501
        }

    discriminator = None

    attribute_map = {
        "sources": "sources",  # noqa: E501
        "target": "target",  # noqa: E501
        "type": "type",  # noqa: E501
        "is_enabled": "is_enabled",  # noqa: E501
        "is_encoded": "is_encoded",  # noqa: E501
        "name": "name",  # noqa: E501
    }

    read_only_vars = {}

    _composed_schemas = {}

    @convert_js_args_to_python_args
    def __init__(self, type, *args, **kwargs):  # noqa: E501
        """LogsUserAgentParser - a model defined in OpenAPI

        Args:
            type (LogsUserAgentParserType):

        Keyword Args:
            sources ([str]): Array of source attributes.. defaults to ["http.useragent"]  # noqa: E501
            target (str): Name of the parent attribute that contains all the extracted details from the `sources`.. defaults to "http.useragent_details"  # noqa: E501
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
            is_encoded (bool): Define if the source attribute is URL encoded or not.. [optional] if omitted the server will use the default value of False  # noqa: E501
            name (str): Name of the processor.. [optional]  # noqa: E501
        """
        super().__init__(kwargs)

        sources = kwargs.get("sources", ["http.useragent"])
        target = kwargs.get("target", "http.useragent_details")

        self._check_pos_args(args)

        self.sources = sources
        self.target = target
        self.type = type

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, type, *args, **kwargs):  # noqa: E501
        """Helper creating a new instance from a response."""
        sources = kwargs.get("sources", ["http.useragent"])
        target = kwargs.get("target", "http.useragent_details")

        self = super(LogsUserAgentParser, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.sources = sources
        self.target = target
        self.type = type
        return self
