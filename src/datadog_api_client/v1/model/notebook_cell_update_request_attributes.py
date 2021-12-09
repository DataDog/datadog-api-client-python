# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
)


def lazy_import():
    from datadog_api_client.v1.model.log_stream_widget_definition import LogStreamWidgetDefinition
    from datadog_api_client.v1.model.notebook_cell_time import NotebookCellTime
    from datadog_api_client.v1.model.notebook_distribution_cell_attributes import NotebookDistributionCellAttributes
    from datadog_api_client.v1.model.notebook_graph_size import NotebookGraphSize
    from datadog_api_client.v1.model.notebook_heat_map_cell_attributes import NotebookHeatMapCellAttributes
    from datadog_api_client.v1.model.notebook_log_stream_cell_attributes import NotebookLogStreamCellAttributes
    from datadog_api_client.v1.model.notebook_markdown_cell_attributes import NotebookMarkdownCellAttributes
    from datadog_api_client.v1.model.notebook_split_by import NotebookSplitBy
    from datadog_api_client.v1.model.notebook_timeseries_cell_attributes import NotebookTimeseriesCellAttributes
    from datadog_api_client.v1.model.notebook_toplist_cell_attributes import NotebookToplistCellAttributes

    globals()["LogStreamWidgetDefinition"] = LogStreamWidgetDefinition
    globals()["NotebookCellTime"] = NotebookCellTime
    globals()["NotebookDistributionCellAttributes"] = NotebookDistributionCellAttributes
    globals()["NotebookGraphSize"] = NotebookGraphSize
    globals()["NotebookHeatMapCellAttributes"] = NotebookHeatMapCellAttributes
    globals()["NotebookLogStreamCellAttributes"] = NotebookLogStreamCellAttributes
    globals()["NotebookMarkdownCellAttributes"] = NotebookMarkdownCellAttributes
    globals()["NotebookSplitBy"] = NotebookSplitBy
    globals()["NotebookTimeseriesCellAttributes"] = NotebookTimeseriesCellAttributes
    globals()["NotebookToplistCellAttributes"] = NotebookToplistCellAttributes


class NotebookCellUpdateRequestAttributes(ModelComposed):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the name of the attribute. The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.

      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the name of the attribute. The value is a dict
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
        return {}

    discriminator = None

    attribute_map = {}

    read_only_vars = {}

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """NotebookCellUpdateRequestAttributes - a model defined in OpenAPI

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
            graph_size (NotebookGraphSize): [optional]  # noqa: E501
            split_by (NotebookSplitBy): [optional]  # noqa: E501
            time (NotebookCellTime): [optional]  # noqa: E501
            definition (LogStreamWidgetDefinition): [optional]  # noqa: E501
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Helper creating a new instance from a response."""

        self = super(NotebookCellUpdateRequestAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self

    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
            "anyOf": [],
            "allOf": [],
            "oneOf": [
                NotebookDistributionCellAttributes,
                NotebookHeatMapCellAttributes,
                NotebookLogStreamCellAttributes,
                NotebookMarkdownCellAttributes,
                NotebookTimeseriesCellAttributes,
                NotebookToplistCellAttributes,
            ],
        }
