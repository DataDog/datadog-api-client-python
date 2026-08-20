# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class AnnotationMarkdownTextAnnotation(ModelNormal):
    validations = {
        "text": {
            "max_length": 3000,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "text": (str,),
        }

    attribute_map = {
        "text": "text",
    }

    def __init__(self_, text: Union[str, UnsetType] = unset, **kwargs):
        """
        Markdown content displayed in an annotation.

        :param text: The annotation's Markdown content.
        :type text: str, optional
        """
        if text is not unset:
            kwargs["text"] = text
        super().__init__(kwargs)
