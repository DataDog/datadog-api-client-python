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
    from datadog_api_client.v2.model.org_group_policy_override_data import OrgGroupPolicyOverrideData


class OrgGroupPolicyOverrideResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_group_policy_override_data import OrgGroupPolicyOverrideData

        return {
            "data": (OrgGroupPolicyOverrideData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: OrgGroupPolicyOverrideData, **kwargs):
        """
        Response containing a single org group policy override.

        :param data: An org group policy override resource.
        :type data: OrgGroupPolicyOverrideData
        """
        super().__init__(kwargs)

        self_.data = data
