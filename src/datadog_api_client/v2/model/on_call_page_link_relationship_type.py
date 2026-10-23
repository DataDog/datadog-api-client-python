# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OnCallPageLinkRelationshipType(ModelSimple):
    """
    How the parent resource relates to the child resource.

    :param value: Must be one of ["relates_to", "causes", "blocks", "duplicates", "parent_of", "successor_of", "escalates_to", "pages"].
    :type value: str
    """

    allowed_values = {
        "relates_to",
        "causes",
        "blocks",
        "duplicates",
        "parent_of",
        "successor_of",
        "escalates_to",
        "pages",
    }
    RELATES_TO: ClassVar["OnCallPageLinkRelationshipType"]
    CAUSES: ClassVar["OnCallPageLinkRelationshipType"]
    BLOCKS: ClassVar["OnCallPageLinkRelationshipType"]
    DUPLICATES: ClassVar["OnCallPageLinkRelationshipType"]
    PARENT_OF: ClassVar["OnCallPageLinkRelationshipType"]
    SUCCESSOR_OF: ClassVar["OnCallPageLinkRelationshipType"]
    ESCALATES_TO: ClassVar["OnCallPageLinkRelationshipType"]
    PAGES: ClassVar["OnCallPageLinkRelationshipType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OnCallPageLinkRelationshipType.RELATES_TO = OnCallPageLinkRelationshipType("relates_to")
OnCallPageLinkRelationshipType.CAUSES = OnCallPageLinkRelationshipType("causes")
OnCallPageLinkRelationshipType.BLOCKS = OnCallPageLinkRelationshipType("blocks")
OnCallPageLinkRelationshipType.DUPLICATES = OnCallPageLinkRelationshipType("duplicates")
OnCallPageLinkRelationshipType.PARENT_OF = OnCallPageLinkRelationshipType("parent_of")
OnCallPageLinkRelationshipType.SUCCESSOR_OF = OnCallPageLinkRelationshipType("successor_of")
OnCallPageLinkRelationshipType.ESCALATES_TO = OnCallPageLinkRelationshipType("escalates_to")
OnCallPageLinkRelationshipType.PAGES = OnCallPageLinkRelationshipType("pages")
