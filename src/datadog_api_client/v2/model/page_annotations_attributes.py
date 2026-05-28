# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.annotations_in_page_map import AnnotationsInPageMap
    from datadog_api_client.v2.model.widget_annotations_map import WidgetAnnotationsMap


class PageAnnotationsAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.annotations_in_page_map import AnnotationsInPageMap
        from datadog_api_client.v2.model.widget_annotations_map import WidgetAnnotationsMap

        return {
            "annotations": (AnnotationsInPageMap,),
            "global_annotations": ([UUID],),
            "widget_mapping": (WidgetAnnotationsMap,),
        }

    attribute_map = {
        "annotations": "annotations",
        "global_annotations": "global_annotations",
        "widget_mapping": "widget_mapping",
    }

    def __init__(
        self_,
        annotations: AnnotationsInPageMap,
        global_annotations: List[UUID],
        widget_mapping: WidgetAnnotationsMap,
        **kwargs,
    ):
        """
        Attributes of the annotations on a page.

        :param annotations: Map of annotation UUID to annotation object, keyed by annotation ID.
        :type annotations: AnnotationsInPageMap

        :param global_annotations: List of annotation IDs that apply to the entire page rather than a specific widget.
        :type global_annotations: [UUID]

        :param widget_mapping: Map from widget ID to the list of annotation IDs displayed on that widget.
        :type widget_mapping: WidgetAnnotationsMap
        """
        super().__init__(kwargs)

        self_.annotations = annotations
        self_.global_annotations = global_annotations
        self_.widget_mapping = widget_mapping
