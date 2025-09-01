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
    from datadog_api_client.v2.model.issue_update_assignee_request_data_type import IssueUpdateAssigneeRequestDataType


class IssueUpdateAssigneeRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.issue_update_assignee_request_data_type import (
            IssueUpdateAssigneeRequestDataType,
        )

        return {
            "id": (str,),
            "type": (IssueUpdateAssigneeRequestDataType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: IssueUpdateAssigneeRequestDataType, **kwargs):
        """
        Update issue assignee request.

        :param id: User identifier.
        :type id: str

        :param type: Type of the object.
        :type type: IssueUpdateAssigneeRequestDataType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
