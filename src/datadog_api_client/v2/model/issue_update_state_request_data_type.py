# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IssueUpdateStateRequestDataType(ModelSimple):
    """
    Type of the object.

    :param value: If omitted defaults to "error_tracking_issue". Must be one of ["error_tracking_issue"].
    :type value: str
    """

    allowed_values = {
        "error_tracking_issue",
    }
    ERROR_TRACKING_ISSUE: ClassVar["IssueUpdateStateRequestDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IssueUpdateStateRequestDataType.ERROR_TRACKING_ISSUE = IssueUpdateStateRequestDataType("error_tracking_issue")
