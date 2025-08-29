# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.issue import Issue
    from datadog_api_client.v2.model.issue_included import IssueIncluded
    from datadog_api_client.v2.model.issue_case import IssueCase
    from datadog_api_client.v2.model.issue_user import IssueUser
    from datadog_api_client.v2.model.issue_team import IssueTeam


class IssueResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.issue import Issue
        from datadog_api_client.v2.model.issue_included import IssueIncluded

        return {
            "data": (Issue,),
            "included": ([IssueIncluded],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(
        self_,
        data: Union[Issue, UnsetType] = unset,
        included: Union[List[Union[IssueIncluded, IssueCase, IssueUser, IssueTeam]], UnsetType] = unset,
        **kwargs,
    ):
        """
        Response containing error tracking issue data.

        :param data: The issue matching the request.
        :type data: Issue, optional

        :param included: Array of resources related to the issue.
        :type included: [IssueIncluded], optional
        """
        if data is not unset:
            kwargs["data"] = data
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)
