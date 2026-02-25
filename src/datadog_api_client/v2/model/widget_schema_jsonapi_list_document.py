# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.widget_schema_resource import WidgetSchemaResource
    from datadog_api_client.v2.model.widget_error_input import WidgetErrorInput
    from datadog_api_client.v2.model.widget_resource_object_output import WidgetResourceObjectOutput
    from datadog_api_client.v2.model.widget_links import WidgetLinks


class WidgetSchemaJSONAPIListDocument(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.widget_schema_resource import WidgetSchemaResource
        from datadog_api_client.v2.model.widget_error_input import WidgetErrorInput
        from datadog_api_client.v2.model.widget_resource_object_output import WidgetResourceObjectOutput
        from datadog_api_client.v2.model.widget_links import WidgetLinks

        return {
            "data": ([WidgetSchemaResource],),
            "errors": ([WidgetErrorInput], none_type),
            "included": ([WidgetResourceObjectOutput], none_type),
            "links": (WidgetLinks,),
            "meta": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
                none_type,
            ),
        }

    attribute_map = {
        "data": "data",
        "errors": "errors",
        "included": "included",
        "links": "links",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: List[WidgetSchemaResource],
        errors: Union[List[WidgetErrorInput], none_type, UnsetType] = unset,
        included: Union[List[WidgetResourceObjectOutput], none_type, UnsetType] = unset,
        links: Union[WidgetLinks, UnsetType] = unset,
        meta: Union[Dict[str, Any], none_type, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param data:
        :type data: [WidgetSchemaResource]

        :param errors:
        :type errors: [WidgetErrorInput], none_type, optional

        :param included:
        :type included: [WidgetResourceObjectOutput], none_type, optional

        :param links: A JSON:API "links" member
            See: https://jsonapi.org/format/#document-links
        :type links: WidgetLinks, optional

        :param meta:
        :type meta: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, none_type, optional
        """
        if errors is not unset:
            kwargs["errors"] = errors
        if included is not unset:
            kwargs["included"] = included
        if links is not unset:
            kwargs["links"] = links
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data
