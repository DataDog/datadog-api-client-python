# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CaseStatusGroup(ModelSimple):
    """
    Status group of the case.

    :param value: Must be one of ["SG_OPEN", "SG_IN_PROGRESS", "SG_CLOSED"].
    :type value: str
    """

    allowed_values = {
        "SG_OPEN",
        "SG_IN_PROGRESS",
        "SG_CLOSED",
    }
    SG_OPEN: ClassVar["CaseStatusGroup"]
    SG_IN_PROGRESS: ClassVar["CaseStatusGroup"]
    SG_CLOSED: ClassVar["CaseStatusGroup"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CaseStatusGroup.SG_OPEN = CaseStatusGroup("SG_OPEN")
CaseStatusGroup.SG_IN_PROGRESS = CaseStatusGroup("SG_IN_PROGRESS")
CaseStatusGroup.SG_CLOSED = CaseStatusGroup("SG_CLOSED")
