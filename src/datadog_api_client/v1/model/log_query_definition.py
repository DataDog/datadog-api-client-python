# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (  # noqa: F401
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
    from datadog_api_client.v1.model.log_query_definition_group_by import LogQueryDefinitionGroupBy
    from datadog_api_client.v1.model.log_query_definition_search import LogQueryDefinitionSearch
    from datadog_api_client.v1.model.logs_query_compute import LogsQueryCompute

    globals()["LogQueryDefinitionGroupBy"] = LogQueryDefinitionGroupBy
    globals()["LogQueryDefinitionSearch"] = LogQueryDefinitionSearch
    globals()["LogsQueryCompute"] = LogsQueryCompute


class LogQueryDefinition(ModelNormal):
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
            "compute": (LogsQueryCompute,),
            "group_by": ([LogQueryDefinitionGroupBy],),
            "index": (str,),
            "multi_compute": ([LogsQueryCompute],),
            "search": (LogQueryDefinitionSearch,),
        }

    attribute_map = {
        "compute": "compute",
        "group_by": "group_by",
        "index": "index",
        "multi_compute": "multi_compute",
        "search": "search",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """LogQueryDefinition - a model defined in OpenAPI

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
            compute (LogsQueryCompute): [optional]
            group_by ([LogQueryDefinitionGroupBy]): List of tag prefixes to group by in the case of a cluster check.. [optional]
            index (str): A coma separated-list of index names. Use \"*\" query all indexes at once. [Multiple Indexes](https://docs.datadoghq.com/logs/indexes/#multiple-indexes). [optional]
            multi_compute ([LogsQueryCompute]): This field is mutually exclusive with `compute`.. [optional]
            search (LogQueryDefinitionSearch): [optional]
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogQueryDefinition, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
