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
    from datadog_api_client.v1.model.synthetics_device_id import SyntheticsDeviceID
    from datadog_api_client.v1.model.synthetics_status import SyntheticsStatus
    from datadog_api_client.v1.model.synthetics_test_details_type import SyntheticsTestDetailsType
    from datadog_api_client.v1.model.synthetics_test_execution_rule import SyntheticsTestExecutionRule

    globals()["SyntheticsDeviceID"] = SyntheticsDeviceID
    globals()["SyntheticsStatus"] = SyntheticsStatus
    globals()["SyntheticsTestDetailsType"] = SyntheticsTestDetailsType
    globals()["SyntheticsTestExecutionRule"] = SyntheticsTestExecutionRule


class SyntheticsBatchResult(ModelNormal):
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
            "device": (SyntheticsDeviceID,),
            "duration": (float,),
            "execution_rule": (SyntheticsTestExecutionRule,),
            "location": (str,),
            "result_id": (str,),
            "retries": (float,),
            "status": (SyntheticsStatus,),
            "test_name": (str,),
            "test_public_id": (str,),
            "test_type": (SyntheticsTestDetailsType,),
        }

    attribute_map = {
        "device": "device",
        "duration": "duration",
        "execution_rule": "execution_rule",
        "location": "location",
        "result_id": "result_id",
        "retries": "retries",
        "status": "status",
        "test_name": "test_name",
        "test_public_id": "test_public_id",
        "test_type": "test_type",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """SyntheticsBatchResult - a model defined in OpenAPI

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
            device (SyntheticsDeviceID): [optional]
            duration (float): Total duration in millisecond of the test.. [optional]
            execution_rule (SyntheticsTestExecutionRule): [optional]
            location (str): Name of the location.. [optional]
            result_id (str): The ID of the result to get.. [optional]
            retries (float): Total duration in millisecond of the test.. [optional]
            status (SyntheticsStatus): [optional]
            test_name (str): Name of the test.. [optional]
            test_public_id (str): The public ID of the Synthetic test.. [optional]
            test_type (SyntheticsTestDetailsType): [optional]
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsBatchResult, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
