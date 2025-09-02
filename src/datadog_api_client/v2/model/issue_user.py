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
    from datadog_api_client.v2.model.issue_user_attributes import IssueUserAttributes
    from datadog_api_client.v2.model.issue_user_type import IssueUserType


class IssueUser(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.issue_user_attributes import IssueUserAttributes
        from datadog_api_client.v2.model.issue_user_type import IssueUserType

        return {
            "attributes": (IssueUserAttributes,),
            "id": (str,),
            "type": (IssueUserType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: IssueUserAttributes, id: str, type: IssueUserType, **kwargs):
        """
        The user to whom the issue is assigned.

        :param attributes: Object containing the information of a user.
        :type attributes: IssueUserAttributes

        :param id: User identifier.
        :type id: str

        :param type: Type of the object
        :type type: IssueUserType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
