# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LegacyIssueStreamRequestResponseFormat(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: If omitted defaults to "event_list". Must be one of ["event_list"].
    :type value: str
    """

    allowed_values = {
        "event_list",
    }
    EVENT_LIST: ClassVar["LegacyIssueStreamRequestResponseFormat"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LegacyIssueStreamRequestResponseFormat.EVENT_LIST = LegacyIssueStreamRequestResponseFormat("event_list")
