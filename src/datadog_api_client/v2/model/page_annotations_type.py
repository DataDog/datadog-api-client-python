# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class PageAnnotationsType(ModelSimple):
    """
    Page annotations resource type.

    :param value: If omitted defaults to "page_annotations". Must be one of ["page_annotations"].
    :type value: str
    """

    allowed_values = {
        "page_annotations",
    }
    PAGE_ANNOTATIONS: ClassVar["PageAnnotationsType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


PageAnnotationsType.PAGE_ANNOTATIONS = PageAnnotationsType("page_annotations")
