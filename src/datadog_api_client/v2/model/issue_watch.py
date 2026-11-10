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
    from datadog_api_client.v2.model.issue_watch_attributes import IssueWatchAttributes
    from datadog_api_client.v2.model.issue_watch_type import IssueWatchType


class IssueWatch(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.issue_watch_attributes import IssueWatchAttributes
        from datadog_api_client.v2.model.issue_watch_type import IssueWatchType

        return {
            "attributes": (IssueWatchAttributes,),
            "id": (str,),
            "type": (IssueWatchType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: IssueWatchAttributes, id: str, type: IssueWatchType, **kwargs):
        """
        An active watch on an issue. A watch moves an ignored issue back to open when its condition is met.

        :param attributes: Object containing the information of a watch.
        :type attributes: IssueWatchAttributes

        :param id: Watch identifier.
        :type id: str

        :param type: Type of the object.
        :type type: IssueWatchType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
