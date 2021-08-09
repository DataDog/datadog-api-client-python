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
    from datadog_api_client.v1.model.monitor_summary_widget_definition_type import MonitorSummaryWidgetDefinitionType
    from datadog_api_client.v1.model.widget_color_preference import WidgetColorPreference
    from datadog_api_client.v1.model.widget_monitor_summary_display_format import WidgetMonitorSummaryDisplayFormat
    from datadog_api_client.v1.model.widget_monitor_summary_sort import WidgetMonitorSummarySort
    from datadog_api_client.v1.model.widget_summary_type import WidgetSummaryType
    from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign

    globals()["MonitorSummaryWidgetDefinitionType"] = MonitorSummaryWidgetDefinitionType
    globals()["WidgetColorPreference"] = WidgetColorPreference
    globals()["WidgetMonitorSummaryDisplayFormat"] = WidgetMonitorSummaryDisplayFormat
    globals()["WidgetMonitorSummarySort"] = WidgetMonitorSummarySort
    globals()["WidgetSummaryType"] = WidgetSummaryType
    globals()["WidgetTextAlign"] = WidgetTextAlign


class MonitorSummaryWidgetDefinition(ModelNormal):
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
            "query": (str,),  # noqa: E501
            "type": (MonitorSummaryWidgetDefinitionType,),  # noqa: E501
            "color_preference": (WidgetColorPreference,),  # noqa: E501
            "count": (int,),  # noqa: E501
            "display_format": (WidgetMonitorSummaryDisplayFormat,),  # noqa: E501
            "hide_zero_counts": (bool,),  # noqa: E501
            "show_last_triggered": (bool,),  # noqa: E501
            "sort": (WidgetMonitorSummarySort,),  # noqa: E501
            "start": (int,),  # noqa: E501
            "summary_type": (WidgetSummaryType,),  # noqa: E501
            "title": (str,),  # noqa: E501
            "title_align": (WidgetTextAlign,),  # noqa: E501
            "title_size": (str,),  # noqa: E501
        }

    discriminator = None

    attribute_map = {
        "query": "query",  # noqa: E501
        "type": "type",  # noqa: E501
        "color_preference": "color_preference",  # noqa: E501
        "count": "count",  # noqa: E501
        "display_format": "display_format",  # noqa: E501
        "hide_zero_counts": "hide_zero_counts",  # noqa: E501
        "show_last_triggered": "show_last_triggered",  # noqa: E501
        "sort": "sort",  # noqa: E501
        "start": "start",  # noqa: E501
        "summary_type": "summary_type",  # noqa: E501
        "title": "title",  # noqa: E501
        "title_align": "title_align",  # noqa: E501
        "title_size": "title_size",  # noqa: E501
    }

    read_only_vars = {}

    _composed_schemas = {}

    @convert_js_args_to_python_args
    def __init__(self, query, type, *args, **kwargs):  # noqa: E501
        """MonitorSummaryWidgetDefinition - a model defined in OpenAPI

        Args:
            query (str): Query to filter the monitors with.
            type (MonitorSummaryWidgetDefinitionType):

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
            color_preference (WidgetColorPreference): [optional]  # noqa: E501
            count (int): The number of monitors to display.. [optional]  # noqa: E501
            display_format (WidgetMonitorSummaryDisplayFormat): [optional]  # noqa: E501
            hide_zero_counts (bool): Whether to show counts of 0 or not.. [optional]  # noqa: E501
            show_last_triggered (bool): Whether to show the time that has elapsed since the monitor/group triggered.. [optional]  # noqa: E501
            sort (WidgetMonitorSummarySort): [optional]  # noqa: E501
            start (int): The start of the list. Typically 0.. [optional]  # noqa: E501
            summary_type (WidgetSummaryType): [optional]  # noqa: E501
            title (str): Title of the widget.. [optional]  # noqa: E501
            title_align (WidgetTextAlign): [optional]  # noqa: E501
            title_size (str): Size of the title.. [optional]  # noqa: E501
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.query = query
        self.type = type

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, query, type, *args, **kwargs):  # noqa: E501
        """Helper creating a new instance from a response."""

        self = super(MonitorSummaryWidgetDefinition, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.query = query
        self.type = type
        return self
