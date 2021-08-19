# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


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
)


def lazy_import():
    from datadog_api_client.v2.model.incident_field_attributes import IncidentFieldAttributes
    from datadog_api_client.v2.model.incident_notification_handle import IncidentNotificationHandle
    from datadog_api_client.v2.model.incident_timeline_cell_create_attributes import (
        IncidentTimelineCellCreateAttributes,
    )

    globals()["IncidentFieldAttributes"] = IncidentFieldAttributes
    globals()["IncidentNotificationHandle"] = IncidentNotificationHandle
    globals()["IncidentTimelineCellCreateAttributes"] = IncidentTimelineCellCreateAttributes


class IncidentCreateAttributes(ModelNormal):
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
            "customer_impacted": (bool,),  # noqa: E501
            "title": (str,),  # noqa: E501
            "fields": ({str: (IncidentFieldAttributes,)},),  # noqa: E501
            "initial_cells": ([IncidentTimelineCellCreateAttributes],),  # noqa: E501
            "notification_handles": ([IncidentNotificationHandle],),  # noqa: E501
        }

    discriminator = None

    attribute_map = {
        "customer_impacted": "customer_impacted",  # noqa: E501
        "title": "title",  # noqa: E501
        "fields": "fields",  # noqa: E501
        "initial_cells": "initial_cells",  # noqa: E501
        "notification_handles": "notification_handles",  # noqa: E501
    }

    read_only_vars = {}

    _composed_schemas = {}

    @convert_js_args_to_python_args
    def __init__(self, customer_impacted, title, *args, **kwargs):  # noqa: E501
        """IncidentCreateAttributes - a model defined in OpenAPI

        Args:
            customer_impacted (bool): A flag indicating whether the incident caused customer impact.
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
            fields ({str: (IncidentFieldAttributes,)}): A condensed view of the user-defined fields for which to create initial selections.. [optional]  # noqa: E501
            initial_cells ([IncidentTimelineCellCreateAttributes]): An array of initial timeline cells to be placed at the beginning of the incident timeline.. [optional]  # noqa: E501
            notification_handles ([IncidentNotificationHandle]): Notification handles that will be notified of the incident at creation.. [optional]  # noqa: E501
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.customer_impacted = customer_impacted
        self.title = title

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, customer_impacted, title, *args, **kwargs):  # noqa: E501
        """Helper creating a new instance from a response."""

        self = super(IncidentCreateAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.customer_impacted = customer_impacted
        self.title = title
        return self
