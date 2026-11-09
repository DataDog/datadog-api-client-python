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
    from datadog_api_client.v2.model.status_page_email_access_policy_data_relationships_created_by_user import (
        StatusPageEmailAccessPolicyDataRelationshipsCreatedByUser,
    )
    from datadog_api_client.v2.model.status_page_email_access_policy_data_relationships_status_page import (
        StatusPageEmailAccessPolicyDataRelationshipsStatusPage,
    )


class StatusPageEmailAccessPolicyDataRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.status_page_email_access_policy_data_relationships_created_by_user import (
            StatusPageEmailAccessPolicyDataRelationshipsCreatedByUser,
        )
        from datadog_api_client.v2.model.status_page_email_access_policy_data_relationships_status_page import (
            StatusPageEmailAccessPolicyDataRelationshipsStatusPage,
        )

        return {
            "created_by_user": (StatusPageEmailAccessPolicyDataRelationshipsCreatedByUser,),
            "status_page": (StatusPageEmailAccessPolicyDataRelationshipsStatusPage,),
        }

    attribute_map = {
        "created_by_user": "created_by_user",
        "status_page": "status_page",
    }

    def __init__(
        self_,
        created_by_user: StatusPageEmailAccessPolicyDataRelationshipsCreatedByUser,
        status_page: StatusPageEmailAccessPolicyDataRelationshipsStatusPage,
        **kwargs,
    ):
        """
        Relationships of a status page email access policy.

        :param created_by_user: The Datadog user who created the email access policy.
        :type created_by_user: StatusPageEmailAccessPolicyDataRelationshipsCreatedByUser

        :param status_page: The status page associated with the email access policy.
        :type status_page: StatusPageEmailAccessPolicyDataRelationshipsStatusPage
        """
        super().__init__(kwargs)

        self_.created_by_user = created_by_user
        self_.status_page = status_page
