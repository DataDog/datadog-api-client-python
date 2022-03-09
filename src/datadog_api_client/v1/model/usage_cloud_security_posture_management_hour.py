# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
)


class UsageCloudSecurityPostureManagementHour(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "aas_host_count": (float, none_type),
            "azure_host_count": (float, none_type),
            "compliance_host_count": (float, none_type),
            "container_count": (float, none_type),
            "host_count": (float, none_type),
            "hour": (datetime,),
            "org_name": (str,),
            "public_id": (str,),
        }

    attribute_map = {
        "aas_host_count": "aas_host_count",
        "azure_host_count": "azure_host_count",
        "compliance_host_count": "compliance_host_count",
        "container_count": "container_count",
        "host_count": "host_count",
        "hour": "hour",
        "org_name": "org_name",
        "public_id": "public_id",
    }

    def __init__(self, *args, **kwargs):
        """
        Cloud Security Posture Management usage for a given organization for a given hour.

        :param aas_host_count: The number of Cloud Security Posture Management Azure app services hosts during a given hour.
        :type aas_host_count: float, none_type, optional

        :param azure_host_count: The number of Cloud Security Posture Management Azure hosts during a given hour.
        :type azure_host_count: float, none_type, optional

        :param compliance_host_count: The number of Cloud Security Posture Management hosts during a given hour.
        :type compliance_host_count: float, none_type, optional

        :param container_count: The total number of Cloud Security Posture Management containers during a given hour.
        :type container_count: float, none_type, optional

        :param host_count: The total number of Cloud Security Posture Management hosts during a given hour.
        :type host_count: float, none_type, optional

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

        self = super(UsageCloudSecurityPostureManagementHour, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
