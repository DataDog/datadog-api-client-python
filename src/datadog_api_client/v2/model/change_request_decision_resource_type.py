# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ChangeRequestDecisionResourceType(ModelSimple):
    """
    Change request decision resource type.

    :param value: If omitted defaults to "change_request_decision". Must be one of ["change_request_decision"].
    :type value: str
    """

    allowed_values = {
        "change_request_decision",
    }
    CHANGE_REQUEST_DECISION: ClassVar["ChangeRequestDecisionResourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ChangeRequestDecisionResourceType.CHANGE_REQUEST_DECISION = ChangeRequestDecisionResourceType("change_request_decision")
