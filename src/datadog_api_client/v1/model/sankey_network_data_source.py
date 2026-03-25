# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SankeyNetworkDataSource(ModelSimple):
    """
    Network data source type.

    :param value: If omitted defaults to "network". Must be one of ["network_device_flows", "network"].
    :type value: str
    """

    allowed_values = {
        "network_device_flows",
        "network",
    }
    NETWORK_DEVICE_FLOWS: ClassVar["SankeyNetworkDataSource"]
    NETWORK: ClassVar["SankeyNetworkDataSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SankeyNetworkDataSource.NETWORK_DEVICE_FLOWS = SankeyNetworkDataSource("network_device_flows")
SankeyNetworkDataSource.NETWORK = SankeyNetworkDataSource("network")
