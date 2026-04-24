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


class SyntheticsTestResultRouter(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "ip": (str,),
            "resolved_host": (str,),
        }

    attribute_map = {
        "ip": "ip",
        "resolved_host": "resolved_host",
    }

    def __init__(self_, ip: Union[str, UnsetType] = unset, resolved_host: Union[str, UnsetType] = unset, **kwargs):
        """
        A router along the traceroute path.

        :param ip: IP address of the router.
        :type ip: str, optional

        :param resolved_host: Resolved hostname of the router.
        :type resolved_host: str, optional
        """
        if ip is not unset:
            kwargs["ip"] = ip
        if resolved_host is not unset:
            kwargs["resolved_host"] = resolved_host
        super().__init__(kwargs)
