# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.create_linear_issue_request_data_attributes import (
        CreateLinearIssueRequestDataAttributes,
    )
    from datadog_api_client.v2.model.create_linear_issue_request_data_relationships import (
        CreateLinearIssueRequestDataRelationships,
    )
    from datadog_api_client.v2.model.linear_issues_data_type import LinearIssuesDataType


class CreateLinearIssueRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_linear_issue_request_data_attributes import (
            CreateLinearIssueRequestDataAttributes,
        )
        from datadog_api_client.v2.model.create_linear_issue_request_data_relationships import (
            CreateLinearIssueRequestDataRelationships,
        )
        from datadog_api_client.v2.model.linear_issues_data_type import LinearIssuesDataType

        return {
            "attributes": (CreateLinearIssueRequestDataAttributes,),
            "relationships": (CreateLinearIssueRequestDataRelationships,),
            "type": (LinearIssuesDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        type: LinearIssuesDataType,
        attributes: Union[CreateLinearIssueRequestDataAttributes, UnsetType] = unset,
        relationships: Union[CreateLinearIssueRequestDataRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data of the Linear issue to create.

        :param attributes: Attributes of the Linear issue to create.
        :type attributes: CreateLinearIssueRequestDataAttributes, optional

        :param relationships: Relationships of the Linear issue to create.
        :type relationships: CreateLinearIssueRequestDataRelationships, optional

        :param type: Linear issues resource type.
        :type type: LinearIssuesDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.type = type
