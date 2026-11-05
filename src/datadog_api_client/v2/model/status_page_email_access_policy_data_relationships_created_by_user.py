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
    from datadog_api_client.v2.model.status_page_email_access_policy_data_relationships_created_by_user_data import (
        StatusPageEmailAccessPolicyDataRelationshipsCreatedByUserData,
    )


class StatusPageEmailAccessPolicyDataRelationshipsCreatedByUser(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.status_page_email_access_policy_data_relationships_created_by_user_data import (
            StatusPageEmailAccessPolicyDataRelationshipsCreatedByUserData,
        )

        return {
            "data": (StatusPageEmailAccessPolicyDataRelationshipsCreatedByUserData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: StatusPageEmailAccessPolicyDataRelationshipsCreatedByUserData, **kwargs):
        """
        The Datadog user who created the email access policy.

        :param data: The data object identifying the Datadog user who created the email access policy.
        :type data: StatusPageEmailAccessPolicyDataRelationshipsCreatedByUserData
        """
        super().__init__(kwargs)

        self_.data = data
