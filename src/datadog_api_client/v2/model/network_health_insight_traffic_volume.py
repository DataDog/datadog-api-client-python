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


class NetworkHealthInsightTrafficVolume(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "bytes_read": (int,),
            "bytes_written": (int,),
            "total_traffic": (int,),
        }

    attribute_map = {
        "bytes_read": "bytes_read",
        "bytes_written": "bytes_written",
        "total_traffic": "total_traffic",
    }

    def __init__(
        self_,
        bytes_read: Union[int, UnsetType] = unset,
        bytes_written: Union[int, UnsetType] = unset,
        total_traffic: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Network traffic volume metrics between the client and server services during the query window.

        :param bytes_read: Total bytes read from the server to the client during the query window.
        :type bytes_read: int, optional

        :param bytes_written: Total bytes written from the client to the server during the query window.
        :type bytes_written: int, optional

        :param total_traffic: Sum of bytes written and bytes read across the query window.
        :type total_traffic: int, optional
        """
        if bytes_read is not unset:
            kwargs["bytes_read"] = bytes_read
        if bytes_written is not unset:
            kwargs["bytes_written"] = bytes_written
        if total_traffic is not unset:
            kwargs["total_traffic"] = total_traffic
        super().__init__(kwargs)
