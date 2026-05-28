# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AnnotationType(ModelSimple):
    """
    Annotation resource type.

    :param value: If omitted defaults to "annotation". Must be one of ["annotation"].
    :type value: str
    """

    allowed_values = {
        "annotation",
    }
    ANNOTATION: ClassVar["AnnotationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AnnotationType.ANNOTATION = AnnotationType("annotation")
