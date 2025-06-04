# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class MonitorDraftStatus(ModelSimple):
    """
    Indicates whether the monitor is in a draft or published state.

        `draft`: The monitor appears as Draft and does not send notifications.
        `published`: The monitor is active and evaluates conditions and notify as configured.

        This field is in preview. The draft value is only available to customers with the feature enabled.


    :param value: If omitted defaults to "published". Must be one of ["draft", "published"].
    :type value: str
    """

    allowed_values = {
        "draft",
        "published",
    }
    DRAFT: ClassVar["MonitorDraftStatus"]
    PUBLISHED: ClassVar["MonitorDraftStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


MonitorDraftStatus.DRAFT = MonitorDraftStatus("draft")
MonitorDraftStatus.PUBLISHED = MonitorDraftStatus("published")
