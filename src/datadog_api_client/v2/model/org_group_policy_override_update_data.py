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
    from datadog_api_client.v2.model.org_group_policy_override_update_attributes import (
        OrgGroupPolicyOverrideUpdateAttributes,
    )
    from datadog_api_client.v2.model.org_group_policy_override_type import OrgGroupPolicyOverrideType


class OrgGroupPolicyOverrideUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_group_policy_override_update_attributes import (
            OrgGroupPolicyOverrideUpdateAttributes,
        )
        from datadog_api_client.v2.model.org_group_policy_override_type import OrgGroupPolicyOverrideType

        return {
            "attributes": (OrgGroupPolicyOverrideUpdateAttributes,),
            "id": (UUID,),
            "type": (OrgGroupPolicyOverrideType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: OrgGroupPolicyOverrideUpdateAttributes, id: UUID, type: OrgGroupPolicyOverrideType, **kwargs
    ):
        """
        Data for updating a policy override.

        :param attributes: Attributes for updating a policy override. The ``org_uuid`` and ``org_site`` fields must match the existing override and cannot be changed.
        :type attributes: OrgGroupPolicyOverrideUpdateAttributes

        :param id: The ID of the policy override.
        :type id: UUID

        :param type: Org group policy overrides resource type.
        :type type: OrgGroupPolicyOverrideType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
