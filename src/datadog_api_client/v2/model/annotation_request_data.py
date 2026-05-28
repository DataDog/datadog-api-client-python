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
    from datadog_api_client.v2.model.annotation_create_attributes import AnnotationCreateAttributes
    from datadog_api_client.v2.model.annotation_type import AnnotationType


class AnnotationRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.annotation_create_attributes import AnnotationCreateAttributes
        from datadog_api_client.v2.model.annotation_type import AnnotationType

        return {
            "attributes": (AnnotationCreateAttributes,),
            "type": (AnnotationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: AnnotationCreateAttributes, type: AnnotationType, **kwargs):
        """
        Data for creating an annotation.

        :param attributes: Attributes for creating or updating an annotation.
        :type attributes: AnnotationCreateAttributes

        :param type: Annotation resource type.
        :type type: AnnotationType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
