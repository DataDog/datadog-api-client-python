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


class RumHardcodedCrossProductSamplingUpdate(ModelNormal):
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
        Partial update for cross-product retention of a hardcoded retention filter.
        Only fields whose matching flag in ``cross_product_sampling_editability`` is ``true`` can be updated.

        :param session_replay_enabled: Controls whether Session Replay cross-product retention is active. Omit to leave unchanged.
        :type session_replay_enabled: bool, optional

        :param session_replay_sample_rate: Percentage (0–100) of retained sessions with an ingested replay whose replay data is kept.
            Omit to leave unchanged.
        :type session_replay_sample_rate: float, optional

        :param trace_enabled: Controls whether Trace cross-product retention is active. Omit to leave unchanged.
        :type trace_enabled: bool, optional

        :param trace_sample_rate: Percentage (0–100) of retained sessions with ingested traces whose traces are indexed.
            Omit to leave unchanged.
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
