# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OnCallPageLinkEntityType(ModelSimple):
    """
    The type of a resource linked to a Page.

    :param value: Must be one of ["case", "incident", "page", "agent_conversation"].
    :type value: str
    """

    allowed_values = {
        "case",
        "incident",
        "page",
        "agent_conversation",
    }
    CASE: ClassVar["OnCallPageLinkEntityType"]
    INCIDENT: ClassVar["OnCallPageLinkEntityType"]
    PAGE: ClassVar["OnCallPageLinkEntityType"]
    AGENT_CONVERSATION: ClassVar["OnCallPageLinkEntityType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OnCallPageLinkEntityType.CASE = OnCallPageLinkEntityType("case")
OnCallPageLinkEntityType.INCIDENT = OnCallPageLinkEntityType("incident")
OnCallPageLinkEntityType.PAGE = OnCallPageLinkEntityType("page")
OnCallPageLinkEntityType.AGENT_CONVERSATION = OnCallPageLinkEntityType("agent_conversation")
