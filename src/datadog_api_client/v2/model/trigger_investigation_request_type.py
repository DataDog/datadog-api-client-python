# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TriggerInvestigationRequestType(ModelSimple):
    """
    The resource type for trigger investigation requests.

    :param value: If omitted defaults to "trigger_investigation_request". Must be one of ["trigger_investigation_request"].
    :type value: str
    """

    allowed_values = {
        "trigger_investigation_request",
    }
    TRIGGER_INVESTIGATION_REQUEST: ClassVar["TriggerInvestigationRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TriggerInvestigationRequestType.TRIGGER_INVESTIGATION_REQUEST = TriggerInvestigationRequestType(
    "trigger_investigation_request"
)
