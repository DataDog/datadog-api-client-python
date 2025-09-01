# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class IssuesSearchResultAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "impacted_sessions": (int,),
            "impacted_users": (int,),
            "total_count": (int,),
        }

    attribute_map = {
        "impacted_sessions": "impacted_sessions",
        "impacted_users": "impacted_users",
        "total_count": "total_count",
    }

    def __init__(
        self_,
        impacted_sessions: Union[int, UnsetType] = unset,
        impacted_users: Union[int, UnsetType] = unset,
        total_count: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object containing the information of a search result.

        :param impacted_sessions: Count of sessions impacted by the issue over the queried time window.
        :type impacted_sessions: int, optional

        :param impacted_users: Count of users impacted by the issue over the queried time window.
        :type impacted_users: int, optional

        :param total_count: Total count of errors that match the issue over the queried time window.
        :type total_count: int, optional
        """
        if impacted_sessions is not unset:
            kwargs["impacted_sessions"] = impacted_sessions
        if impacted_users is not unset:
            kwargs["impacted_users"] = impacted_users
        if total_count is not unset:
            kwargs["total_count"] = total_count
        super().__init__(kwargs)
