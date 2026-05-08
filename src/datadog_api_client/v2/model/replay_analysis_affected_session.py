# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class ReplayAnalysisAffectedSession(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "session_id": (str,),
            "session_start_timestamp_ms": (int, none_type),
        }

    attribute_map = {
        "session_id": "session_id",
        "session_start_timestamp_ms": "session_start_timestamp_ms",
    }

    def __init__(
        self_, session_id: str, session_start_timestamp_ms: Union[int, none_type, UnsetType] = unset, **kwargs
    ):
        """
        A session affected by a replay analysis issue.

        :param session_id: Unique identifier of the affected session.
        :type session_id: str

        :param session_start_timestamp_ms: Session start timestamp in milliseconds.
        :type session_start_timestamp_ms: int, none_type, optional
        """
        if session_start_timestamp_ms is not unset:
            kwargs["session_start_timestamp_ms"] = session_start_timestamp_ms
        super().__init__(kwargs)

        self_.session_id = session_id
