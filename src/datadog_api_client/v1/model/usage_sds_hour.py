# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class UsageSDSHour(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "hour": (datetime,),
            "logs_scanned_bytes": (int,),
            "org_name": (str,),
            "public_id": (str,),
            "total_scanned_bytes": (int,),
        }

    attribute_map = {
        "hour": "hour",
        "logs_scanned_bytes": "logs_scanned_bytes",
        "org_name": "org_name",
        "public_id": "public_id",
        "total_scanned_bytes": "total_scanned_bytes",
    }

    def __init__(self, *args, **kwargs):
        """
        Sensitive Data Scanner usage for a given organization for a given hour.

        :param hour: The hour for the usage.
        :type hour: datetime, optional

        :param logs_scanned_bytes: The total number of bytes scanned of logs usage by the Sensitive Data Scanner from the start of the given hour’s month until the given hour.
        :type logs_scanned_bytes: int, optional

        :param org_name: The organization name.
        :type org_name: str, optional

        :param public_id: The organization public ID.
        :type public_id: str, optional

        :param total_scanned_bytes: The total number of bytes scanned across all usage types by the Sensitive Data Scanner from the start of the given hour’s month until the given hour.
        :type total_scanned_bytes: int, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UsageSDSHour, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
