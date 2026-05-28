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
    from datadog_api_client.v2.model.page_annotations_attributes import PageAnnotationsAttributes
    from datadog_api_client.v2.model.page_annotations_type import PageAnnotationsType


class PageAnnotationsData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.page_annotations_attributes import PageAnnotationsAttributes
        from datadog_api_client.v2.model.page_annotations_type import PageAnnotationsType

        return {
            "attributes": (PageAnnotationsAttributes,),
            "id": (str,),
            "type": (PageAnnotationsType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: PageAnnotationsAttributes, id: str, type: PageAnnotationsType, **kwargs):
        """
        Annotations grouped by widget for a single page.

        :param attributes: Attributes of the annotations on a page.
        :type attributes: PageAnnotationsAttributes

        :param id: ID of the page, prefixed with the page type and joined by a colon
            (for example, ``dashboard:abc-def-xyz`` or ``notebook:1234567890`` ).
        :type id: str

        :param type: Page annotations resource type.
        :type type: PageAnnotationsType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
