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
    from datadog_api_client.v2.model.org_group_policy_override_create_data import OrgGroupPolicyOverrideCreateData


class OrgGroupPolicyOverrideCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_group_policy_override_create_data import OrgGroupPolicyOverrideCreateData

        return {
            "data": (OrgGroupPolicyOverrideCreateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: OrgGroupPolicyOverrideCreateData, **kwargs):
        """
        Request to create an org group policy override.

        :param data: Data for creating an org group policy override.
        :type data: OrgGroupPolicyOverrideCreateData
        """
        super().__init__(kwargs)

        self_.data = data
