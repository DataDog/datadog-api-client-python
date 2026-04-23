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


class SyntheticsTestResultNetpathDestination(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "hostname": (str,),
            "ip_address": (str,),
            "port": (int,),
        }

    attribute_map = {
        "hostname": "hostname",
        "ip_address": "ip_address",
        "port": "port",
    }

    def __init__(
        self_,
        hostname: Union[str, UnsetType] = unset,
        ip_address: Union[str, UnsetType] = unset,
        port: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Destination endpoint of a network path measurement.

        :param hostname: Hostname of the destination.
        :type hostname: str, optional

        :param ip_address: IP address of the destination.
        :type ip_address: str, optional

        :param port: Port of the destination service.
        :type port: int, optional
        """
        if hostname is not unset:
            kwargs["hostname"] = hostname
        if ip_address is not unset:
            kwargs["ip_address"] = ip_address
        if port is not unset:
            kwargs["port"] = port
        super().__init__(kwargs)
