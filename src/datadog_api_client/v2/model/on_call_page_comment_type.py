# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OnCallPageCommentType(ModelSimple):
    """
    Indicates that the resource is of type `comments`.

    :param value: If omitted defaults to "comments". Must be one of ["comments"].
    :type value: str
    """

    allowed_values = {
        "comments",
    }
    COMMENTS: ClassVar["OnCallPageCommentType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OnCallPageCommentType.COMMENTS = OnCallPageCommentType("comments")
