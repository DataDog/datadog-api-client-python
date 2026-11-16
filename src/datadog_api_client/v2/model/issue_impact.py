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
    from datadog_api_client.v2.model.issue_impact_attributes import IssueImpactAttributes
    from datadog_api_client.v2.model.issue_impact_type import IssueImpactType


class IssueImpact(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.issue_impact_attributes import IssueImpactAttributes
        from datadog_api_client.v2.model.issue_impact_type import IssueImpactType

        return {
            "attributes": (IssueImpactAttributes,),
            "id": (str,),
            "type": (IssueImpactType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: IssueImpactAttributes, id: str, type: IssueImpactType, **kwargs):
        """
        The impact of an issue over the requested time window.

        :param attributes: The issue's errors in the time window, and the users, sessions, accounts, views, and endpoints they affect.
        :type attributes: IssueImpactAttributes

        :param id: Identifier of the issue.
        :type id: str

        :param type: Type of the object.
        :type type: IssueImpactType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
