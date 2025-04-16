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
    from datadog_api_client.v2.model.escalation_policy_update_request_data import EscalationPolicyUpdateRequestData


class EscalationPolicyUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.escalation_policy_update_request_data import EscalationPolicyUpdateRequestData

        return {
            "data": (EscalationPolicyUpdateRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: EscalationPolicyUpdateRequestData, **kwargs):
        """
        Represents a request to update an existing escalation policy, including the updated policy data.

        :param data: Represents the data for updating an existing escalation policy, including its ID, attributes, relationships, and resource type.
        :type data: EscalationPolicyUpdateRequestData
        """
        super().__init__(kwargs)

        self_.data = data
