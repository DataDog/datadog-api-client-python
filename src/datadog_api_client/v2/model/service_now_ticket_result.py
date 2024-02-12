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


class ServiceNowTicketResult(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "sys_target_link": (str,),
        }

    attribute_map = {
        "sys_target_link": "sys_target_link",
    }

    def __init__(self_, sys_target_link: Union[str, UnsetType] = unset, **kwargs):
        """
        ServiceNow ticket information

        :param sys_target_link: Link to the Incident created on ServiceNow
        :type sys_target_link: str, optional
        """
        if sys_target_link is not unset:
            kwargs["sys_target_link"] = sys_target_link
        super().__init__(kwargs)
