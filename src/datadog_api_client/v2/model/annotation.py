# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.annotation_display import AnnotationDisplay
    from datadog_api_client.v2.model.annotation_markdown_text_annotation import AnnotationMarkdownTextAnnotation


class Annotation(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.annotation_display import AnnotationDisplay
        from datadog_api_client.v2.model.annotation_markdown_text_annotation import AnnotationMarkdownTextAnnotation

        return {
            "display": (AnnotationDisplay,),
            "id": (str,),
            "markdown_text_annotation": (AnnotationMarkdownTextAnnotation,),
        }

    attribute_map = {
        "display": "display",
        "id": "id",
        "markdown_text_annotation": "markdownTextAnnotation",
    }

    def __init__(
        self_, display: AnnotationDisplay, id: str, markdown_text_annotation: AnnotationMarkdownTextAnnotation, **kwargs
    ):
        """
        A list of annotations used in the workflow. These are like sticky notes for your workflow!

        :param display: The definition of ``AnnotationDisplay`` object.
        :type display: AnnotationDisplay

        :param id: The ``Annotation`` ``id``.
        :type id: str

        :param markdown_text_annotation: The definition of ``AnnotationMarkdownTextAnnotation`` object.
        :type markdown_text_annotation: AnnotationMarkdownTextAnnotation
        """
        super().__init__(kwargs)

        self_.display = display
        self_.id = id
        self_.markdown_text_annotation = markdown_text_annotation
