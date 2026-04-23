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


class SyntheticsTestResultNetpathHop(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "hostname": (str,),
            "ip_address": (str,),
            "reachable": (bool,),
            "rtt": (float,),
            "ttl": (int,),
        }

    attribute_map = {
        "hostname": "hostname",
        "ip_address": "ip_address",
        "reachable": "reachable",
        "rtt": "rtt",
        "ttl": "ttl",
    }

    def __init__(
        self_,
        hostname: Union[str, UnsetType] = unset,
        ip_address: Union[str, UnsetType] = unset,
        reachable: Union[bool, UnsetType] = unset,
        rtt: Union[float, UnsetType] = unset,
        ttl: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        A single hop along a network path.

        :param hostname: Resolved hostname of the hop.
        :type hostname: str, optional

        :param ip_address: IP address of the hop.
        :type ip_address: str, optional

        :param reachable: Whether this hop was reachable.
        :type reachable: bool, optional

        :param rtt: Round-trip time to this hop in milliseconds.
        :type rtt: float, optional

        :param ttl: Time-to-live value of the probe packet at this hop.
        :type ttl: int, optional
        """
        if hostname is not unset:
            kwargs["hostname"] = hostname
        if ip_address is not unset:
            kwargs["ip_address"] = ip_address
        if reachable is not unset:
            kwargs["reachable"] = reachable
        if rtt is not unset:
            kwargs["rtt"] = rtt
        if ttl is not unset:
            kwargs["ttl"] = ttl
        super().__init__(kwargs)
