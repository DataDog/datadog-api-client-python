# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union, TYPE_CHECKING

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
    from datadog_api_client.v2.model.resource_object_output_attributes import ResourceObjectOutputAttributes
    from datadog_api_client.v2.model.widget_links import WidgetLinks
    from datadog_api_client.v2.model.widget_relationship_object_output import WidgetRelationshipObjectOutput
    from datadog_api_client.v2.model.resource_object_output_attributes_one_of import ResourceObjectOutputAttributesOneOf
    from datadog_api_client.v2.model.jsonapi_attributes import JSONAPIAttributes


class WidgetResourceObjectOutput(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.resource_object_output_attributes import ResourceObjectOutputAttributes
        from datadog_api_client.v2.model.widget_links import WidgetLinks
        from datadog_api_client.v2.model.widget_relationship_object_output import WidgetRelationshipObjectOutput

        return {
            "attributes": (ResourceObjectOutputAttributes,),
            "id": (str,),
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
            "relationships": ({str: (WidgetRelationshipObjectOutput,)}, none_type),
            "type": (str,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "links": "links",
        "meta": "meta",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        type: str,
        attributes: Union[
            Union[ResourceObjectOutputAttributes, ResourceObjectOutputAttributesOneOf, JSONAPIAttributes],
            none_type,
            UnsetType,
        ] = unset,
        links: Union[WidgetLinks, UnsetType] = unset,
        meta: Union[Dict[str, Any], none_type, UnsetType] = unset,
        relationships: Union[Dict[str, WidgetRelationshipObjectOutput], none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        A JSON:API resource object.
        See: https://jsonapi.org/format/#document-resource-objects

        :param attributes:
        :type attributes: ResourceObjectOutputAttributes, none_type, optional

        :param id:
        :type id: str

        :param links: A JSON:API "links" member
            See: https://jsonapi.org/format/#document-links
        :type links: WidgetLinks, optional

        :param meta:
        :type meta: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, none_type, optional

        :param relationships:
        :type relationships: {str: (WidgetRelationshipObjectOutput,)}, none_type, optional

        :param type:
        :type type: str
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if links is not unset:
            kwargs["links"] = links
        if meta is not unset:
            kwargs["meta"] = meta
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
