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
    from datadog_api_client.v2.model.org_group_policy_create_data import OrgGroupPolicyCreateData


class OrgGroupPolicyCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_group_policy_create_data import OrgGroupPolicyCreateData

        return {
            "data": (OrgGroupPolicyCreateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: OrgGroupPolicyCreateData, **kwargs):
        """
        Request to create an org group policy.

        :param data: Data for creating an org group policy.
        :type data: OrgGroupPolicyCreateData
        """
        super().__init__(kwargs)

        self_.data = data
