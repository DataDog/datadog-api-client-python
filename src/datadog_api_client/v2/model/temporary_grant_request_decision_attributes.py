# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.temporary_grant_request_decision import TemporaryGrantRequestDecision


class TemporaryGrantRequestDecisionAttributes(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.temporary_grant_request_decision import TemporaryGrantRequestDecision

        return {
            "decision": (TemporaryGrantRequestDecision,),
        }

    attribute_map = {
        "decision": "decision",
    }

    def __init__(self_, decision: TemporaryGrantRequestDecision, **kwargs):
        """
        Binary decision. Overrides, reason fields, and unknown attributes are rejected, including null values.

        :param decision: Approve the exact submitted total and expiry, or deny the request.
        :type decision: TemporaryGrantRequestDecision
        """
        super().__init__(kwargs)

        self_.decision = decision
