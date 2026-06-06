# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TopologyQueryDataStreamsOrServiceMapDataSource(ModelSimple):
    """
    Name of the data source

    :param value: Must be one of ["data_streams", "service_map"].
    :type value: str
    """

    allowed_values = {
        "data_streams",
        "service_map",
    }
    DATA_STREAMS: ClassVar["TopologyQueryDataStreamsOrServiceMapDataSource"]
    SERVICE_MAP: ClassVar["TopologyQueryDataStreamsOrServiceMapDataSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TopologyQueryDataStreamsOrServiceMapDataSource.DATA_STREAMS = TopologyQueryDataStreamsOrServiceMapDataSource(
    "data_streams"
)
TopologyQueryDataStreamsOrServiceMapDataSource.SERVICE_MAP = TopologyQueryDataStreamsOrServiceMapDataSource(
    "service_map"
)
