# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TemporaryGrantRequestGrantState(ModelSimple):
    """
    Current state of the grant associated with an approved request. Replaced means a successor superseded this grant; the successor need not still be active. Absent for requests that were not approved.

    :param value: Must be one of ["active", "expired", "revoked", "replaced"].
    :type value: str
    """

    allowed_values = {
        "active",
        "expired",
        "revoked",
        "replaced",
    }
    ACTIVE: ClassVar["TemporaryGrantRequestGrantState"]
    EXPIRED: ClassVar["TemporaryGrantRequestGrantState"]
    REVOKED: ClassVar["TemporaryGrantRequestGrantState"]
    REPLACED: ClassVar["TemporaryGrantRequestGrantState"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TemporaryGrantRequestGrantState.ACTIVE = TemporaryGrantRequestGrantState("active")
TemporaryGrantRequestGrantState.EXPIRED = TemporaryGrantRequestGrantState("expired")
TemporaryGrantRequestGrantState.REVOKED = TemporaryGrantRequestGrantState("revoked")
TemporaryGrantRequestGrantState.REPLACED = TemporaryGrantRequestGrantState("replaced")
