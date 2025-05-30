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
    Whether a monitor is in draft or published state. Draft monitors do not notify recipients. Draft monitors are currently in
        preview and the field is only processed for enabled customers. This accepts the values `draft`
        and `published`. Defaults to published.

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
