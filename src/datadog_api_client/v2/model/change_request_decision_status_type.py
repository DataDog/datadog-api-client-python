# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ChangeRequestDecisionStatusType(ModelSimple):
    """
    The status of a change request decision.

    :param value: Must be one of ["REQUESTED", "APPROVED", "DECLINED"].
    :type value: str
    """

    allowed_values = {
        "REQUESTED",
        "APPROVED",
        "DECLINED",
    }
    REQUESTED: ClassVar["ChangeRequestDecisionStatusType"]
    APPROVED: ClassVar["ChangeRequestDecisionStatusType"]
    DECLINED: ClassVar["ChangeRequestDecisionStatusType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ChangeRequestDecisionStatusType.REQUESTED = ChangeRequestDecisionStatusType("REQUESTED")
ChangeRequestDecisionStatusType.APPROVED = ChangeRequestDecisionStatusType("APPROVED")
ChangeRequestDecisionStatusType.DECLINED = ChangeRequestDecisionStatusType("DECLINED")
