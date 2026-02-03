# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class WatchDataType(ModelSimple):
    """
    Rum replay watch resource type.

    :param value: If omitted defaults to "rum_replay_watch". Must be one of ["rum_replay_watch"].
    :type value: str
    """

    allowed_values = {
        "rum_replay_watch",
    }
    RUM_REPLAY_WATCH: ClassVar["WatchDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


WatchDataType.RUM_REPLAY_WATCH = WatchDataType("rum_replay_watch")
