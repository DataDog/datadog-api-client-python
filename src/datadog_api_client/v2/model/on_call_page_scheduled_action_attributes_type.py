# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OnCallPageScheduledActionAttributesType(ModelSimple):
    """
    The kind of action that is scheduled.

    :param value: Must be one of ["escalate", "resolve", "release", "retrigger"].
    :type value: str
    """

    allowed_values = {
        "escalate",
        "resolve",
        "release",
        "retrigger",
    }
    ESCALATE: ClassVar["OnCallPageScheduledActionAttributesType"]
    RESOLVE: ClassVar["OnCallPageScheduledActionAttributesType"]
    RELEASE: ClassVar["OnCallPageScheduledActionAttributesType"]
    RETRIGGER: ClassVar["OnCallPageScheduledActionAttributesType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OnCallPageScheduledActionAttributesType.ESCALATE = OnCallPageScheduledActionAttributesType("escalate")
OnCallPageScheduledActionAttributesType.RESOLVE = OnCallPageScheduledActionAttributesType("resolve")
OnCallPageScheduledActionAttributesType.RELEASE = OnCallPageScheduledActionAttributesType("release")
OnCallPageScheduledActionAttributesType.RETRIGGER = OnCallPageScheduledActionAttributesType("retrigger")
