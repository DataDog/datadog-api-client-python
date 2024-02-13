# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class Case3rdPartyTicketStatus(ModelSimple):
    """
    Case status

    :param value: If omitted defaults to "IN_PROGRESS". Must be one of ["IN_PROGRESS", "COMPLETED", "FAILED"].
    :type value: str
    """

    allowed_values = {
        "IN_PROGRESS",
        "COMPLETED",
        "FAILED",
    }
    IN_PROGRESS: ClassVar["Case3rdPartyTicketStatus"]
    COMPLETED: ClassVar["Case3rdPartyTicketStatus"]
    FAILED: ClassVar["Case3rdPartyTicketStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


Case3rdPartyTicketStatus.IN_PROGRESS = Case3rdPartyTicketStatus("IN_PROGRESS")
Case3rdPartyTicketStatus.COMPLETED = Case3rdPartyTicketStatus("COMPLETED")
Case3rdPartyTicketStatus.FAILED = Case3rdPartyTicketStatus("FAILED")
