# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class NotifyEndState(StringEnum):
    """
    A notification end state.

    :param value: Must be one of ["alert", "no data", "warn"].
    :type value: str
    """

    allowed_values = {
        "alert",
        "no data",
        "warn",
    }
    ALERT: ClassVar["NotifyEndState"]
    NO_DATA: ClassVar["NotifyEndState"]
    WARN: ClassVar["NotifyEndState"]


NotifyEndState.ALERT = NotifyEndState("alert")
NotifyEndState.NO_DATA = NotifyEndState("no data")
NotifyEndState.WARN = NotifyEndState("warn")
