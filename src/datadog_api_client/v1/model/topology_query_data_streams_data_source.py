# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TopologyQueryDataStreamsDataSource(ModelSimple):
    """
    Name of the data source.

    :param value: If omitted defaults to "data_streams". Must be one of ["data_streams"].
    :type value: str
    """

    allowed_values = {
        "data_streams",
    }
    DATA_STREAMS: ClassVar["TopologyQueryDataStreamsDataSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TopologyQueryDataStreamsDataSource.DATA_STREAMS = TopologyQueryDataStreamsDataSource("data_streams")
