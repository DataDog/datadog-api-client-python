# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IssuePullRequestType(ModelSimple):
    """
    Type of the object.

    :param value: If omitted defaults to "error_tracking_pull_request". Must be one of ["error_tracking_pull_request"].
    :type value: str
    """

    allowed_values = {
        "error_tracking_pull_request",
    }
    ERROR_TRACKING_PULL_REQUEST: ClassVar["IssuePullRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IssuePullRequestType.ERROR_TRACKING_PULL_REQUEST = IssuePullRequestType("error_tracking_pull_request")
