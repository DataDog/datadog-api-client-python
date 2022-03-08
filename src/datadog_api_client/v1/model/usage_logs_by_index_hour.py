# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class UsageLogsByIndexHour(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "event_count": (int,),
            "hour": (datetime,),
            "index_id": (str,),
            "index_name": (str,),
            "org_name": (str,),
            "public_id": (str,),
            "retention": (int,),
        }

    attribute_map = {
        "event_count": "event_count",
        "hour": "hour",
        "index_id": "index_id",
        "index_name": "index_name",
        "org_name": "org_name",
        "public_id": "public_id",
        "retention": "retention",
    }

    def __init__(self, *args, **kwargs):
        """
        Number of indexed logs for each hour and index for a given organization.

        :param event_count: The total number of indexed logs for the queried hour.
        :type event_count: int, optional

        :param hour: The hour for the usage.
        :type hour: datetime, optional

        :param index_id: The index ID for this usage.
        :type index_id: str, optional

        :param index_name: The user specified name for this index ID.
        :type index_name: str, optional

        :param org_name: The organization name.
        :type org_name: str, optional

        :param public_id: The organization public ID.
        :type public_id: str, optional

        :param retention: The retention period (in days) for this index ID.
        :type retention: int, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UsageLogsByIndexHour, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
