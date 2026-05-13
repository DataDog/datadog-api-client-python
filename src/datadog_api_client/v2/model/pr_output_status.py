# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class PROutputStatus(ModelSimple):
    """
    The current status of the pull request.

    :param value: Must be one of ["PENDING", "DRAFT", "READY", "MERGED", "CLOSED"].
    :type value: str
    """

    allowed_values = {
        "PENDING",
        "DRAFT",
        "READY",
        "MERGED",
        "CLOSED",
    }
    PENDING: ClassVar["PROutputStatus"]
    DRAFT: ClassVar["PROutputStatus"]
    READY: ClassVar["PROutputStatus"]
    MERGED: ClassVar["PROutputStatus"]
    CLOSED: ClassVar["PROutputStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


PROutputStatus.PENDING = PROutputStatus("PENDING")
PROutputStatus.DRAFT = PROutputStatus("DRAFT")
PROutputStatus.READY = PROutputStatus("READY")
PROutputStatus.MERGED = PROutputStatus("MERGED")
PROutputStatus.CLOSED = PROutputStatus("CLOSED")
