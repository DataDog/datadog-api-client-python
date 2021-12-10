# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    date,
    datetime,
    file_type,
    none_type,
)


def lazy_import():
    from datadog_api_client.v1.model.logs_arithmetic_processor_type import LogsArithmeticProcessorType

    globals()["LogsArithmeticProcessorType"] = LogsArithmeticProcessorType


class LogsArithmeticProcessor(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the name of the attribute. The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.

      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      validations (dict): The key is the name of the attribute. The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.

    """

    validations = {}

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
            "expression": (str,),
            "is_enabled": (bool,),
            "is_replace_missing": (bool,),
            "name": (str,),
            "target": (str,),
            "type": (LogsArithmeticProcessorType,),
        }

    attribute_map = {
        "expression": "expression",
        "target": "target",
        "type": "type",
        "is_enabled": "is_enabled",
        "is_replace_missing": "is_replace_missing",
        "name": "name",
    }

    read_only_vars = {}

    def __init__(self, expression, target, type, *args, **kwargs):
        """LogsArithmeticProcessor - a model defined in OpenAPI

        Args:
            expression (str): Arithmetic operation between one or more log attributes.
            target (str): Name of the attribute that contains the result of the arithmetic operation.
            type (LogsArithmeticProcessorType):

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
            is_enabled (bool): Whether or not the processor is enabled.. [optional] if omitted the server will use the default value of False
            is_replace_missing (bool): If `true`, it replaces all missing attributes of expression by `0`, `false` skip the operation if an attribute is missing.. [optional] if omitted the server will use the default value of False
            name (str): Name of the processor.. [optional]
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.expression = expression
        self.target = target
        self.type = type

    @classmethod
    def _from_openapi_data(cls, expression, target, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsArithmeticProcessor, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.expression = expression
        self.target = target
        self.type = type
        return self
