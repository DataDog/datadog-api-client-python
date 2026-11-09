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
    from datadog_api_client.v2.model.status_page_email_access_policy_data_attributes import (
        StatusPageEmailAccessPolicyDataAttributes,
    )
    from datadog_api_client.v2.model.status_page_email_access_policy_data_relationships import (
        StatusPageEmailAccessPolicyDataRelationships,
    )
    from datadog_api_client.v2.model.status_page_email_access_policy_type import StatusPageEmailAccessPolicyType


class StatusPageEmailAccessPolicyData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.status_page_email_access_policy_data_attributes import (
            StatusPageEmailAccessPolicyDataAttributes,
        )
        from datadog_api_client.v2.model.status_page_email_access_policy_data_relationships import (
            StatusPageEmailAccessPolicyDataRelationships,
        )
        from datadog_api_client.v2.model.status_page_email_access_policy_type import StatusPageEmailAccessPolicyType

        return {
            "attributes": (StatusPageEmailAccessPolicyDataAttributes,),
            "id": (UUID,),
            "relationships": (StatusPageEmailAccessPolicyDataRelationships,),
            "type": (StatusPageEmailAccessPolicyType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: StatusPageEmailAccessPolicyDataAttributes,
        id: UUID,
        relationships: StatusPageEmailAccessPolicyDataRelationships,
        type: StatusPageEmailAccessPolicyType,
        **kwargs,
    ):
        """
        The data object for a status page email access policy.

        :param attributes: Attributes of a status page email access policy.
        :type attributes: StatusPageEmailAccessPolicyDataAttributes

        :param id: The ID of the email access policy.
        :type id: UUID

        :param relationships: Relationships of a status page email access policy.
        :type relationships: StatusPageEmailAccessPolicyDataRelationships

        :param type: Status page email access policy resource type.
        :type type: StatusPageEmailAccessPolicyType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.relationships = relationships
        self_.type = type
