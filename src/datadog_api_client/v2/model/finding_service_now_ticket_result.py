# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class FindingServiceNowTicketResult(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "instance_name": (str,),
            "sys_id": (str,),
            "sys_target_link": (str,),
            "sys_target_sys_id": (str,),
            "table_name": (str,),
            "url": (str,),
        }

    attribute_map = {
        "instance_name": "instance_name",
        "sys_id": "sys_id",
        "sys_target_link": "sys_target_link",
        "sys_target_sys_id": "sys_target_sys_id",
        "table_name": "table_name",
        "url": "url",
    }

    def __init__(
        self_,
        instance_name: Union[str, UnsetType] = unset,
        sys_id: Union[str, UnsetType] = unset,
        sys_target_link: Union[str, UnsetType] = unset,
        sys_target_sys_id: Union[str, UnsetType] = unset,
        table_name: Union[str, UnsetType] = unset,
        url: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Result of the ServiceNow ticket creation or attachment.

        :param instance_name: ServiceNow instance name extracted from the ticket URL.
        :type instance_name: str, optional

        :param sys_id: Unique identifier of the ServiceNow incident record.
        :type sys_id: str, optional

        :param sys_target_link: Direct link to the ServiceNow incident record.
        :type sys_target_link: str, optional

        :param sys_target_sys_id: Unique identifier of the target ServiceNow record.
        :type sys_target_sys_id: str, optional

        :param table_name: ServiceNow table containing the incident record.
        :type table_name: str, optional

        :param url: URL of the ServiceNow incident record.
        :type url: str, optional
        """
        if instance_name is not unset:
            kwargs["instance_name"] = instance_name
        if sys_id is not unset:
            kwargs["sys_id"] = sys_id
        if sys_target_link is not unset:
            kwargs["sys_target_link"] = sys_target_link
        if sys_target_sys_id is not unset:
            kwargs["sys_target_sys_id"] = sys_target_sys_id
        if table_name is not unset:
            kwargs["table_name"] = table_name
        if url is not unset:
            kwargs["url"] = url
        super().__init__(kwargs)
