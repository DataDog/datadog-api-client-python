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


class RumCrossProductSampling(ModelNormal):
    validations = {
        "session_replay_sample_rate": {
            "inclusive_maximum": 100,
            "inclusive_minimum": 0,
        },
        "trace_sample_rate": {
            "inclusive_maximum": 100,
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "session_replay_enabled": (bool,),
            "session_replay_sample_rate": (float,),
            "trace_enabled": (bool,),
            "trace_sample_rate": (float,),
        }

    attribute_map = {
        "session_replay_enabled": "session_replay_enabled",
        "session_replay_sample_rate": "session_replay_sample_rate",
        "trace_enabled": "trace_enabled",
        "trace_sample_rate": "trace_sample_rate",
    }

    def __init__(
        self_,
        session_replay_enabled: Union[bool, UnsetType] = unset,
        session_replay_sample_rate: Union[float, UnsetType] = unset,
        trace_enabled: Union[bool, UnsetType] = unset,
        trace_sample_rate: Union[float, UnsetType] = unset,
        **kwargs,
    ):
        """
        The configuration for cross-product retention filters.

        :param session_replay_enabled: Whether the cross-product retention filter for Session Replay is enabled.
        :type session_replay_enabled: bool, optional

        :param session_replay_sample_rate: The sample rate for the Session Replay cross-product retention filter, between 0 and 100.
        :type session_replay_sample_rate: float, optional

        :param trace_enabled: Whether the cross-product retention filter for APM traces is enabled.
        :type trace_enabled: bool, optional

        :param trace_sample_rate: The sample rate for the APM cross-product retention filter, between 0 and 100. Values returned by the API are rounded to two decimal places.
        :type trace_sample_rate: float, optional
        """
        if session_replay_enabled is not unset:
            kwargs["session_replay_enabled"] = session_replay_enabled
        if session_replay_sample_rate is not unset:
            kwargs["session_replay_sample_rate"] = session_replay_sample_rate
        if trace_enabled is not unset:
            kwargs["trace_enabled"] = trace_enabled
        if trace_sample_rate is not unset:
            kwargs["trace_sample_rate"] = trace_sample_rate
        super().__init__(kwargs)
