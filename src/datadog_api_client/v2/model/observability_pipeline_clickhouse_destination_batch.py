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


class ObservabilityPipelineClickhouseDestinationBatch(ModelNormal):
    validations = {
        "max_events": {
            "inclusive_minimum": 1,
        },
        "timeout_secs": {
            "inclusive_maximum": 65535,
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "max_events": (int,),
            "timeout_secs": (int,),
        }

    attribute_map = {
        "max_events": "max_events",
        "timeout_secs": "timeout_secs",
    }

    def __init__(
        self_, max_events: Union[int, UnsetType] = unset, timeout_secs: Union[int, UnsetType] = unset, **kwargs
    ):
        """
        Batching configuration for ClickHouse inserts.

        :param max_events: Maximum number of events per batch before it is flushed.
        :type max_events: int, optional

        :param timeout_secs: Maximum number of seconds to wait before flushing a partial batch.
        :type timeout_secs: int, optional
        """
        if max_events is not unset:
            kwargs["max_events"] = max_events
        if timeout_secs is not unset:
            kwargs["timeout_secs"] = timeout_secs
        super().__init__(kwargs)
