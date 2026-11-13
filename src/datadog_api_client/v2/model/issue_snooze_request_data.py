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
    from datadog_api_client.v2.model.issue_snooze_request_data_attributes import IssueSnoozeRequestDataAttributes
    from datadog_api_client.v2.model.issue_snooze_request_data_type import IssueSnoozeRequestDataType


class IssueSnoozeRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.issue_snooze_request_data_attributes import IssueSnoozeRequestDataAttributes
        from datadog_api_client.v2.model.issue_snooze_request_data_type import IssueSnoozeRequestDataType

        return {
            "attributes": (IssueSnoozeRequestDataAttributes,),
            "id": (str,),
            "type": (IssueSnoozeRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: IssueSnoozeRequestDataAttributes, id: str, type: IssueSnoozeRequestDataType, **kwargs
    ):
        """
        Snooze issue request.

        :param attributes: Object describing an issue snooze request.
        :type attributes: IssueSnoozeRequestDataAttributes

        :param id: Issue identifier.
        :type id: str

        :param type: Type of the object.
        :type type: IssueSnoozeRequestDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
