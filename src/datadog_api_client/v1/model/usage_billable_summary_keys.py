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
    from datadog_api_client.v1.model.usage_billable_summary_body import UsageBillableSummaryBody

    globals()["UsageBillableSummaryBody"] = UsageBillableSummaryBody


class UsageBillableSummaryKeys(ModelNormal):
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
            "apm_host_sum": (UsageBillableSummaryBody,),  # noqa: E501
            "apm_host_top99p": (UsageBillableSummaryBody,),  # noqa: E501
            "apm_trace_search_sum": (UsageBillableSummaryBody,),  # noqa: E501
            "fargate_container_average": (UsageBillableSummaryBody,),  # noqa: E501
            "infra_container_sum": (UsageBillableSummaryBody,),  # noqa: E501
            "infra_host_sum": (UsageBillableSummaryBody,),  # noqa: E501
            "infra_host_top99p": (UsageBillableSummaryBody,),  # noqa: E501
            "iot_top99p": (UsageBillableSummaryBody,),  # noqa: E501
            "lambda_function_average": (UsageBillableSummaryBody,),  # noqa: E501
            "logs_indexed_15day_sum": (UsageBillableSummaryBody,),  # noqa: E501
            "logs_indexed_180day_sum": (UsageBillableSummaryBody,),  # noqa: E501
            "logs_indexed_30day_sum": (UsageBillableSummaryBody,),  # noqa: E501
            "logs_indexed_3day_sum": (UsageBillableSummaryBody,),  # noqa: E501
            "logs_indexed_45day_sum": (UsageBillableSummaryBody,),  # noqa: E501
            "logs_indexed_60day_sum": (UsageBillableSummaryBody,),  # noqa: E501
            "logs_indexed_7day_sum": (UsageBillableSummaryBody,),  # noqa: E501
            "logs_indexed_90day_sum": (UsageBillableSummaryBody,),  # noqa: E501
            "logs_indexed_custom_retention_sum": (UsageBillableSummaryBody,),  # noqa: E501
            "logs_indexed_sum": (UsageBillableSummaryBody,),  # noqa: E501
            "logs_ingested_sum": (UsageBillableSummaryBody,),  # noqa: E501
            "network_device_top99p": (UsageBillableSummaryBody,),  # noqa: E501
            "npm_flow_sum": (UsageBillableSummaryBody,),  # noqa: E501
            "npm_host_sum": (UsageBillableSummaryBody,),  # noqa: E501
            "npm_host_top99p": (UsageBillableSummaryBody,),  # noqa: E501
            "prof_container_sum": (UsageBillableSummaryBody,),  # noqa: E501
            "prof_host_top99p": (UsageBillableSummaryBody,),  # noqa: E501
            "rum_sum": (UsageBillableSummaryBody,),  # noqa: E501
            "serverless_invocation_sum": (UsageBillableSummaryBody,),  # noqa: E501
            "siem_sum": (UsageBillableSummaryBody,),  # noqa: E501
            "synthetics_api_tests_sum": (UsageBillableSummaryBody,),  # noqa: E501
            "synthetics_browser_checks_sum": (UsageBillableSummaryBody,),  # noqa: E501
            "timeseries_average": (UsageBillableSummaryBody,),  # noqa: E501
        }

    discriminator = None

    attribute_map = {
        "apm_host_sum": "apm_host_sum",  # noqa: E501
        "apm_host_top99p": "apm_host_top99p",  # noqa: E501
        "apm_trace_search_sum": "apm_trace_search_sum",  # noqa: E501
        "fargate_container_average": "fargate_container_average",  # noqa: E501
        "infra_container_sum": "infra_container_sum",  # noqa: E501
        "infra_host_sum": "infra_host_sum",  # noqa: E501
        "infra_host_top99p": "infra_host_top99p",  # noqa: E501
        "iot_top99p": "iot_top99p",  # noqa: E501
        "lambda_function_average": "lambda_function_average",  # noqa: E501
        "logs_indexed_15day_sum": "logs_indexed_15day_sum",  # noqa: E501
        "logs_indexed_180day_sum": "logs_indexed_180day_sum",  # noqa: E501
        "logs_indexed_30day_sum": "logs_indexed_30day_sum",  # noqa: E501
        "logs_indexed_3day_sum": "logs_indexed_3day_sum",  # noqa: E501
        "logs_indexed_45day_sum": "logs_indexed_45day_sum",  # noqa: E501
        "logs_indexed_60day_sum": "logs_indexed_60day_sum",  # noqa: E501
        "logs_indexed_7day_sum": "logs_indexed_7day_sum",  # noqa: E501
        "logs_indexed_90day_sum": "logs_indexed_90day_sum",  # noqa: E501
        "logs_indexed_custom_retention_sum": "logs_indexed_custom_retention_sum",  # noqa: E501
        "logs_indexed_sum": "logs_indexed_sum",  # noqa: E501
        "logs_ingested_sum": "logs_ingested_sum",  # noqa: E501
        "network_device_top99p": "network_device_top99p",  # noqa: E501
        "npm_flow_sum": "npm_flow_sum",  # noqa: E501
        "npm_host_sum": "npm_host_sum",  # noqa: E501
        "npm_host_top99p": "npm_host_top99p",  # noqa: E501
        "prof_container_sum": "prof_container_sum",  # noqa: E501
        "prof_host_top99p": "prof_host_top99p",  # noqa: E501
        "rum_sum": "rum_sum",  # noqa: E501
        "serverless_invocation_sum": "serverless_invocation_sum",  # noqa: E501
        "siem_sum": "siem_sum",  # noqa: E501
        "synthetics_api_tests_sum": "synthetics_api_tests_sum",  # noqa: E501
        "synthetics_browser_checks_sum": "synthetics_browser_checks_sum",  # noqa: E501
        "timeseries_average": "timeseries_average",  # noqa: E501
    }

    read_only_vars = {}

    _composed_schemas = {}

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """UsageBillableSummaryKeys - a model defined in OpenAPI

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
            apm_host_sum (UsageBillableSummaryBody): [optional]  # noqa: E501
            apm_host_top99p (UsageBillableSummaryBody): [optional]  # noqa: E501
            apm_trace_search_sum (UsageBillableSummaryBody): [optional]  # noqa: E501
            fargate_container_average (UsageBillableSummaryBody): [optional]  # noqa: E501
            infra_container_sum (UsageBillableSummaryBody): [optional]  # noqa: E501
            infra_host_sum (UsageBillableSummaryBody): [optional]  # noqa: E501
            infra_host_top99p (UsageBillableSummaryBody): [optional]  # noqa: E501
            iot_top99p (UsageBillableSummaryBody): [optional]  # noqa: E501
            lambda_function_average (UsageBillableSummaryBody): [optional]  # noqa: E501
            logs_indexed_15day_sum (UsageBillableSummaryBody): [optional]  # noqa: E501
            logs_indexed_180day_sum (UsageBillableSummaryBody): [optional]  # noqa: E501
            logs_indexed_30day_sum (UsageBillableSummaryBody): [optional]  # noqa: E501
            logs_indexed_3day_sum (UsageBillableSummaryBody): [optional]  # noqa: E501
            logs_indexed_45day_sum (UsageBillableSummaryBody): [optional]  # noqa: E501
            logs_indexed_60day_sum (UsageBillableSummaryBody): [optional]  # noqa: E501
            logs_indexed_7day_sum (UsageBillableSummaryBody): [optional]  # noqa: E501
            logs_indexed_90day_sum (UsageBillableSummaryBody): [optional]  # noqa: E501
            logs_indexed_custom_retention_sum (UsageBillableSummaryBody): [optional]  # noqa: E501
            logs_indexed_sum (UsageBillableSummaryBody): [optional]  # noqa: E501
            logs_ingested_sum (UsageBillableSummaryBody): [optional]  # noqa: E501
            network_device_top99p (UsageBillableSummaryBody): [optional]  # noqa: E501
            npm_flow_sum (UsageBillableSummaryBody): [optional]  # noqa: E501
            npm_host_sum (UsageBillableSummaryBody): [optional]  # noqa: E501
            npm_host_top99p (UsageBillableSummaryBody): [optional]  # noqa: E501
            prof_container_sum (UsageBillableSummaryBody): [optional]  # noqa: E501
            prof_host_top99p (UsageBillableSummaryBody): [optional]  # noqa: E501
            rum_sum (UsageBillableSummaryBody): [optional]  # noqa: E501
            serverless_invocation_sum (UsageBillableSummaryBody): [optional]  # noqa: E501
            siem_sum (UsageBillableSummaryBody): [optional]  # noqa: E501
            synthetics_api_tests_sum (UsageBillableSummaryBody): [optional]  # noqa: E501
            synthetics_browser_checks_sum (UsageBillableSummaryBody): [optional]  # noqa: E501
            timeseries_average (UsageBillableSummaryBody): [optional]  # noqa: E501
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Helper creating a new instance from a response."""

        self = super(UsageBillableSummaryKeys, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
