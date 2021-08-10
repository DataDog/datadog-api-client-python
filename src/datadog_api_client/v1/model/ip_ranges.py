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
    from datadog_api_client.v1.model.ip_prefixes_agents import IPPrefixesAgents
    from datadog_api_client.v1.model.ip_prefixes_api import IPPrefixesAPI
    from datadog_api_client.v1.model.ip_prefixes_apm import IPPrefixesAPM
    from datadog_api_client.v1.model.ip_prefixes_logs import IPPrefixesLogs
    from datadog_api_client.v1.model.ip_prefixes_process import IPPrefixesProcess
    from datadog_api_client.v1.model.ip_prefixes_synthetics import IPPrefixesSynthetics
    from datadog_api_client.v1.model.ip_prefixes_webhooks import IPPrefixesWebhooks

    globals()["IPPrefixesAPI"] = IPPrefixesAPI
    globals()["IPPrefixesAPM"] = IPPrefixesAPM
    globals()["IPPrefixesAgents"] = IPPrefixesAgents
    globals()["IPPrefixesLogs"] = IPPrefixesLogs
    globals()["IPPrefixesProcess"] = IPPrefixesProcess
    globals()["IPPrefixesSynthetics"] = IPPrefixesSynthetics
    globals()["IPPrefixesWebhooks"] = IPPrefixesWebhooks


class IPRanges(ModelNormal):
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
            "agents": (IPPrefixesAgents,),  # noqa: E501
            "api": (IPPrefixesAPI,),  # noqa: E501
            "apm": (IPPrefixesAPM,),  # noqa: E501
            "logs": (IPPrefixesLogs,),  # noqa: E501
            "modified": (str,),  # noqa: E501
            "process": (IPPrefixesProcess,),  # noqa: E501
            "synthetics": (IPPrefixesSynthetics,),  # noqa: E501
            "version": (int,),  # noqa: E501
            "webhooks": (IPPrefixesWebhooks,),  # noqa: E501
        }

    discriminator = None

    attribute_map = {
        "agents": "agents",  # noqa: E501
        "api": "api",  # noqa: E501
        "apm": "apm",  # noqa: E501
        "logs": "logs",  # noqa: E501
        "modified": "modified",  # noqa: E501
        "process": "process",  # noqa: E501
        "synthetics": "synthetics",  # noqa: E501
        "version": "version",  # noqa: E501
        "webhooks": "webhooks",  # noqa: E501
    }

    read_only_vars = {}

    _composed_schemas = {}

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """IPRanges - a model defined in OpenAPI

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
            agents (IPPrefixesAgents): [optional]  # noqa: E501
            api (IPPrefixesAPI): [optional]  # noqa: E501
            apm (IPPrefixesAPM): [optional]  # noqa: E501
            logs (IPPrefixesLogs): [optional]  # noqa: E501
            modified (str): Date when last updated, in the form `YYYY-MM-DD-hh-mm-ss`.. [optional]  # noqa: E501
            process (IPPrefixesProcess): [optional]  # noqa: E501
            synthetics (IPPrefixesSynthetics): [optional]  # noqa: E501
            version (int): Version of the IP list.. [optional]  # noqa: E501
            webhooks (IPPrefixesWebhooks): [optional]  # noqa: E501
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Helper creating a new instance from a response."""

        self = super(IPRanges, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
