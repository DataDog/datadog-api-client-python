# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.org_group_policy_update_attributes import OrgGroupPolicyUpdateAttributes
    from datadog_api_client.v2.model.org_group_policy_type import OrgGroupPolicyType


class OrgGroupPolicyUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_group_policy_update_attributes import OrgGroupPolicyUpdateAttributes
        from datadog_api_client.v2.model.org_group_policy_type import OrgGroupPolicyType

        return {
            "attributes": (OrgGroupPolicyUpdateAttributes,),
            "id": (UUID,),
            "type": (OrgGroupPolicyType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: OrgGroupPolicyUpdateAttributes, id: UUID, type: OrgGroupPolicyType, **kwargs):
        """
        Data for updating an org group policy.

        :param attributes: Attributes for updating an org group policy.
        :type attributes: OrgGroupPolicyUpdateAttributes

        :param id: The ID of the policy.
        :type id: UUID

        :param type: Org group policies resource type.
        :type type: OrgGroupPolicyType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
