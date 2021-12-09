# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
)


def lazy_import():
    from datadog_api_client.v1.model.logs_attribute_remapper_type import LogsAttributeRemapperType
    from datadog_api_client.v1.model.target_format_type import TargetFormatType

    globals()["LogsAttributeRemapperType"] = LogsAttributeRemapperType
    globals()["TargetFormatType"] = TargetFormatType


class LogsAttributeRemapper(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the name of the attribute. The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.

      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the name of the attribute. The value is a dict
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
            "type": (LogsAttributeRemapperType,),  # noqa: E501
            "is_enabled": (bool,),  # noqa: E501
            "name": (str,),  # noqa: E501
            "override_on_conflict": (bool,),  # noqa: E501
            "preserve_source": (bool,),  # noqa: E501
            "source_type": (str,),  # noqa: E501
            "target_format": (TargetFormatType,),  # noqa: E501
            "target_type": (str,),  # noqa: E501
        }

    discriminator = None

    attribute_map = {
        "sources": "sources",  # noqa: E501
        "target": "target",  # noqa: E501
        "type": "type",  # noqa: E501
        "is_enabled": "is_enabled",  # noqa: E501
        "name": "name",  # noqa: E501
        "override_on_conflict": "override_on_conflict",  # noqa: E501
        "preserve_source": "preserve_source",  # noqa: E501
        "source_type": "source_type",  # noqa: E501
        "target_format": "target_format",  # noqa: E501
        "target_type": "target_type",  # noqa: E501
    }

    read_only_vars = {}

    _composed_schemas = {}

    @convert_js_args_to_python_args
    def __init__(self, sources, target, type, *args, **kwargs):  # noqa: E501
        """LogsAttributeRemapper - a model defined in OpenAPI

        Args:
            sources ([str]): Array of source attributes.
            target (str): Final attribute or tag name to remap the sources to.
            type (LogsAttributeRemapperType):

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
            override_on_conflict (bool): Override or not the target element if already set,. [optional] if omitted the server will use the default value of False  # noqa: E501
            preserve_source (bool): Remove or preserve the remapped source element.. [optional] if omitted the server will use the default value of False  # noqa: E501
            source_type (str): Defines if the sources are from log `attribute` or `tag`.. [optional] if omitted the server will use the default value of "attribute"  # noqa: E501
            target_format (TargetFormatType): [optional]  # noqa: E501
            target_type (str): Defines if the final attribute or tag name is from log `attribute` or `tag`.. [optional] if omitted the server will use the default value of "attribute"  # noqa: E501
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.sources = sources
        self.target = target
        self.type = type

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, sources, target, type, *args, **kwargs):  # noqa: E501
        """Helper creating a new instance from a response."""

        self = super(LogsAttributeRemapper, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.sources = sources
        self.target = target
        self.type = type
        return self
