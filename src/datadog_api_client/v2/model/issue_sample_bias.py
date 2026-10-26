# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IssueSampleBias(ModelSimple):
    """
    Criterion used to pick a sample. `latest` picks the most recent error. `git_metadata` picks the most
        recent error with source code metadata, whose stack trace is parsed. `trace` picks the most recent error
        with an APM trace. `session_replay` picks the most recent error with a RUM session replay.
        `exception_replay` picks the most recent error with an Exception Replay snapshot.

    :param value: Must be one of ["latest", "git_metadata", "trace", "session_replay", "exception_replay"].
    :type value: str
    """

    allowed_values = {
        "latest",
        "git_metadata",
        "trace",
        "session_replay",
        "exception_replay",
    }
    LATEST: ClassVar["IssueSampleBias"]
    GIT_METADATA: ClassVar["IssueSampleBias"]
    TRACE: ClassVar["IssueSampleBias"]
    SESSION_REPLAY: ClassVar["IssueSampleBias"]
    EXCEPTION_REPLAY: ClassVar["IssueSampleBias"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IssueSampleBias.LATEST = IssueSampleBias("latest")
IssueSampleBias.GIT_METADATA = IssueSampleBias("git_metadata")
IssueSampleBias.TRACE = IssueSampleBias("trace")
IssueSampleBias.SESSION_REPLAY = IssueSampleBias("session_replay")
IssueSampleBias.EXCEPTION_REPLAY = IssueSampleBias("exception_replay")
