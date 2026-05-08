# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ReplayAnalysisScreenshot(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "screenshot_key": (str,),
            "session_id": (str,),
            "timestamp_ms": (int,),
            "view_id": (str,),
        }

    attribute_map = {
        "screenshot_key": "screenshot_key",
        "session_id": "session_id",
        "timestamp_ms": "timestamp_ms",
        "view_id": "view_id",
    }

    def __init__(self_, screenshot_key: str, session_id: str, timestamp_ms: int, view_id: str, **kwargs):
        """
        A screenshot captured during a replay session.

        :param screenshot_key: Filename or key identifier of the screenshot.
        :type screenshot_key: str

        :param session_id: Unique identifier of the session where the screenshot was taken.
        :type session_id: str

        :param timestamp_ms: Timestamp of the screenshot in milliseconds.
        :type timestamp_ms: int

        :param view_id: Unique identifier of the view where the screenshot was taken.
        :type view_id: str
        """
        super().__init__(kwargs)

        self_.screenshot_key = screenshot_key
        self_.session_id = session_id
        self_.timestamp_ms = timestamp_ms
        self_.view_id = view_id
