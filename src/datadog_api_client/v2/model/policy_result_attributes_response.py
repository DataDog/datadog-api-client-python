# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


class PolicyResultAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "active": (bool,),
            "payload": (dict,),
            "policy_type": (str,),
            "reference_org_uuid": (UUID,),
        }

    attribute_map = {
        "active": "active",
        "payload": "payload",
        "policy_type": "policy_type",
        "reference_org_uuid": "reference_org_uuid",
    }

    def __init__(self_, active: bool, payload: dict, policy_type: str, reference_org_uuid: UUID, **kwargs):
        """
        Attributes of a policy evaluation result.

        :param active: Whether the policy is active.
        :type active: bool

        :param payload: The policy configuration payload.
        :type payload: dict

        :param policy_type: The type of policy being evaluated.
        :type policy_type: str

        :param reference_org_uuid: The organization UUID reference.
        :type reference_org_uuid: UUID
        """
        super().__init__(kwargs)

        self_.active = active
        self_.payload = payload
        self_.policy_type = policy_type
        self_.reference_org_uuid = reference_org_uuid
