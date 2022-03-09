# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class UsageSNMPHour(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "hour": (datetime,),
            "org_name": (str,),
            "public_id": (str,),
            "snmp_devices": (int,),
        }

    attribute_map = {
        "hour": "hour",
        "org_name": "org_name",
        "public_id": "public_id",
        "snmp_devices": "snmp_devices",
    }

    def __init__(self, *args, **kwargs):
        """
        The number of SNMP devices for each hour for a given organization.

        :param hour: The hour for the usage.
        :type hour: datetime, optional

        :param org_name: The organization name.
        :type org_name: str, optional

        :param public_id: The organization public ID.
        :type public_id: str, optional

        :param snmp_devices: Contains the number of SNMP devices.
        :type snmp_devices: int, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UsageSNMPHour, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
