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
    from datadog_api_client.v1.model.usage_summary_date_org import UsageSummaryDateOrg

    globals()["UsageSummaryDateOrg"] = UsageSummaryDateOrg


class UsageSummaryDate(ModelNormal):
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
            "agent_host_top99p": (int,),  # noqa: E501
            "apm_azure_app_service_host_top99p": (int,),  # noqa: E501
            "apm_host_top99p": (int,),  # noqa: E501
            "aws_host_top99p": (int,),  # noqa: E501
            "aws_lambda_func_count": (int,),  # noqa: E501
            "aws_lambda_invocations_sum": (int,),  # noqa: E501
            "azure_app_service_top99p": (int,),  # noqa: E501
            "billable_ingested_bytes_sum": (int,),  # noqa: E501
            "compliance_container_count_sum": (
                bool,
                date,
                datetime,
                dict,
                float,
                int,
                list,
                str,
                none_type,
            ),  # noqa: E501
            "compliance_host_count_sum": (int,),  # noqa: E501
            "container_avg": (int,),  # noqa: E501
            "container_hwm": (int,),  # noqa: E501
            "custom_ts_avg": (int,),  # noqa: E501
            "date": (datetime,),  # noqa: E501
            "fargate_tasks_count_avg": (int,),  # noqa: E501
            "fargate_tasks_count_hwm": (int,),  # noqa: E501
            "gcp_host_top99p": (int,),  # noqa: E501
            "heroku_host_top99p_sum": (int,),  # noqa: E501
            "incident_management_monthly_active_users_hwm": (int,),  # noqa: E501
            "indexed_events_count_sum": (int,),  # noqa: E501
            "infra_host_top99p": (int,),  # noqa: E501
            "ingested_events_bytes_sum": (int,),  # noqa: E501
            "iot_device_agg_sum": (int,),  # noqa: E501
            "iot_device_top99p_sum": (int,),  # noqa: E501
            "mobile_rum_session_count_android_sum": (int,),  # noqa: E501
            "mobile_rum_session_count_ios_sum": (int,),  # noqa: E501
            "mobile_rum_session_count_sum": (int,),  # noqa: E501
            "netflow_indexed_events_count_sum": (int,),  # noqa: E501
            "npm_host_top99p": (int,),  # noqa: E501
            "opentelemetry_host_top99p_sum": (int,),  # noqa: E501
            "orgs": ([UsageSummaryDateOrg],),  # noqa: E501
            "profiling_host_top99p": (int,),  # noqa: E501
            "rum_session_count_sum": (int,),  # noqa: E501
            "rum_total_session_count_sum": (int,),  # noqa: E501
            "synthetics_browser_check_calls_count_sum": (int,),  # noqa: E501
            "synthetics_check_calls_count_sum": (int,),  # noqa: E501
            "trace_search_indexed_events_count_sum": (int,),  # noqa: E501
            "twol_ingested_events_bytes_sum": (int,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None

    attribute_map = {
        "agent_host_top99p": "agent_host_top99p",  # noqa: E501
        "apm_azure_app_service_host_top99p": "apm_azure_app_service_host_top99p",  # noqa: E501
        "apm_host_top99p": "apm_host_top99p",  # noqa: E501
        "aws_host_top99p": "aws_host_top99p",  # noqa: E501
        "aws_lambda_func_count": "aws_lambda_func_count",  # noqa: E501
        "aws_lambda_invocations_sum": "aws_lambda_invocations_sum",  # noqa: E501
        "azure_app_service_top99p": "azure_app_service_top99p",  # noqa: E501
        "billable_ingested_bytes_sum": "billable_ingested_bytes_sum",  # noqa: E501
        "compliance_container_count_sum": "compliance_container_count_sum",  # noqa: E501
        "compliance_host_count_sum": "compliance_host_count_sum",  # noqa: E501
        "container_avg": "container_avg",  # noqa: E501
        "container_hwm": "container_hwm",  # noqa: E501
        "custom_ts_avg": "custom_ts_avg",  # noqa: E501
        "date": "date",  # noqa: E501
        "fargate_tasks_count_avg": "fargate_tasks_count_avg",  # noqa: E501
        "fargate_tasks_count_hwm": "fargate_tasks_count_hwm",  # noqa: E501
        "gcp_host_top99p": "gcp_host_top99p",  # noqa: E501
        "heroku_host_top99p_sum": "heroku_host_top99p_sum",  # noqa: E501
        "incident_management_monthly_active_users_hwm": "incident_management_monthly_active_users_hwm",  # noqa: E501
        "indexed_events_count_sum": "indexed_events_count_sum",  # noqa: E501
        "infra_host_top99p": "infra_host_top99p",  # noqa: E501
        "ingested_events_bytes_sum": "ingested_events_bytes_sum",  # noqa: E501
        "iot_device_agg_sum": "iot_device_agg_sum",  # noqa: E501
        "iot_device_top99p_sum": "iot_device_top99p_sum",  # noqa: E501
        "mobile_rum_session_count_android_sum": "mobile_rum_session_count_android_sum",  # noqa: E501
        "mobile_rum_session_count_ios_sum": "mobile_rum_session_count_ios_sum",  # noqa: E501
        "mobile_rum_session_count_sum": "mobile_rum_session_count_sum",  # noqa: E501
        "netflow_indexed_events_count_sum": "netflow_indexed_events_count_sum",  # noqa: E501
        "npm_host_top99p": "npm_host_top99p",  # noqa: E501
        "opentelemetry_host_top99p_sum": "opentelemetry_host_top99p_sum",  # noqa: E501
        "orgs": "orgs",  # noqa: E501
        "profiling_host_top99p": "profiling_host_top99p",  # noqa: E501
        "rum_session_count_sum": "rum_session_count_sum",  # noqa: E501
        "rum_total_session_count_sum": "rum_total_session_count_sum",  # noqa: E501
        "synthetics_browser_check_calls_count_sum": "synthetics_browser_check_calls_count_sum",  # noqa: E501
        "synthetics_check_calls_count_sum": "synthetics_check_calls_count_sum",  # noqa: E501
        "trace_search_indexed_events_count_sum": "trace_search_indexed_events_count_sum",  # noqa: E501
        "twol_ingested_events_bytes_sum": "twol_ingested_events_bytes_sum",  # noqa: E501
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
        """UsageSummaryDate - a model defined in OpenAPI

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
            agent_host_top99p (int): Shows the 99th percentile of all agent hosts over all hours in the current date for all organizations.. [optional]  # noqa: E501
            apm_azure_app_service_host_top99p (int): Shows the 99th percentile of all Azure app services using APM over all hours in the current date all organizations.. [optional]  # noqa: E501
            apm_host_top99p (int): Shows the 99th percentile of all distinct APM hosts over all hours in the current date for all organizations.. [optional]  # noqa: E501
            aws_host_top99p (int): Shows the 99th percentile of all AWS hosts over all hours in the current date for all organizations.. [optional]  # noqa: E501
            aws_lambda_func_count (int): Shows the average of the number of functions that executed 1 or more times each hour in the current date for all organizations.. [optional]  # noqa: E501
            aws_lambda_invocations_sum (int): Shows the sum of all AWS Lambda invocations over all hours in the current date for all organizations.. [optional]  # noqa: E501
            azure_app_service_top99p (int): Shows the 99th percentile of all Azure app services over all hours in the current date for all organizations.. [optional]  # noqa: E501
            billable_ingested_bytes_sum (int): Shows the sum of all log bytes ingested over all hours in the current date for all organizations.. [optional]  # noqa: E501
            compliance_container_count_sum (bool, date, datetime, dict, float, int, list, str, none_type): Shows the sum of compliance containers over all hours in the current date for all organizations.. [optional]  # noqa: E501
            compliance_host_count_sum (int): Shows the sum of compliance hosts over all hours in the current date for all organizations.. [optional]  # noqa: E501
            container_avg (int): Shows the average of all distinct containers over all hours in the current date for all organizations.. [optional]  # noqa: E501
            container_hwm (int): Shows the high-water mark of all distinct containers over all hours in the current date for all organizations.. [optional]  # noqa: E501
            custom_ts_avg (int): Shows the average number of distinct custom metrics over all hours in the current date for all organizations.. [optional]  # noqa: E501
            date (datetime): The date for the usage.. [optional]  # noqa: E501
            fargate_tasks_count_avg (int): Shows the high-watermark of all Fargate tasks over all hours in the current date for all organizations.. [optional]  # noqa: E501
            fargate_tasks_count_hwm (int): Shows the average of all Fargate tasks over all hours in the current date for all organizations.. [optional]  # noqa: E501
            gcp_host_top99p (int): Shows the 99th percentile of all GCP hosts over all hours in the current date for all organizations.. [optional]  # noqa: E501
            heroku_host_top99p_sum (int): Shows the 99th percentile of all Heroku dynos over all hours in the current date for all organizations.. [optional]  # noqa: E501
            incident_management_monthly_active_users_hwm (int): Shows the high-water mark of incident management monthly active users over all hours in the current date for all organizations.. [optional]  # noqa: E501
            indexed_events_count_sum (int): Shows the sum of all log events indexed over all hours in the current date for all organizations.. [optional]  # noqa: E501
            infra_host_top99p (int): Shows the 99th percentile of all distinct infrastructure hosts over all hours in the current date for all organizations.. [optional]  # noqa: E501
            ingested_events_bytes_sum (int): Shows the sum of all log bytes ingested over all hours in the current date for all organizations.. [optional]  # noqa: E501
            iot_device_agg_sum (int): Shows the sum of all IoT devices over all hours in the current date for all organizations.. [optional]  # noqa: E501
            iot_device_top99p_sum (int): Shows the 99th percentile of all IoT devices over all hours in the current date all organizations.. [optional]  # noqa: E501
            mobile_rum_session_count_android_sum (int): Shows the sum of all mobile RUM Sessions on Android over all hours in the current date for all organizations.. [optional]  # noqa: E501
            mobile_rum_session_count_ios_sum (int): Shows the sum of all mobile RUM Sessions on iOS over all hours in the current date for all organizations.. [optional]  # noqa: E501
            mobile_rum_session_count_sum (int): Shows the sum of all mobile RUM Sessions over all hours in the current date for all organizations. [optional]  # noqa: E501
            netflow_indexed_events_count_sum (int): Shows the sum of all Network flows indexed over all hours in the current date for all organizations.. [optional]  # noqa: E501
            npm_host_top99p (int): Shows the 99th percentile of all distinct Networks hosts over all hours in the current date for all organizations.. [optional]  # noqa: E501
            opentelemetry_host_top99p_sum (int): Shows the 99th percentile of all hosts reported by the Datadog exporter for the OpenTelemetry Collector over all hours in the current date for all organizations.. [optional]  # noqa: E501
            orgs ([UsageSummaryDateOrg]): Organizations associated with a user.. [optional]  # noqa: E501
            profiling_host_top99p (int): Shows the 99th percentile of all profiled hosts over all hours in the current date for all organizations.. [optional]  # noqa: E501
            rum_session_count_sum (int): Shows the sum of all browser RUM Sessions over all hours in the current date for all organizations. [optional]  # noqa: E501
            rum_total_session_count_sum (int): Shows the sum of RUM Sessions (browser and mobile) over all hours in the current date for all organizations.. [optional]  # noqa: E501
            synthetics_browser_check_calls_count_sum (int): Shows the sum of all Synthetic browser tests over all hours in the current date for all organizations.. [optional]  # noqa: E501
            synthetics_check_calls_count_sum (int): Shows the sum of all Synthetic API tests over all hours in the current date for all organizations.. [optional]  # noqa: E501
            trace_search_indexed_events_count_sum (int): Shows the sum of all Indexed Spans indexed over all hours in the current date for all organizations.. [optional]  # noqa: E501
            twol_ingested_events_bytes_sum (int): Shows the sum of all tracing without limits bytes ingested over all hours in the current date for all organizations.. [optional]  # noqa: E501
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
