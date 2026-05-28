# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.annotation_color import AnnotationColor
    from datadog_api_client.v2.model.annotation_kind import AnnotationKind


class AnnotationCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.annotation_color import AnnotationColor
        from datadog_api_client.v2.model.annotation_kind import AnnotationKind

        return {
            "color": (AnnotationColor,),
            "description": (str,),
            "end_time": (int, none_type),
            "page_id": (str,),
            "start_time": (int,),
            "type": (AnnotationKind,),
            "widget_ids": ([str],),
        }

    attribute_map = {
        "color": "color",
        "description": "description",
        "end_time": "end_time",
        "page_id": "page_id",
        "start_time": "start_time",
        "type": "type",
        "widget_ids": "widget_ids",
    }

    def __init__(
        self_,
        color: AnnotationColor,
        description: str,
        page_id: str,
        start_time: int,
        type: AnnotationKind,
        end_time: Union[int, none_type, UnsetType] = unset,
        widget_ids: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating or updating an annotation.

        :param color: Color used to render the annotation in the UI.
        :type color: AnnotationColor

        :param description: User-defined text attached to the annotation.
        :type description: str

        :param end_time: End time of the annotation in milliseconds since the Unix epoch. Required for ``timeRegion`` annotations; omit or set to null for ``pointInTime`` annotations.
        :type end_time: int, none_type, optional

        :param page_id: ID of the page the annotation belongs to, prefixed with the page type and joined by a colon
            (for example, ``dashboard:abc-def-xyz`` or ``notebook:1234567890`` ).
        :type page_id: str

        :param start_time: Start time of the annotation in milliseconds since the Unix epoch.
        :type start_time: int

        :param type: Kind of annotation. ``pointInTime`` annotations mark a single moment in time,
            while ``timeRegion`` annotations span a window of time and require an ``end_time``.
        :type type: AnnotationKind

        :param widget_ids: IDs of widgets the annotation is associated with. When empty or omitted, the annotation applies to the whole page.
        :type widget_ids: [str], optional
        """
        if end_time is not unset:
            kwargs["end_time"] = end_time
        if widget_ids is not unset:
            kwargs["widget_ids"] = widget_ids
        super().__init__(kwargs)

        self_.color = color
        self_.description = description
        self_.page_id = page_id
        self_.start_time = start_time
        self_.type = type
