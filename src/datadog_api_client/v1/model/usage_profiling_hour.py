# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


class UsageProfilingHour(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "aas_count": (int, none_type),
            "avg_container_agent_count": (int, none_type),
            "host_count": (int, none_type),
            "hour": (datetime,),
            "org_name": (str,),
            "public_id": (str,),
        }

    attribute_map = {
        "aas_count": "aas_count",
        "avg_container_agent_count": "avg_container_agent_count",
        "host_count": "host_count",
        "hour": "hour",
        "org_name": "org_name",
        "public_id": "public_id",
    }

    def __init__(
        self_,
        aas_count: Union[int, none_type, UnsetType] = unset,
        avg_container_agent_count: Union[int, none_type, UnsetType] = unset,
        host_count: Union[int, none_type, UnsetType] = unset,
        hour: Union[datetime, UnsetType] = unset,
        org_name: Union[str, UnsetType] = unset,
        public_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The number of profiled hosts for each hour for a given organization.

        :param aas_count: Contains the total number of profiled Azure app services reporting during a given hour.
        :type aas_count: int, none_type, optional

        :param avg_container_agent_count: Get average number of container agents for that hour.
        :type avg_container_agent_count: int, none_type, optional

        :param host_count: Contains the total number of profiled hosts reporting during a given hour.
        :type host_count: int, none_type, optional

        :param hour: The hour for the usage.
        :type hour: datetime, optional

        :param org_name: The organization name.
        :type org_name: str, optional

        :param public_id: The organization public ID.
        :type public_id: str, optional
        """
        if aas_count is not unset:
            kwargs["aas_count"] = aas_count
        if avg_container_agent_count is not unset:
            kwargs["avg_container_agent_count"] = avg_container_agent_count
        if host_count is not unset:
            kwargs["host_count"] = host_count
        if hour is not unset:
            kwargs["hour"] = hour
        if org_name is not unset:
            kwargs["org_name"] = org_name
        if public_id is not unset:
            kwargs["public_id"] = public_id
        super().__init__(kwargs)
