# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.org_group_policy_attributes import OrgGroupPolicyAttributes
    from datadog_api_client.v2.model.org_group_policy_relationships import OrgGroupPolicyRelationships
    from datadog_api_client.v2.model.org_group_policy_type import OrgGroupPolicyType


class OrgGroupPolicyData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_group_policy_attributes import OrgGroupPolicyAttributes
        from datadog_api_client.v2.model.org_group_policy_relationships import OrgGroupPolicyRelationships
        from datadog_api_client.v2.model.org_group_policy_type import OrgGroupPolicyType

        return {
            "attributes": (OrgGroupPolicyAttributes,),
            "id": (UUID,),
            "relationships": (OrgGroupPolicyRelationships,),
            "type": (OrgGroupPolicyType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: OrgGroupPolicyAttributes,
        id: UUID,
        type: OrgGroupPolicyType,
        relationships: Union[OrgGroupPolicyRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        An org group policy resource.

        :param attributes: Attributes of an org group policy.
        :type attributes: OrgGroupPolicyAttributes

        :param id: The ID of the org group policy.
        :type id: UUID

        :param relationships: Relationships of an org group policy.
        :type relationships: OrgGroupPolicyRelationships, optional

        :param type: Org group policies resource type.
        :type type: OrgGroupPolicyType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
