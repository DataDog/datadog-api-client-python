# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IoCTriageState(ModelSimple):
    """
    Current triage state of the indicator.

    :param value: Must be one of ["not_reviewed", "reviewed"].
    :type value: str
    """

    allowed_values = {
        "not_reviewed",
        "reviewed",
    }
    NOT_REVIEWED: ClassVar["IoCTriageState"]
    REVIEWED: ClassVar["IoCTriageState"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IoCTriageState.NOT_REVIEWED = IoCTriageState("not_reviewed")
IoCTriageState.REVIEWED = IoCTriageState("reviewed")
