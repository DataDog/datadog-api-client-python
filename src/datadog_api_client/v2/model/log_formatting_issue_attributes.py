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
    from datadog_api_client.v2.model.log_formatting_issue_reason import LogFormattingIssueReason


class LogFormattingIssueAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.log_formatting_issue_reason import LogFormattingIssueReason

        return {
            "reason": (LogFormattingIssueReason,),
        }

    attribute_map = {
        "reason": "reason",
    }

    def __init__(self_, reason: LogFormattingIssueReason, **kwargs):
        """
        Attributes describing why a log source is not properly formatted for Cloud SIEM detection rules.

        :param reason: A machine-readable reason explaining why logs from this source cannot be used by Cloud SIEM detection rules.
            ``raw_wrapper`` indicates the logs are delivered with their content wrapped in a ``_raw`` attribute (for example,
            from a third-party pipeline) so structured fields cannot be extracted.
        :type reason: LogFormattingIssueReason
        """
        super().__init__(kwargs)

        self_.reason = reason
