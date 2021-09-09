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
    from datadog_api_client.v1.model.slo_history_metrics import SLOHistoryMetrics
    from datadog_api_client.v1.model.slo_history_monitor import SLOHistoryMonitor
    from datadog_api_client.v1.model.slo_history_sli_data import SLOHistorySLIData
    from datadog_api_client.v1.model.slo_threshold import SLOThreshold
    from datadog_api_client.v1.model.slo_type import SLOType
    from datadog_api_client.v1.model.slo_type_numeric import SLOTypeNumeric

    globals()["SLOHistoryMetrics"] = SLOHistoryMetrics
    globals()["SLOHistoryMonitor"] = SLOHistoryMonitor
    globals()["SLOHistorySLIData"] = SLOHistorySLIData
    globals()["SLOThreshold"] = SLOThreshold
    globals()["SLOType"] = SLOType
    globals()["SLOTypeNumeric"] = SLOTypeNumeric


class SLOHistoryResponseData(ModelNormal):
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
            "from_ts": (int,),  # noqa: E501
            "group_by": ([str],),  # noqa: E501
            "groups": ([SLOHistoryMonitor],),  # noqa: E501
            "monitors": ([SLOHistoryMonitor],),  # noqa: E501
            "overall": (SLOHistorySLIData,),  # noqa: E501
            "series": (SLOHistoryMetrics,),  # noqa: E501
            "thresholds": ({str: (SLOThreshold,)},),  # noqa: E501
            "to_ts": (int,),  # noqa: E501
            "type": (SLOType,),  # noqa: E501
            "type_id": (SLOTypeNumeric,),  # noqa: E501
        }

    discriminator = None

    attribute_map = {
        "from_ts": "from_ts",  # noqa: E501
        "group_by": "group_by",  # noqa: E501
        "groups": "groups",  # noqa: E501
        "monitors": "monitors",  # noqa: E501
        "overall": "overall",  # noqa: E501
        "series": "series",  # noqa: E501
        "thresholds": "thresholds",  # noqa: E501
        "to_ts": "to_ts",  # noqa: E501
        "type": "type",  # noqa: E501
        "type_id": "type_id",  # noqa: E501
    }

    read_only_vars = {}

    _composed_schemas = {}

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """SLOHistoryResponseData - a model defined in OpenAPI

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
            from_ts (int): The `from` timestamp in epoch seconds.. [optional]  # noqa: E501
            group_by ([str]): For `metric` based SLOs where the query includes a group-by clause, this represents the list of grouping parameters.  This is not included in responses for `monitor` based SLOs.. [optional]  # noqa: E501
            groups ([SLOHistoryMonitor]): For grouped SLOs, this represents SLI data for specific groups.  This is not included in the responses for `metric` based SLOs.. [optional]  # noqa: E501
            monitors ([SLOHistoryMonitor]): For multi-monitor SLOs, this represents SLI data for specific monitors.  This is not included in the responses for `metric` based SLOs.. [optional]  # noqa: E501
            overall (SLOHistorySLIData): [optional]  # noqa: E501
            series (SLOHistoryMetrics): [optional]  # noqa: E501
            thresholds ({str: (SLOThreshold,)}): mapping of string timeframe to the SLO threshold.. [optional]  # noqa: E501
            to_ts (int): The `to` timestamp in epoch seconds.. [optional]  # noqa: E501
            type (SLOType): [optional]  # noqa: E501
            type_id (SLOTypeNumeric): [optional]  # noqa: E501
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Helper creating a new instance from a response."""

        self = super(SLOHistoryResponseData, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
