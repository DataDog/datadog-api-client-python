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
    from datadog_api_client.v2.model.escalation_policy_create_request_data import EscalationPolicyCreateRequestData


class EscalationPolicyCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.escalation_policy_create_request_data import EscalationPolicyCreateRequestData

        return {
            "data": (EscalationPolicyCreateRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: EscalationPolicyCreateRequestData, **kwargs):
        """
        Represents a request to create a new escalation policy, including the policy data.

        :param data: Represents the data for creating an escalation policy, including its attributes, relationships, and resource type.
        :type data: EscalationPolicyCreateRequestData
        """
        super().__init__(kwargs)

        self_.data = data
