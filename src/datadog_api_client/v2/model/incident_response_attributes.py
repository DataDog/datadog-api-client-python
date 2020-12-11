# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import re  # noqa: F401
import sys  # noqa: F401

import nulltype  # noqa: F401

from datadog_api_client.v2.model_utils import (  # noqa: F401
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
    from datadog_api_client.v2.model.incident_field_attributes import IncidentFieldAttributes
    globals()['IncidentFieldAttributes'] = IncidentFieldAttributes


class IncidentResponseAttributes(ModelNormal):
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
            'title': (str,),  # noqa: E501
            'created': (datetime,),  # noqa: E501
            'customer_impact_duration': (int,),  # noqa: E501
            'customer_impact_end': (datetime, none_type,),  # noqa: E501
            'customer_impact_scope': (str, none_type,),  # noqa: E501
            'customer_impact_start': (datetime, none_type,),  # noqa: E501
            'customer_impacted': (bool,),  # noqa: E501
            'detected': (datetime, none_type,),  # noqa: E501
            'fields': ({str: (IncidentFieldAttributes,)},),  # noqa: E501
            'modified': (datetime,),  # noqa: E501
            'notification_handles': ([str],),  # noqa: E501
            'postmortem_id': (str,),  # noqa: E501
            'public_id': (int,),  # noqa: E501
            'resolved': (datetime, none_type,),  # noqa: E501
            'time_to_detect': (int,),  # noqa: E501
            'time_to_internal_response': (int,),  # noqa: E501
            'time_to_repair': (int,),  # noqa: E501
            'time_to_resolve': (int,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'title': 'title',  # noqa: E501
        'created': 'created',  # noqa: E501
        'customer_impact_duration': 'customer_impact_duration',  # noqa: E501
        'customer_impact_end': 'customer_impact_end',  # noqa: E501
        'customer_impact_scope': 'customer_impact_scope',  # noqa: E501
        'customer_impact_start': 'customer_impact_start',  # noqa: E501
        'customer_impacted': 'customer_impacted',  # noqa: E501
        'detected': 'detected',  # noqa: E501
        'fields': 'fields',  # noqa: E501
        'modified': 'modified',  # noqa: E501
        'notification_handles': 'notification_handles',  # noqa: E501
        'postmortem_id': 'postmortem_id',  # noqa: E501
        'public_id': 'public_id',  # noqa: E501
        'resolved': 'resolved',  # noqa: E501
        'time_to_detect': 'time_to_detect',  # noqa: E501
        'time_to_internal_response': 'time_to_internal_response',  # noqa: E501
        'time_to_repair': 'time_to_repair',  # noqa: E501
        'time_to_resolve': 'time_to_resolve',  # noqa: E501
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
    def __init__(self, title, *args, **kwargs):  # noqa: E501
        """IncidentResponseAttributes - a model defined in OpenAPI

        Args:
            title (str): The title of the incident, which summarizes what happened.

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
            created (datetime): Timestamp when the incident was created.. [optional]  # noqa: E501
            customer_impact_duration (int): Length of the incident's customer impact in seconds. Equals the difference between `customer_impact_start` and `customer_impact_end`.. [optional]  # noqa: E501
            customer_impact_end (datetime, none_type): Timestamp when customers were no longer impacted by the incident.. [optional]  # noqa: E501
            customer_impact_scope (str, none_type): A summary of the impact customers experienced during the incident.. [optional]  # noqa: E501
            customer_impact_start (datetime, none_type): Timestamp when customers began being impacted by the incident.. [optional]  # noqa: E501
            customer_impacted (bool): A flag indicating whether the incident caused customer impact.. [optional]  # noqa: E501
            detected (datetime, none_type): Timestamp when the incident was detected.. [optional]  # noqa: E501
            fields ({str: (IncidentFieldAttributes,)}): A condensed view of the user-defined fields attached to incidents.. [optional]  # noqa: E501
            modified (datetime): Timestamp when the incident was last modified.. [optional]  # noqa: E501
            notification_handles ([str]): Notification handles that will be notified of the incident during update.. [optional]  # noqa: E501
            postmortem_id (str): The UUID of the postmortem object attached to the incident.. [optional]  # noqa: E501
            public_id (int): The monotonically increasing integer ID for the incident.. [optional]  # noqa: E501
            resolved (datetime, none_type): Timestamp when the incident's state was set to resolved.. [optional]  # noqa: E501
            time_to_detect (int): The amount of time in seconds to detect the incident. Equals the difference between `customer_impact_start` and `detected`.. [optional]  # noqa: E501
            time_to_internal_response (int): The amount of time in seconds to call incident after detection. Equals the difference of `detected` and `created`.. [optional]  # noqa: E501
            time_to_repair (int): The amount of time in seconds to resolve customer impact after detecting the issue. Equals the difference between `customer_impact_end` and `detected`.. [optional]  # noqa: E501
            time_to_resolve (int): The amount of time in seconds to resolve the incident after it was created. Equals the difference between `created` and `resolved`.. [optional]  # noqa: E501
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

        self.title = title
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
