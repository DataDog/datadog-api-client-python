# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.widget_text_align import WidgetTextAlign
    from datadog_api_client.v1_20270101.model.widget_time import WidgetTime
    from datadog_api_client.v1_20270101.model.alert_value_definition_type import AlertValueDefinitionType
    from datadog_api_client.v1_20270101.model.widget_time20270101_one_of import WidgetTime20270101OneOf
    from datadog_api_client.v1_20270101.model.widget_time20270101_one_of4464103552 import (
        WidgetTime20270101OneOf4464103552,
    )
    from datadog_api_client.v1_20270101.model.widget_time20270101_one_of4464104512 import (
        WidgetTime20270101OneOf4464104512,
    )
    from datadog_api_client.v1_20270101.model.widget_time20270101_one_of4464105312 import (
        WidgetTime20270101OneOf4464105312,
    )
    from datadog_api_client.v1.model.widget_time20270101_one_of4464105952 import WidgetTime20270101OneOf4464105952


class AlertValueDefinition(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.widget_text_align import WidgetTextAlign
        from datadog_api_client.v1_20270101.model.widget_time import WidgetTime
        from datadog_api_client.v1_20270101.model.alert_value_definition_type import AlertValueDefinitionType

        return {
            "alert_id": (str,),
            "description": (str,),
            "notes": (str,),
            "precision": (float,),
            "text_align": (WidgetTextAlign,),
            "text_size": (str,),
            "time": (WidgetTime,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (AlertValueDefinitionType,),
            "unit": (str,),
        }

    attribute_map = {
        "alert_id": "alert_id",
        "description": "description",
        "notes": "notes",
        "precision": "precision",
        "text_align": "text_align",
        "text_size": "text_size",
        "time": "time",
        "title": "title",
        "title_align": "title_align",
        "title_size": "title_size",
        "type": "type",
        "unit": "unit",
    }

    def __init__(
        self_,
        alert_id: str,
        type: AlertValueDefinitionType,
        description: Union[str, UnsetType] = unset,
        notes: Union[str, UnsetType] = unset,
        precision: Union[float, UnsetType] = unset,
        text_align: Union[WidgetTextAlign, UnsetType] = unset,
        text_size: Union[str, UnsetType] = unset,
        time: Union[
            WidgetTime,
            WidgetTime20270101OneOf,
            WidgetTime20270101OneOf4464103552,
            WidgetTime20270101OneOf4464104512,
            WidgetTime20270101OneOf4464105312,
            WidgetTime20270101OneOf4464105952,
            EmptyObject,
            UnsetType,
        ] = unset,
        title: Union[str, UnsetType] = unset,
        title_align: Union[WidgetTextAlign, UnsetType] = unset,
        title_size: Union[str, UnsetType] = unset,
        unit: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param alert_id: Test-only generated schema for the dashboard versioning proof of concept.
        :type alert_id: str

        :param description: Test-only generated schema for the dashboard versioning proof of concept.
        :type description: str, optional

        :param notes: Test-only generated schema for the dashboard versioning proof of concept.
        :type notes: str, optional

        :param precision: Test-only generated schema for the dashboard versioning proof of concept.
        :type precision: float, optional

        :param text_align: Test-only generated schema for the dashboard versioning proof of concept.
        :type text_align: WidgetTextAlign, optional

        :param text_size: Test-only generated schema for the dashboard versioning proof of concept.
        :type text_size: str, optional

        :param time: Test-only generated schema for the dashboard versioning proof of concept.
        :type time: WidgetTime, optional

        :param title: Test-only generated schema for the dashboard versioning proof of concept.
        :type title: str, optional

        :param title_align: Test-only generated schema for the dashboard versioning proof of concept.
        :type title_align: WidgetTextAlign, optional

        :param title_size: Test-only generated schema for the dashboard versioning proof of concept.
        :type title_size: str, optional

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: AlertValueDefinitionType

        :param unit: Test-only generated schema for the dashboard versioning proof of concept.
        :type unit: str, optional
        """
        if description is not unset:
            kwargs["description"] = description
        if notes is not unset:
            kwargs["notes"] = notes
        if precision is not unset:
            kwargs["precision"] = precision
        if text_align is not unset:
            kwargs["text_align"] = text_align
        if text_size is not unset:
            kwargs["text_size"] = text_size
        if time is not unset:
            kwargs["time"] = time
        if title is not unset:
            kwargs["title"] = title
        if title_align is not unset:
            kwargs["title_align"] = title_align
        if title_size is not unset:
            kwargs["title_size"] = title_size
        if unit is not unset:
            kwargs["unit"] = unit
        super().__init__(kwargs)

        self_.alert_id = alert_id
        self_.type = type
