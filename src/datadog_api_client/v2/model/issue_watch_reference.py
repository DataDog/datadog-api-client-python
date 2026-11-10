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
    from datadog_api_client.v2.model.issue_watch_type import IssueWatchType


class IssueWatchReference(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.issue_watch_type import IssueWatchType

        return {
            "id": (str,),
            "type": (IssueWatchType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: IssueWatchType, **kwargs):
        """
        An active watch on the issue.

        :param id: Watch identifier.
        :type id: str

        :param type: Type of the object.
        :type type: IssueWatchType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
