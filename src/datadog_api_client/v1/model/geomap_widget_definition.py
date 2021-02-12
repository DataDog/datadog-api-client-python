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
    from datadog_api_client.v1.model.geomap_widget_definition_style import GeomapWidgetDefinitionStyle
    from datadog_api_client.v1.model.geomap_widget_definition_type import GeomapWidgetDefinitionType
    from datadog_api_client.v1.model.geomap_widget_definition_view import GeomapWidgetDefinitionView
    from datadog_api_client.v1.model.geomap_widget_request import GeomapWidgetRequest
    from datadog_api_client.v1.model.widget_custom_link import WidgetCustomLink
    from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
    from datadog_api_client.v1.model.widget_time import WidgetTime

    globals()["GeomapWidgetDefinitionStyle"] = GeomapWidgetDefinitionStyle
    globals()["GeomapWidgetDefinitionType"] = GeomapWidgetDefinitionType
    globals()["GeomapWidgetDefinitionView"] = GeomapWidgetDefinitionView
    globals()["GeomapWidgetRequest"] = GeomapWidgetRequest
    globals()["WidgetCustomLink"] = WidgetCustomLink
    globals()["WidgetTextAlign"] = WidgetTextAlign
    globals()["WidgetTime"] = WidgetTime


class GeomapWidgetDefinition(ModelNormal):
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
            "requests": ([GeomapWidgetRequest],),  # noqa: E501
            "style": (GeomapWidgetDefinitionStyle,),  # noqa: E501
            "type": (GeomapWidgetDefinitionType,),  # noqa: E501
            "view": (GeomapWidgetDefinitionView,),  # noqa: E501
            "custom_links": ([WidgetCustomLink],),  # noqa: E501
            "time": (WidgetTime,),  # noqa: E501
            "title": (str,),  # noqa: E501
            "title_align": (WidgetTextAlign,),  # noqa: E501
            "title_size": (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None

    attribute_map = {
        "requests": "requests",  # noqa: E501
        "style": "style",  # noqa: E501
        "type": "type",  # noqa: E501
        "view": "view",  # noqa: E501
        "custom_links": "custom_links",  # noqa: E501
        "time": "time",  # noqa: E501
        "title": "title",  # noqa: E501
        "title_align": "title_align",  # noqa: E501
        "title_size": "title_size",  # noqa: E501
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
    def __init__(self, requests, style, type, view, *args, **kwargs):  # noqa: E501
        """GeomapWidgetDefinition - a model defined in OpenAPI

        Args:
            requests ([GeomapWidgetRequest]): Array of one request object to display in the widget. The request must contain a `group-by` tag whose value is a country ISO code.  See the [Request JSON schema documentation](https://docs.datadoghq.com/dashboards/graphing_json/request_json) for information about building the `REQUEST_SCHEMA`.
            style (GeomapWidgetDefinitionStyle):
            type (GeomapWidgetDefinitionType):
            view (GeomapWidgetDefinitionView):

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
            custom_links ([WidgetCustomLink]): A list of custom links.. [optional]  # noqa: E501
            time (WidgetTime): [optional]  # noqa: E501
            title (str): The title of your widget.. [optional]  # noqa: E501
            title_align (WidgetTextAlign): [optional]  # noqa: E501
            title_size (str): The size of the title.. [optional]  # noqa: E501
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

        self.requests = requests
        self.style = style
        self.type = type
        self.view = view
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
