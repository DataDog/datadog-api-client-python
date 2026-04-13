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
    from datadog_api_client.v2.model.org_group_policy_override_attributes import OrgGroupPolicyOverrideAttributes
    from datadog_api_client.v2.model.org_group_policy_override_relationships import OrgGroupPolicyOverrideRelationships
    from datadog_api_client.v2.model.org_group_policy_override_type import OrgGroupPolicyOverrideType


class OrgGroupPolicyOverrideData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_group_policy_override_attributes import OrgGroupPolicyOverrideAttributes
        from datadog_api_client.v2.model.org_group_policy_override_relationships import (
            OrgGroupPolicyOverrideRelationships,
        )
        from datadog_api_client.v2.model.org_group_policy_override_type import OrgGroupPolicyOverrideType

        return {
            "attributes": (OrgGroupPolicyOverrideAttributes,),
            "id": (UUID,),
            "relationships": (OrgGroupPolicyOverrideRelationships,),
            "type": (OrgGroupPolicyOverrideType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: OrgGroupPolicyOverrideAttributes,
        id: UUID,
        type: OrgGroupPolicyOverrideType,
        relationships: Union[OrgGroupPolicyOverrideRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        An org group policy override resource.

        :param attributes: Attributes of an org group policy override.
        :type attributes: OrgGroupPolicyOverrideAttributes

        :param id: The ID of the policy override.
        :type id: UUID

        :param relationships: Relationships of an org group policy override.
        :type relationships: OrgGroupPolicyOverrideRelationships, optional

        :param type: Org group policy overrides resource type.
        :type type: OrgGroupPolicyOverrideType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
