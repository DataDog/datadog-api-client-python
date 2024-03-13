# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CustomDestinationAttributeTagsRestrictionListType(ModelSimple):
    """
    How `forward_tags_restriction_list` parameter should be interpreted.
        If `ALLOW_LIST`, then only tags whose keys on the forwarded logs match the ones on the restriction list
        are forwarded.

        `BLOCK_LIST` works the opposite way. It does not forward the tags matching the ones on the list.

    :param value: If omitted defaults to "ALLOW_LIST". Must be one of ["ALLOW_LIST", "BLOCK_LIST"].
    :type value: str
    """

    allowed_values = {
        "ALLOW_LIST",
        "BLOCK_LIST",
    }
    ALLOW_LIST: ClassVar["CustomDestinationAttributeTagsRestrictionListType"]
    BLOCK_LIST: ClassVar["CustomDestinationAttributeTagsRestrictionListType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CustomDestinationAttributeTagsRestrictionListType.ALLOW_LIST = CustomDestinationAttributeTagsRestrictionListType(
    "ALLOW_LIST"
)
CustomDestinationAttributeTagsRestrictionListType.BLOCK_LIST = CustomDestinationAttributeTagsRestrictionListType(
    "BLOCK_LIST"
)
