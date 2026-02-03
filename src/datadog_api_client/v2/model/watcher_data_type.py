# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class WatcherDataType(ModelSimple):
    """
    Rum replay watcher resource type.

    :param value: If omitted defaults to "rum_replay_watcher". Must be one of ["rum_replay_watcher"].
    :type value: str
    """

    allowed_values = {
        "rum_replay_watcher",
    }
    RUM_REPLAY_WATCHER: ClassVar["WatcherDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


WatcherDataType.RUM_REPLAY_WATCHER = WatcherDataType("rum_replay_watcher")
