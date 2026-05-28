# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.annotation_attributes import AnnotationAttributes
    from datadog_api_client.v2.model.annotation_type import AnnotationType


class AnnotationData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.annotation_attributes import AnnotationAttributes
        from datadog_api_client.v2.model.annotation_type import AnnotationType

        return {
            "attributes": (AnnotationAttributes,),
            "id": (UUID,),
            "type": (AnnotationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: AnnotationAttributes, id: UUID, type: AnnotationType, **kwargs):
        """
        A single annotation resource.

        :param attributes: Attributes of an annotation returned in a response.
        :type attributes: AnnotationAttributes

        :param id: Unique identifier of the annotation.
        :type id: UUID

        :param type: Annotation resource type.
        :type type: AnnotationType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
