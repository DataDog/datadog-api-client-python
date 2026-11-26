# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.widget_custom_link import WidgetCustomLink
    from datadog_api_client.v1_20270101.model.query_value_backend_request import QueryValueBackendRequest
    from datadog_api_client.v1_20270101.model.widget_text_align import WidgetTextAlign
    from datadog_api_client.v1_20270101.model.widget_time import WidgetTime
    from datadog_api_client.v1_20270101.model.timeseries_background import TimeseriesBackground
    from datadog_api_client.v1_20270101.model.query_value_backend_definition_type import QueryValueBackendDefinitionType
    from datadog_api_client.v1_20270101.model.context_menu_link import ContextMenuLink
    from datadog_api_client.v1_20270101.model.user_defined_link import UserDefinedLink
    from datadog_api_client.v1_20270101.model.query_value_backend_request20270101_one_of import (
        QueryValueBackendRequest20270101OneOf,
    )
    from datadog_api_client.v1_20270101.model.query_value_backend_request20270101_one_of4460683296 import (
        QueryValueBackendRequest20270101OneOf4460683296,
    )
    from datadog_api_client.v1_20270101.model.query_value_backend_request20270101_one_of4460685056 import (
        QueryValueBackendRequest20270101OneOf4460685056,
    )
    from datadog_api_client.v1_20270101.model.query_value_backend_request20270101_one_of4460686496 import (
        QueryValueBackendRequest20270101OneOf4460686496,
    )
    from datadog_api_client.v1_20270101.model.query_value_backend_request20270101_one_of4460688416 import (
        QueryValueBackendRequest20270101OneOf4460688416,
    )
    from datadog_api_client.v1_20270101.model.query_value_backend_request20270101_one_of4460689536 import (
        QueryValueBackendRequest20270101OneOf4460689536,
    )
    from datadog_api_client.v1_20270101.model.query_value_backend_request20270101_one_of4460690656 import (
        QueryValueBackendRequest20270101OneOf4460690656,
    )
    from datadog_api_client.v1_20270101.model.query_value_backend_request20270101_one_of4460904832 import (
        QueryValueBackendRequest20270101OneOf4460904832,
    )
    from datadog_api_client.v1_20270101.model.query_value_backend_request20270101_one_of4460905952 import (
        QueryValueBackendRequest20270101OneOf4460905952,
    )
    from datadog_api_client.v1_20270101.model.query_value_backend_request20270101_one_of4460907072 import (
        QueryValueBackendRequest20270101OneOf4460907072,
    )
    from datadog_api_client.v1_20270101.model.query_value_backend_request20270101_one_of4460908192 import (
        QueryValueBackendRequest20270101OneOf4460908192,
    )
    from datadog_api_client.v1_20270101.model.query_value_backend_request20270101_one_of4460909312 import (
        QueryValueBackendRequest20270101OneOf4460909312,
    )
    from datadog_api_client.v1_20270101.model.query_value_backend_request20270101_one_of4460910432 import (
        QueryValueBackendRequest20270101OneOf4460910432,
    )
    from datadog_api_client.v1_20270101.model.query_value_backend_request20270101_one_of4460911552 import (
        QueryValueBackendRequest20270101OneOf4460911552,
    )
    from datadog_api_client.v1_20270101.model.query_value_backend_request20270101_one_of4460912672 import (
        QueryValueBackendRequest20270101OneOf4460912672,
    )
    from datadog_api_client.v1_20270101.model.query_value_backend_request20270101_one_of4460913792 import (
        QueryValueBackendRequest20270101OneOf4460913792,
    )
    from datadog_api_client.v1_20270101.model.query_value_backend_request20270101_one_of4460914912 import (
        QueryValueBackendRequest20270101OneOf4460914912,
    )
    from datadog_api_client.v1_20270101.model.query_value_backend_request20270101_one_of4460916032 import (
        QueryValueBackendRequest20270101OneOf4460916032,
    )
    from datadog_api_client.v1_20270101.model.query_value_backend_request20270101_one_of4460917152 import (
        QueryValueBackendRequest20270101OneOf4460917152,
    )
    from datadog_api_client.v1_20270101.model.query_value_backend_request20270101_one_of4460918912 import (
        QueryValueBackendRequest20270101OneOf4460918912,
    )
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


class QueryValueBackendDefinition(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.widget_custom_link import WidgetCustomLink
        from datadog_api_client.v1_20270101.model.query_value_backend_request import QueryValueBackendRequest
        from datadog_api_client.v1_20270101.model.widget_text_align import WidgetTextAlign
        from datadog_api_client.v1_20270101.model.widget_time import WidgetTime
        from datadog_api_client.v1_20270101.model.timeseries_background import TimeseriesBackground
        from datadog_api_client.v1_20270101.model.query_value_backend_definition_type import (
            QueryValueBackendDefinitionType,
        )

        return {
            "autoscale": (bool,),
            "custom_links": ([WidgetCustomLink],),
            "custom_unit": (str,),
            "description": (str,),
            "notes": (str,),
            "precision": (float,),
            "requests": ([QueryValueBackendRequest],),
            "text_align": (WidgetTextAlign,),
            "time": (WidgetTime,),
            "timeseries_background": (TimeseriesBackground,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (QueryValueBackendDefinitionType,),
        }

    attribute_map = {
        "autoscale": "autoscale",
        "custom_links": "custom_links",
        "custom_unit": "custom_unit",
        "description": "description",
        "notes": "notes",
        "precision": "precision",
        "requests": "requests",
        "text_align": "text_align",
        "time": "time",
        "timeseries_background": "timeseries_background",
        "title": "title",
        "title_align": "title_align",
        "title_size": "title_size",
        "type": "type",
    }

    def __init__(
        self_,
        requests: List[
            Union[
                QueryValueBackendRequest,
                QueryValueBackendRequest20270101OneOf,
                QueryValueBackendRequest20270101OneOf4460683296,
                QueryValueBackendRequest20270101OneOf4460685056,
                QueryValueBackendRequest20270101OneOf4460686496,
                QueryValueBackendRequest20270101OneOf4460688416,
                QueryValueBackendRequest20270101OneOf4460689536,
                QueryValueBackendRequest20270101OneOf4460690656,
                QueryValueBackendRequest20270101OneOf4460904832,
                QueryValueBackendRequest20270101OneOf4460905952,
                QueryValueBackendRequest20270101OneOf4460907072,
                QueryValueBackendRequest20270101OneOf4460908192,
                QueryValueBackendRequest20270101OneOf4460909312,
                QueryValueBackendRequest20270101OneOf4460910432,
                QueryValueBackendRequest20270101OneOf4460911552,
                QueryValueBackendRequest20270101OneOf4460912672,
                QueryValueBackendRequest20270101OneOf4460913792,
                QueryValueBackendRequest20270101OneOf4460914912,
                QueryValueBackendRequest20270101OneOf4460916032,
                QueryValueBackendRequest20270101OneOf4460917152,
                QueryValueBackendRequest20270101OneOf4460918912,
            ]
        ],
        type: QueryValueBackendDefinitionType,
        autoscale: Union[bool, UnsetType] = unset,
        custom_links: Union[List[Union[WidgetCustomLink, ContextMenuLink, UserDefinedLink]], UnsetType] = unset,
        custom_unit: Union[str, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        notes: Union[str, UnsetType] = unset,
        precision: Union[float, UnsetType] = unset,
        text_align: Union[WidgetTextAlign, UnsetType] = unset,
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
        timeseries_background: Union[TimeseriesBackground, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        title_align: Union[WidgetTextAlign, UnsetType] = unset,
        title_size: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param autoscale: Test-only generated schema for the dashboard versioning proof of concept.
        :type autoscale: bool, optional

        :param custom_links: Test-only generated schema for the dashboard versioning proof of concept.
        :type custom_links: [WidgetCustomLink], optional

        :param custom_unit: Test-only generated schema for the dashboard versioning proof of concept.
        :type custom_unit: str, optional

        :param description: Test-only generated schema for the dashboard versioning proof of concept.
        :type description: str, optional

        :param notes: Test-only generated schema for the dashboard versioning proof of concept.
        :type notes: str, optional

        :param precision: Test-only generated schema for the dashboard versioning proof of concept.
        :type precision: float, optional

        :param requests: Test-only generated schema for the dashboard versioning proof of concept.
        :type requests: [QueryValueBackendRequest]

        :param text_align: Test-only generated schema for the dashboard versioning proof of concept.
        :type text_align: WidgetTextAlign, optional

        :param time: Test-only generated schema for the dashboard versioning proof of concept.
        :type time: WidgetTime, optional

        :param timeseries_background: Test-only generated schema for the dashboard versioning proof of concept.
        :type timeseries_background: TimeseriesBackground, optional

        :param title: Test-only generated schema for the dashboard versioning proof of concept.
        :type title: str, optional

        :param title_align: Test-only generated schema for the dashboard versioning proof of concept.
        :type title_align: WidgetTextAlign, optional

        :param title_size: Test-only generated schema for the dashboard versioning proof of concept.
        :type title_size: str, optional

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: QueryValueBackendDefinitionType
        """
        if autoscale is not unset:
            kwargs["autoscale"] = autoscale
        if custom_links is not unset:
            kwargs["custom_links"] = custom_links
        if custom_unit is not unset:
            kwargs["custom_unit"] = custom_unit
        if description is not unset:
            kwargs["description"] = description
        if notes is not unset:
            kwargs["notes"] = notes
        if precision is not unset:
            kwargs["precision"] = precision
        if text_align is not unset:
            kwargs["text_align"] = text_align
        if time is not unset:
            kwargs["time"] = time
        if timeseries_background is not unset:
            kwargs["timeseries_background"] = timeseries_background
        if title is not unset:
            kwargs["title"] = title
        if title_align is not unset:
            kwargs["title_align"] = title_align
        if title_size is not unset:
            kwargs["title_size"] = title_size
        super().__init__(kwargs)

        self_.requests = requests
        self_.type = type
