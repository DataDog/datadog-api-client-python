# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class UsageAttributionPagination(ModelNormal):
    @cached_property
    def openapi_types(_):
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

    def __init__(self, *args, **kwargs):
        """
        The metadata for the current pagination.

        :param limit: Maximum amount of records to be returned.
        :type limit: int, optional

        :param offset: Records to be skipped before beginning to return.
        :type offset: int, optional

        :param sort_direction: Direction to sort by.
        :type sort_direction: str, optional

        :param sort_name: Field to sort by.
        :type sort_name: str, optional

        :param total_number_of_records: Total number of records.
        :type total_number_of_records: int, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UsageAttributionPagination, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
