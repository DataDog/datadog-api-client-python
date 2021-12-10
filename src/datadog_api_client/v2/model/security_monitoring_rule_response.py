# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    date,
    datetime,
    file_type,
    none_type,
)


def lazy_import():
    from datadog_api_client.v2.model.security_monitoring_filter import SecurityMonitoringFilter
    from datadog_api_client.v2.model.security_monitoring_rule_case import SecurityMonitoringRuleCase
    from datadog_api_client.v2.model.security_monitoring_rule_options import SecurityMonitoringRuleOptions
    from datadog_api_client.v2.model.security_monitoring_rule_query import SecurityMonitoringRuleQuery
    from datadog_api_client.v2.model.security_monitoring_rule_type_read import SecurityMonitoringRuleTypeRead

    globals()["SecurityMonitoringFilter"] = SecurityMonitoringFilter
    globals()["SecurityMonitoringRuleCase"] = SecurityMonitoringRuleCase
    globals()["SecurityMonitoringRuleOptions"] = SecurityMonitoringRuleOptions
    globals()["SecurityMonitoringRuleQuery"] = SecurityMonitoringRuleQuery
    globals()["SecurityMonitoringRuleTypeRead"] = SecurityMonitoringRuleTypeRead


class SecurityMonitoringRuleResponse(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the name of the attribute. The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.

      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      validations (dict): The key is the name of the attribute. The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.

    """

    validations = {}

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
            "cases": ([SecurityMonitoringRuleCase],),
            "created_at": (int,),
            "creation_author_id": (int,),
            "filters": ([SecurityMonitoringFilter],),
            "has_extended_title": (bool,),
            "id": (str,),
            "is_default": (bool,),
            "is_deleted": (bool,),
            "is_enabled": (bool,),
            "message": (str,),
            "name": (str,),
            "options": (SecurityMonitoringRuleOptions,),
            "queries": ([SecurityMonitoringRuleQuery],),
            "tags": ([str],),
            "type": (SecurityMonitoringRuleTypeRead,),
            "update_author_id": (int,),
            "version": (int,),
        }

    attribute_map = {
        "cases": "cases",
        "created_at": "createdAt",
        "creation_author_id": "creationAuthorId",
        "filters": "filters",
        "has_extended_title": "hasExtendedTitle",
        "id": "id",
        "is_default": "isDefault",
        "is_deleted": "isDeleted",
        "is_enabled": "isEnabled",
        "message": "message",
        "name": "name",
        "options": "options",
        "queries": "queries",
        "tags": "tags",
        "type": "type",
        "update_author_id": "updateAuthorId",
        "version": "version",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """SecurityMonitoringRuleResponse - a model defined in OpenAPI

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
            cases ([SecurityMonitoringRuleCase]): Cases for generating signals.. [optional]
            created_at (int): When the rule was created, timestamp in milliseconds.. [optional]
            creation_author_id (int): User ID of the user who created the rule.. [optional]
            filters ([SecurityMonitoringFilter]): Additional queries to filter matched events before they are processed.. [optional]
            has_extended_title (bool): Whether the notifications include the triggering group-by values in their title.. [optional]
            id (str): The ID of the rule.. [optional]
            is_default (bool): Whether the rule is included by default.. [optional]
            is_deleted (bool): Whether the rule has been deleted.. [optional]
            is_enabled (bool): Whether the rule is enabled.. [optional]
            message (str): Message for generated signals.. [optional]
            name (str): The name of the rule.. [optional]
            options (SecurityMonitoringRuleOptions): [optional]
            queries ([SecurityMonitoringRuleQuery]): Queries for selecting logs which are part of the rule.. [optional]
            tags ([str]): Tags for generated signals.. [optional]
            type (SecurityMonitoringRuleTypeRead): [optional]
            update_author_id (int): User ID of the user who updated the rule.. [optional]
            version (int): The version of the rule.. [optional]
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SecurityMonitoringRuleResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
