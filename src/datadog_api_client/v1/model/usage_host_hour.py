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


class UsageHostHour(ModelNormal):
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
        return {
            "agent_host_count": (int,),  # noqa: E501
            "alibaba_host_count": (int,),  # noqa: E501
            "apm_azure_app_service_host_count": (int,),  # noqa: E501
            "apm_host_count": (int,),  # noqa: E501
            "aws_host_count": (int,),  # noqa: E501
            "azure_host_count": (int,),  # noqa: E501
            "container_count": (int,),  # noqa: E501
            "gcp_host_count": (int,),  # noqa: E501
            "heroku_host_count": (int,),  # noqa: E501
            "host_count": (int,),  # noqa: E501
            "hour": (datetime,),  # noqa: E501
            "infra_azure_app_service": (int,),  # noqa: E501
            "opentelemetry_host_count": (int,),  # noqa: E501
            "vsphere_host_count": (int,),  # noqa: E501
        }

    discriminator = None

    attribute_map = {
        "agent_host_count": "agent_host_count",  # noqa: E501
        "alibaba_host_count": "alibaba_host_count",  # noqa: E501
        "apm_azure_app_service_host_count": "apm_azure_app_service_host_count",  # noqa: E501
        "apm_host_count": "apm_host_count",  # noqa: E501
        "aws_host_count": "aws_host_count",  # noqa: E501
        "azure_host_count": "azure_host_count",  # noqa: E501
        "container_count": "container_count",  # noqa: E501
        "gcp_host_count": "gcp_host_count",  # noqa: E501
        "heroku_host_count": "heroku_host_count",  # noqa: E501
        "host_count": "host_count",  # noqa: E501
        "hour": "hour",  # noqa: E501
        "infra_azure_app_service": "infra_azure_app_service",  # noqa: E501
        "opentelemetry_host_count": "opentelemetry_host_count",  # noqa: E501
        "vsphere_host_count": "vsphere_host_count",  # noqa: E501
    }

    read_only_vars = {}

    _composed_schemas = {}

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """UsageHostHour - a model defined in OpenAPI

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
            agent_host_count (int): Contains the total number of infrastructure hosts reporting during a given hour that were running the Datadog Agent.. [optional]  # noqa: E501
            alibaba_host_count (int): Contains the total number of hosts that reported via Alibaba integration (and were NOT running the Datadog Agent).. [optional]  # noqa: E501
            apm_azure_app_service_host_count (int): Contains the total number of Azure App Services hosts using APM.. [optional]  # noqa: E501
            apm_host_count (int): Shows the total number of hosts using APM during the hour, these are counted as billable (except during trial periods).. [optional]  # noqa: E501
            aws_host_count (int): Contains the total number of hosts that reported via the AWS integration (and were NOT running the Datadog Agent).. [optional]  # noqa: E501
            azure_host_count (int): Contains the total number of hosts that reported via Azure integration (and were NOT running the Datadog Agent).. [optional]  # noqa: E501
            container_count (int): Shows the total number of containers reported by the Docker integration during the hour.. [optional]  # noqa: E501
            gcp_host_count (int): Contains the total number of hosts that reported via the Google Cloud integration (and were NOT running the Datadog Agent).. [optional]  # noqa: E501
            heroku_host_count (int): Contains the total number of Heroku dynos reported by the Datadog Agent.. [optional]  # noqa: E501
            host_count (int): Contains the total number of billable infrastructure hosts reporting during a given hour. This is the sum of `agent_host_count`, `aws_host_count`, and `gcp_host_count`.. [optional]  # noqa: E501
            hour (datetime): The hour for the usage.. [optional]  # noqa: E501
            infra_azure_app_service (int): Contains the total number of hosts that reported via the Azure App Services integration (and were NOT running the Datadog Agent).. [optional]  # noqa: E501
            opentelemetry_host_count (int): Contains the total number of hosts reported by Datadog exporter for the OpenTelemetry Collector.. [optional]  # noqa: E501
            vsphere_host_count (int): Contains the total number of hosts that reported via vSphere integration (and were NOT running the Datadog Agent).. [optional]  # noqa: E501
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Helper creating a new instance from a response."""

        self = super(UsageHostHour, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
