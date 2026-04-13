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
    from datadog_api_client.v2.model.org_group_policy_relationship_to_one_data import (
        OrgGroupPolicyRelationshipToOneData,
    )


class OrgGroupPolicyRelationshipToOne(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_group_policy_relationship_to_one_data import (
            OrgGroupPolicyRelationshipToOneData,
        )

        return {
            "data": (OrgGroupPolicyRelationshipToOneData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: OrgGroupPolicyRelationshipToOneData, **kwargs):
        """
        Relationship to a single org group policy.

        :param data: A reference to an org group policy.
        :type data: OrgGroupPolicyRelationshipToOneData
        """
        super().__init__(kwargs)

        self_.data = data
