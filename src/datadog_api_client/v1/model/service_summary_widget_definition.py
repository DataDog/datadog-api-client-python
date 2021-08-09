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
    from datadog_api_client.v1.model.service_summary_widget_definition_type import ServiceSummaryWidgetDefinitionType
    from datadog_api_client.v1.model.widget_service_summary_display_format import WidgetServiceSummaryDisplayFormat
    from datadog_api_client.v1.model.widget_size_format import WidgetSizeFormat
    from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
    from datadog_api_client.v1.model.widget_time import WidgetTime

    globals()["ServiceSummaryWidgetDefinitionType"] = ServiceSummaryWidgetDefinitionType
    globals()["WidgetServiceSummaryDisplayFormat"] = WidgetServiceSummaryDisplayFormat
    globals()["WidgetSizeFormat"] = WidgetSizeFormat
    globals()["WidgetTextAlign"] = WidgetTextAlign
    globals()["WidgetTime"] = WidgetTime


class ServiceSummaryWidgetDefinition(ModelNormal):
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
            "env": (str,),  # noqa: E501
            "service": (str,),  # noqa: E501
            "span_name": (str,),  # noqa: E501
            "type": (ServiceSummaryWidgetDefinitionType,),  # noqa: E501
            "display_format": (WidgetServiceSummaryDisplayFormat,),  # noqa: E501
            "show_breakdown": (bool,),  # noqa: E501
            "show_distribution": (bool,),  # noqa: E501
            "show_errors": (bool,),  # noqa: E501
            "show_hits": (bool,),  # noqa: E501
            "show_latency": (bool,),  # noqa: E501
            "show_resource_list": (bool,),  # noqa: E501
            "size_format": (WidgetSizeFormat,),  # noqa: E501
            "time": (WidgetTime,),  # noqa: E501
            "title": (str,),  # noqa: E501
            "title_align": (WidgetTextAlign,),  # noqa: E501
            "title_size": (str,),  # noqa: E501
        }

    discriminator = None

    attribute_map = {
        "env": "env",  # noqa: E501
        "service": "service",  # noqa: E501
        "span_name": "span_name",  # noqa: E501
        "type": "type",  # noqa: E501
        "display_format": "display_format",  # noqa: E501
        "show_breakdown": "show_breakdown",  # noqa: E501
        "show_distribution": "show_distribution",  # noqa: E501
        "show_errors": "show_errors",  # noqa: E501
        "show_hits": "show_hits",  # noqa: E501
        "show_latency": "show_latency",  # noqa: E501
        "show_resource_list": "show_resource_list",  # noqa: E501
        "size_format": "size_format",  # noqa: E501
        "time": "time",  # noqa: E501
        "title": "title",  # noqa: E501
        "title_align": "title_align",  # noqa: E501
        "title_size": "title_size",  # noqa: E501
    }

    read_only_vars = {}

    _composed_schemas = {}

    @convert_js_args_to_python_args
    def __init__(self, env, service, span_name, type, *args, **kwargs):  # noqa: E501
        """ServiceSummaryWidgetDefinition - a model defined in OpenAPI

        Args:
            env (str): APM environment.
            service (str): APM service.
            span_name (str): APM span name.
            type (ServiceSummaryWidgetDefinitionType):

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
            display_format (WidgetServiceSummaryDisplayFormat): [optional]  # noqa: E501
            show_breakdown (bool): Whether to show the latency breakdown or not.. [optional]  # noqa: E501
            show_distribution (bool): Whether to show the latency distribution or not.. [optional]  # noqa: E501
            show_errors (bool): Whether to show the error metrics or not.. [optional]  # noqa: E501
            show_hits (bool): Whether to show the hits metrics or not.. [optional]  # noqa: E501
            show_latency (bool): Whether to show the latency metrics or not.. [optional]  # noqa: E501
            show_resource_list (bool): Whether to show the resource list or not.. [optional]  # noqa: E501
            size_format (WidgetSizeFormat): [optional]  # noqa: E501
            time (WidgetTime): [optional]  # noqa: E501
            title (str): Title of the widget.. [optional]  # noqa: E501
            title_align (WidgetTextAlign): [optional]  # noqa: E501
            title_size (str): Size of the title.. [optional]  # noqa: E501
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.env = env
        self.service = service
        self.span_name = span_name
        self.type = type

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, env, service, span_name, type, *args, **kwargs):  # noqa: E501
        """Helper creating a new instance from a response."""

        self = super(ServiceSummaryWidgetDefinition, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.env = env
        self.service = service
        self.span_name = span_name
        self.type = type
        return self
