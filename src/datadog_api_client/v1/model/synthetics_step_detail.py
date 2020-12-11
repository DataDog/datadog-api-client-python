# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import re  # noqa: F401
import sys  # noqa: F401

import nulltype  # noqa: F401

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
    from datadog_api_client.v1.model.synthetics_browser_error import SyntheticsBrowserError
    from datadog_api_client.v1.model.synthetics_check_type import SyntheticsCheckType
    from datadog_api_client.v1.model.synthetics_playing_tab import SyntheticsPlayingTab
    from datadog_api_client.v1.model.synthetics_resource import SyntheticsResource
    from datadog_api_client.v1.model.synthetics_step_detail_warnings import SyntheticsStepDetailWarnings
    from datadog_api_client.v1.model.synthetics_step_type import SyntheticsStepType
    globals()['SyntheticsBrowserError'] = SyntheticsBrowserError
    globals()['SyntheticsCheckType'] = SyntheticsCheckType
    globals()['SyntheticsPlayingTab'] = SyntheticsPlayingTab
    globals()['SyntheticsResource'] = SyntheticsResource
    globals()['SyntheticsStepDetailWarnings'] = SyntheticsStepDetailWarnings
    globals()['SyntheticsStepType'] = SyntheticsStepType


class SyntheticsStepDetail(ModelNormal):
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

    allowed_values = {
    }

    validations = {
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
            'browser_errors': ([SyntheticsBrowserError],),  # noqa: E501
            'check_type': (SyntheticsCheckType,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'duration': (float,),  # noqa: E501
            'error': (str,),  # noqa: E501
            'playing_tab': (SyntheticsPlayingTab,),  # noqa: E501
            'resources': ([SyntheticsResource],),  # noqa: E501
            'screenshot_bucket_key': (bool,),  # noqa: E501
            'skipped': (bool,),  # noqa: E501
            'snapshot_bucket_key': (bool,),  # noqa: E501
            'step_id': (int,),  # noqa: E501
            'sub_test_step_details': ([SyntheticsStepDetail],),  # noqa: E501
            'time_to_interactive': (float,),  # noqa: E501
            'type': (SyntheticsStepType,),  # noqa: E501
            'url': (str,),  # noqa: E501
            'value': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'warnings': ([SyntheticsStepDetailWarnings],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'browser_errors': 'browserErrors',  # noqa: E501
        'check_type': 'checkType',  # noqa: E501
        'description': 'description',  # noqa: E501
        'duration': 'duration',  # noqa: E501
        'error': 'error',  # noqa: E501
        'playing_tab': 'playingTab',  # noqa: E501
        'resources': 'resources',  # noqa: E501
        'screenshot_bucket_key': 'screenshotBucketKey',  # noqa: E501
        'skipped': 'skipped',  # noqa: E501
        'snapshot_bucket_key': 'snapshotBucketKey',  # noqa: E501
        'step_id': 'stepId',  # noqa: E501
        'sub_test_step_details': 'subTestStepDetails',  # noqa: E501
        'time_to_interactive': 'timeToInteractive',  # noqa: E501
        'type': 'type',  # noqa: E501
        'url': 'url',  # noqa: E501
        'value': 'value',  # noqa: E501
        'warnings': 'warnings',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """SyntheticsStepDetail - a model defined in OpenAPI

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
            browser_errors ([SyntheticsBrowserError]): Array of errors collected for a browser test.. [optional]  # noqa: E501
            check_type (SyntheticsCheckType): [optional]  # noqa: E501
            description (str): Description of the test.. [optional]  # noqa: E501
            duration (float): Total duration in millisecond of the test.. [optional]  # noqa: E501
            error (str): Error returned by the test.. [optional]  # noqa: E501
            playing_tab (SyntheticsPlayingTab): [optional]  # noqa: E501
            resources ([SyntheticsResource]): Array of resources collected by the test.. [optional]  # noqa: E501
            screenshot_bucket_key (bool): Whether or not screenshots where collected by the test.. [optional]  # noqa: E501
            skipped (bool): Whether or not to skip this step.. [optional]  # noqa: E501
            snapshot_bucket_key (bool): Whether or not snapshots where collected by the test.. [optional]  # noqa: E501
            step_id (int): The step ID.. [optional]  # noqa: E501
            sub_test_step_details ([SyntheticsStepDetail]): If this steps include a sub-test. [Subtests documentation](https://docs.datadoghq.com/synthetics/browser_tests/advanced_options/#subtests).. [optional]  # noqa: E501
            time_to_interactive (float): Time before starting the step.. [optional]  # noqa: E501
            type (SyntheticsStepType): [optional]  # noqa: E501
            url (str): URL to perform the step against.. [optional]  # noqa: E501
            value ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Value for the step.. [optional]  # noqa: E501
            warnings ([SyntheticsStepDetailWarnings]): Warning collected that didn't failed the step.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
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
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
