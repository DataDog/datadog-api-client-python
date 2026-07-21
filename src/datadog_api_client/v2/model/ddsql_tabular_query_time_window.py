# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class DdsqlTabularQueryTimeWindow(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "from_timestamp": (int,),
            "to_timestamp": (int,),
        }

    attribute_map = {
        "from_timestamp": "from_timestamp",
        "to_timestamp": "to_timestamp",
    }

    def __init__(self_, from_timestamp: int, to_timestamp: int, **kwargs):
        """
        Time window scoping the underlying data sources, expressed in Unix milliseconds
        since the epoch. Inclusive on ``from_timestamp`` , exclusive on ``to_timestamp``.
        Results from static tables (for example, ``dd.hosts`` ) are not affected by the
        time window, but the field must still be provided.

        :param from_timestamp: Start of the query window (inclusive), in Unix milliseconds since the epoch.
        :type from_timestamp: int

        :param to_timestamp: End of the query window (exclusive), in Unix milliseconds since the epoch.
        :type to_timestamp: int
        """
        super().__init__(kwargs)

        self_.from_timestamp = from_timestamp
        self_.to_timestamp = to_timestamp
