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


class RumHardcodedCrossProductSamplingEditability(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "session_replay_sample_rate": (bool,),
            "trace_sample_rate": (bool,),
        }

    attribute_map = {
        "session_replay_sample_rate": "session_replay_sample_rate",
        "trace_sample_rate": "trace_sample_rate",
    }

    def __init__(
        self_,
        session_replay_sample_rate: Union[bool, UnsetType] = unset,
        trace_sample_rate: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Flags indicating which ``cross_product_sampling`` fields can be updated. Read-only.

        :param session_replay_sample_rate: If ``true`` , ``cross_product_sampling.session_replay_sample_rate`` can be updated on this filter.
        :type session_replay_sample_rate: bool, optional

        :param trace_sample_rate: If ``true`` , ``cross_product_sampling.trace_sample_rate`` can be updated on this filter.
        :type trace_sample_rate: bool, optional
        """
        if session_replay_sample_rate is not unset:
            kwargs["session_replay_sample_rate"] = session_replay_sample_rate
        if trace_sample_rate is not unset:
            kwargs["trace_sample_rate"] = trace_sample_rate
        super().__init__(kwargs)
