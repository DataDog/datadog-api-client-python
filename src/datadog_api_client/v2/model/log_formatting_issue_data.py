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
    from datadog_api_client.v2.model.log_formatting_issue_attributes import LogFormattingIssueAttributes
    from datadog_api_client.v2.model.log_formatting_issue_type import LogFormattingIssueType


class LogFormattingIssueData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.log_formatting_issue_attributes import LogFormattingIssueAttributes
        from datadog_api_client.v2.model.log_formatting_issue_type import LogFormattingIssueType

        return {
            "attributes": (LogFormattingIssueAttributes,),
            "id": (str,),
            "type": (LogFormattingIssueType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: LogFormattingIssueAttributes, id: str, type: LogFormattingIssueType, **kwargs):
        """
        A log source that has formatting issues preventing it from being used by Cloud SIEM detection rules.

        :param attributes: Attributes describing why a log source is not properly formatted for Cloud SIEM detection rules.
        :type attributes: LogFormattingIssueAttributes

        :param id: The name of the log source that has formatting issues.
        :type id: str

        :param type: The type of the resource. The value should always be ``log_formatting_issues``.
        :type type: LogFormattingIssueType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
