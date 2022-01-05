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


class UsageAttributionPagination(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "limit": (int,),
            "offset": (int,),
            "sort_direction": (str,),
            "sort_name": (str,),
            "total_number_of_records": (int,),
        }

    attribute_map = {
        "limit": "limit",
        "offset": "offset",
        "sort_direction": "sort_direction",
        "sort_name": "sort_name",
        "total_number_of_records": "total_number_of_records",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """UsageAttributionPagination - a model defined in OpenAPI

        Keyword Args:
            limit (int): [optional] Maximum amount of records to be returned.
            offset (int): [optional] Records to be skipped before beginning to return.
            sort_direction (str): [optional] Direction to sort by.
            sort_name (str): [optional] Field to sort by.
            total_number_of_records (int): [optional] Total number of records.
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UsageAttributionPagination, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
