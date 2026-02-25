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
    from datadog_api_client.v2.model.relationship_object_output_data import RelationshipObjectOutputData
    from datadog_api_client.v2.model.widget_links import WidgetLinks
    from datadog_api_client.v2.model.resource_identifier_object import ResourceIdentifierObject


class WidgetRelationshipObjectInput(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.relationship_object_output_data import RelationshipObjectOutputData
        from datadog_api_client.v2.model.widget_links import WidgetLinks

        return {
            "data": (RelationshipObjectOutputData,),
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
        "links": "links",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[
            Union[RelationshipObjectOutputData, ResourceIdentifierObject, List[ResourceIdentifierObject]],
            none_type,
            UnsetType,
        ] = unset,
        links: Union[WidgetLinks, UnsetType] = unset,
        meta: Union[Dict[str, Any], none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        A JSON:API "relationship object".
        See: https://jsonapi.org/format/#document-resource-object-relationships

        (When including relationships in models, you probably want Relationship, not this.)

        :param data:
        :type data: RelationshipObjectOutputData, none_type, optional

        :param links: A JSON:API "links" member
            See: https://jsonapi.org/format/#document-links
        :type links: WidgetLinks, optional

        :param meta:
        :type meta: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, none_type, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if links is not unset:
            kwargs["links"] = links
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
