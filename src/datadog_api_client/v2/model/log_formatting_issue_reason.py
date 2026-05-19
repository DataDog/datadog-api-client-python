# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LogFormattingIssueReason(ModelSimple):
    """
    A machine-readable reason explaining why logs from this source cannot be used by Cloud SIEM detection rules.
        `raw_wrapper` indicates the logs are delivered with their content wrapped in a `_raw` attribute (for example,
        from a third-party pipeline) so structured fields cannot be extracted.

    :param value: If omitted defaults to "raw_wrapper". Must be one of ["raw_wrapper"].
    :type value: str
    """

    allowed_values = {
        "raw_wrapper",
    }
    RAW_WRAPPER: ClassVar["LogFormattingIssueReason"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LogFormattingIssueReason.RAW_WRAPPER = LogFormattingIssueReason("raw_wrapper")
