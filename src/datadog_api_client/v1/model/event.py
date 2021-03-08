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
    from datadog_api_client.v1.model.event_alert_type import EventAlertType
    from datadog_api_client.v1.model.event_priority import EventPriority

    globals()["EventAlertType"] = EventAlertType
    globals()["EventPriority"] = EventPriority


class Event(ModelNormal):
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
        ("text",): {
            "max_length": 4000,
        },
        ("title",): {
            "max_length": 100,
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
            "alert_type": (EventAlertType,),  # noqa: E501
            "date_happened": (int,),  # noqa: E501
            "device_name": (str,),  # noqa: E501
            "host": (str,),  # noqa: E501
            "id": (int,),  # noqa: E501
            "payload": (str,),  # noqa: E501
            "priority": (EventPriority,),  # noqa: E501
            "source_type_name": (str,),  # noqa: E501
            "tags": ([str],),  # noqa: E501
            "text": (str,),  # noqa: E501
            "title": (str,),  # noqa: E501
            "url": (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None

    attribute_map = {
        "alert_type": "alert_type",  # noqa: E501
        "date_happened": "date_happened",  # noqa: E501
        "device_name": "device_name",  # noqa: E501
        "host": "host",  # noqa: E501
        "id": "id",  # noqa: E501
        "payload": "payload",  # noqa: E501
        "priority": "priority",  # noqa: E501
        "source_type_name": "source_type_name",  # noqa: E501
        "tags": "tags",  # noqa: E501
        "text": "text",  # noqa: E501
        "title": "title",  # noqa: E501
        "url": "url",  # noqa: E501
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
        """Event - a model defined in OpenAPI

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
            alert_type (EventAlertType): [optional]  # noqa: E501
            date_happened (int): POSIX timestamp of the event. Must be sent as an integer (i.e. no quotes). Limited to events no older than 7 days.. [optional]  # noqa: E501
            device_name (str): A device name.. [optional]  # noqa: E501
            host (str): Host name to associate with the event. Any tags associated with the host are also applied to this event.. [optional]  # noqa: E501
            id (int): Integer ID of the event.. [optional]  # noqa: E501
            payload (str): Payload of the event.. [optional]  # noqa: E501
            priority (EventPriority): [optional]  # noqa: E501
            source_type_name (str): The type of event being posted. Option examples include nagios, hudson, jenkins, my_apps, chef, puppet, git, bitbucket, etc. A complete list of source attribute values [available here](https://docs.datadoghq.com/integrations/faq/list-of-api-source-attribute-value).. [optional]  # noqa: E501
            tags ([str]): A list of tags to apply to the event.. [optional]  # noqa: E501
            text (str): The body of the event. Limited to 4000 characters. The text supports markdown. To use markdown in the event text, start the text block with `%%% \\n` and end the text block with `\\n %%%`. Use `msg_text` with the Datadog Ruby library.. [optional]  # noqa: E501
            title (str): The event title. Limited to 100 characters. Use `msg_title` with the Datadog Ruby library.. [optional]  # noqa: E501
            url (str): URL of the event.. [optional]  # noqa: E501
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
