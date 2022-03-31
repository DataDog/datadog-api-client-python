# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class UsageDBMHour(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "dbm_host_count": (int,),
            "dbm_queries_count": (int,),
            "hour": (datetime,),
            "org_name": (str,),
            "public_id": (str,),
        }

    attribute_map = {
        "dbm_host_count": "dbm_host_count",
        "dbm_queries_count": "dbm_queries_count",
        "hour": "hour",
        "org_name": "org_name",
        "public_id": "public_id",
    }

    def __init__(self, *args, **kwargs):
        """
        Database Monitoring usage for a given organization for a given hour.

        :param dbm_host_count: The total number of Database Monitoring host hours from the start of the given hour’s month until the given hour.
        :type dbm_host_count: int, optional

        :param dbm_queries_count: The total number of normalized Database Monitoring queries from the start of the given hour’s month until the given hour.
        :type dbm_queries_count: int, optional

        :param hour: The hour for the usage.
        :type hour: datetime, optional

        :param org_name: The organization name.
        :type org_name: str, optional

        :param public_id: The organization public ID.
        :type public_id: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UsageDBMHour, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
