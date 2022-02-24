# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class UsageIncidentManagementHour(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "hour": (datetime,),
            "monthly_active_users": (int,),
            "org_name": (str,),
            "public_id": (str,),
        }

    attribute_map = {
        "hour": "hour",
        "monthly_active_users": "monthly_active_users",
        "org_name": "org_name",
        "public_id": "public_id",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """
        Incident management usage for a given organization for a given hour.

        :param hour: The hour for the usage.
        :type hour: datetime, optional

        :param monthly_active_users: Contains the total number monthly active users from the start of the given hour's month until the given hour.
        :type monthly_active_users: int, optional

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

        self = super(UsageIncidentManagementHour, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
