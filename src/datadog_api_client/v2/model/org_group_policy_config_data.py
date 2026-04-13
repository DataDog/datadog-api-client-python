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
    from datadog_api_client.v2.model.org_group_policy_config_attributes import OrgGroupPolicyConfigAttributes
    from datadog_api_client.v2.model.org_group_policy_config_type import OrgGroupPolicyConfigType


class OrgGroupPolicyConfigData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_group_policy_config_attributes import OrgGroupPolicyConfigAttributes
        from datadog_api_client.v2.model.org_group_policy_config_type import OrgGroupPolicyConfigType

        return {
            "attributes": (OrgGroupPolicyConfigAttributes,),
            "id": (str,),
            "type": (OrgGroupPolicyConfigType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: OrgGroupPolicyConfigAttributes, id: str, type: OrgGroupPolicyConfigType, **kwargs):
        """
        An org group policy config resource.

        :param attributes: Attributes of an org group policy config.
        :type attributes: OrgGroupPolicyConfigAttributes

        :param id: The identifier of the policy config (uses the config name).
        :type id: str

        :param type: Org group policy configs resource type.
        :type type: OrgGroupPolicyConfigType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
