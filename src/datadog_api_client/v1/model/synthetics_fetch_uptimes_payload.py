# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsFetchUptimesPayload(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "from_ts": (int,),
            "public_ids": ([str],),
            "to_ts": (int,),
        }

    attribute_map = {
        "from_ts": "from_ts",
        "public_ids": "public_ids",
        "to_ts": "to_ts",
    }

    def __init__(self_, from_ts: int, public_ids: List[str], to_ts: int, **kwargs):
        """
        Object containing IDs of Synthetic tests and a timeframe.

        :param from_ts: Timestamp in seconds (Unix epoch) for the start of uptime.
        :type from_ts: int

        :param public_ids: An array of Synthetic test IDs you want uptimes for.
        :type public_ids: [str]

        :param to_ts: Timestamp in seconds (Unix epoch) for the end of uptime.
        :type to_ts: int
        """
        super().__init__(kwargs)

        self_.from_ts = from_ts
        self_.public_ids = public_ids
        self_.to_ts = to_ts
