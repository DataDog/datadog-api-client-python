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
    from datadog_api_client.v2.model.attach_linear_issue_request_data_attributes import (
        AttachLinearIssueRequestDataAttributes,
    )
    from datadog_api_client.v2.model.attach_linear_issue_request_data_relationships import (
        AttachLinearIssueRequestDataRelationships,
    )
    from datadog_api_client.v2.model.linear_issues_data_type import LinearIssuesDataType


class AttachLinearIssueRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.attach_linear_issue_request_data_attributes import (
            AttachLinearIssueRequestDataAttributes,
        )
        from datadog_api_client.v2.model.attach_linear_issue_request_data_relationships import (
            AttachLinearIssueRequestDataRelationships,
        )
        from datadog_api_client.v2.model.linear_issues_data_type import LinearIssuesDataType

        return {
            "attributes": (AttachLinearIssueRequestDataAttributes,),
            "relationships": (AttachLinearIssueRequestDataRelationships,),
            "type": (LinearIssuesDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: AttachLinearIssueRequestDataAttributes,
        relationships: AttachLinearIssueRequestDataRelationships,
        type: LinearIssuesDataType,
        **kwargs,
    ):
        """
        Data of the Linear issue to attach security findings to.

        :param attributes: Attributes of the Linear issue to attach security findings to.
        :type attributes: AttachLinearIssueRequestDataAttributes

        :param relationships: Relationships of the Linear issue to attach security findings to.
        :type relationships: AttachLinearIssueRequestDataRelationships

        :param type: Linear issues resource type.
        :type type: LinearIssuesDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.relationships = relationships
        self_.type = type
