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
    from datadog_api_client.v2.model.org_group_policy_override_create_attributes import (
        OrgGroupPolicyOverrideCreateAttributes,
    )
    from datadog_api_client.v2.model.org_group_policy_override_create_relationships import (
        OrgGroupPolicyOverrideCreateRelationships,
    )
    from datadog_api_client.v2.model.org_group_policy_override_type import OrgGroupPolicyOverrideType


class OrgGroupPolicyOverrideCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_group_policy_override_create_attributes import (
            OrgGroupPolicyOverrideCreateAttributes,
        )
        from datadog_api_client.v2.model.org_group_policy_override_create_relationships import (
            OrgGroupPolicyOverrideCreateRelationships,
        )
        from datadog_api_client.v2.model.org_group_policy_override_type import OrgGroupPolicyOverrideType

        return {
            "attributes": (OrgGroupPolicyOverrideCreateAttributes,),
            "relationships": (OrgGroupPolicyOverrideCreateRelationships,),
            "type": (OrgGroupPolicyOverrideType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: OrgGroupPolicyOverrideCreateAttributes,
        relationships: OrgGroupPolicyOverrideCreateRelationships,
        type: OrgGroupPolicyOverrideType,
        **kwargs,
    ):
        """
        Data for creating an org group policy override.

        :param attributes: Attributes for creating a policy override.
        :type attributes: OrgGroupPolicyOverrideCreateAttributes

        :param relationships: Relationships for creating a policy override.
        :type relationships: OrgGroupPolicyOverrideCreateRelationships

        :param type: Org group policy overrides resource type.
        :type type: OrgGroupPolicyOverrideType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.relationships = relationships
        self_.type = type
