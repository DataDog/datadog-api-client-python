# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import re  # noqa: F401
import sys  # noqa: F401

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
    validate_get_composed_info,
)


def lazy_import():
    from datadog_api_client.v1.model.synthetics_device_id import SyntheticsDeviceID
    from datadog_api_client.v1.model.synthetics_test_options_monitor_options import SyntheticsTestOptionsMonitorOptions
    from datadog_api_client.v1.model.synthetics_test_options_retry import SyntheticsTestOptionsRetry
    from datadog_api_client.v1.model.synthetics_tick_interval import SyntheticsTickInterval

    globals()["SyntheticsDeviceID"] = SyntheticsDeviceID
    globals()["SyntheticsTestOptionsMonitorOptions"] = SyntheticsTestOptionsMonitorOptions
    globals()["SyntheticsTestOptionsRetry"] = SyntheticsTestOptionsRetry
    globals()["SyntheticsTickInterval"] = SyntheticsTickInterval


class SyntheticsTestOptions(ModelNormal):
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
        ("monitor_priority",): {
            "inclusive_maximum": 5,
            "inclusive_minimum": 1,
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
        lazy_import()
        return {
            "accept_self_signed": (bool,),  # noqa: E501
            "allow_insecure": (bool,),  # noqa: E501
            "device_ids": ([SyntheticsDeviceID],),  # noqa: E501
            "disable_cors": (bool,),  # noqa: E501
            "follow_redirects": (bool,),  # noqa: E501
            "min_failure_duration": (int,),  # noqa: E501
            "min_location_failed": (int,),  # noqa: E501
            "monitor_name": (str,),  # noqa: E501
            "monitor_options": (SyntheticsTestOptionsMonitorOptions,),  # noqa: E501
            "monitor_priority": (int,),  # noqa: E501
            "no_screenshot": (bool,),  # noqa: E501
            "retry": (SyntheticsTestOptionsRetry,),  # noqa: E501
            "tick_every": (SyntheticsTickInterval,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None

    attribute_map = {
        "accept_self_signed": "accept_self_signed",  # noqa: E501
        "allow_insecure": "allow_insecure",  # noqa: E501
        "device_ids": "device_ids",  # noqa: E501
        "disable_cors": "disableCors",  # noqa: E501
        "follow_redirects": "follow_redirects",  # noqa: E501
        "min_failure_duration": "min_failure_duration",  # noqa: E501
        "min_location_failed": "min_location_failed",  # noqa: E501
        "monitor_name": "monitor_name",  # noqa: E501
        "monitor_options": "monitor_options",  # noqa: E501
        "monitor_priority": "monitor_priority",  # noqa: E501
        "no_screenshot": "noScreenshot",  # noqa: E501
        "retry": "retry",  # noqa: E501
        "tick_every": "tick_every",  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set(
        [
            "_data_store",
            "_check_type",
            "_spec_property_naming",
            "_path_to_item",
            "_configuration",
            "_visited_composed_classes",
        ]
    )

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """SyntheticsTestOptions - a model defined in OpenAPI

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
            accept_self_signed (bool): For SSL test, whether or not the test should allow self signed certificates.. [optional]  # noqa: E501
            allow_insecure (bool): Allows loading insecure content for an HTTP request.. [optional]  # noqa: E501
            device_ids ([SyntheticsDeviceID]): For browser test, array with the different device IDs used to run the test.. [optional]  # noqa: E501
            disable_cors (bool): Whether or not to disable CORS mechanism.. [optional]  # noqa: E501
            follow_redirects (bool): For API HTTP test, whether or not the test should follow redirects.. [optional]  # noqa: E501
            min_failure_duration (int): Minimum amount of time in failure required to trigger an alert.. [optional]  # noqa: E501
            min_location_failed (int): Minimum number of locations in failure required to trigger an alert.. [optional]  # noqa: E501
            monitor_name (str): The monitor name is used for the alert title as well as for all monitor dashboard widgets and SLOs.. [optional]  # noqa: E501
            monitor_options (SyntheticsTestOptionsMonitorOptions): [optional]  # noqa: E501
            monitor_priority (int): Integer from 1 (high) to 5 (low) indicating alert severity.. [optional]  # noqa: E501
            no_screenshot (bool): Prevents saving screenshots of the steps.. [optional]  # noqa: E501
            retry (SyntheticsTestOptionsRetry): [optional]  # noqa: E501
            tick_every (SyntheticsTickInterval): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop("_check_type", True)
        _spec_property_naming = kwargs.pop("_spec_property_naming", False)
        _path_to_item = kwargs.pop("_path_to_item", ())
        _configuration = kwargs.pop("_configuration", None)
        _visited_composed_classes = kwargs.pop("_visited_composed_classes", ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments."
                % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if (
                var_name not in self.attribute_map
                and self._configuration is not None
                and self._configuration.discard_unknown_keys
                and self.additional_properties_type is None
            ):
                # discard variable.
                continue
            setattr(self, var_name, var_value)
