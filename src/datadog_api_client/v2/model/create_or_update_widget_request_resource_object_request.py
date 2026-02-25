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
    from datadog_api_client.v2.model.create_or_update_widget_request_attributes import (
        CreateOrUpdateWidgetRequestAttributes,
    )
    from datadog_api_client.v2.model.widget_links import WidgetLinks
    from datadog_api_client.v2.model.widget_relationship_object_input import WidgetRelationshipObjectInput


class CreateOrUpdateWidgetRequestResourceObjectRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_or_update_widget_request_attributes import (
            CreateOrUpdateWidgetRequestAttributes,
        )
        from datadog_api_client.v2.model.widget_links import WidgetLinks
        from datadog_api_client.v2.model.widget_relationship_object_input import WidgetRelationshipObjectInput

        return {
            "attributes": (CreateOrUpdateWidgetRequestAttributes,),
            "id": (str, none_type),
            "lid": (str, none_type),
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
            "relationships": ({str: (WidgetRelationshipObjectInput,)}, none_type),
            "type": (str,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "lid": "lid",
        "links": "links",
        "meta": "meta",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: CreateOrUpdateWidgetRequestAttributes,
        type: str,
        id: Union[str, none_type, UnsetType] = unset,
        lid: Union[str, none_type, UnsetType] = unset,
        links: Union[WidgetLinks, UnsetType] = unset,
        meta: Union[Dict[str, Any], none_type, UnsetType] = unset,
        relationships: Union[Dict[str, WidgetRelationshipObjectInput], none_type, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param attributes:
        :type attributes: CreateOrUpdateWidgetRequestAttributes

        :param id:
        :type id: str, none_type, optional

        :param lid:
        :type lid: str, none_type, optional

        :param links: A JSON:API "links" member
            See: https://jsonapi.org/format/#document-links
        :type links: WidgetLinks, optional

        :param meta:
        :type meta: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, none_type, optional

        :param relationships:
        :type relationships: {str: (WidgetRelationshipObjectInput,)}, none_type, optional

        :param type:
        :type type: str
        """
        if id is not unset:
            kwargs["id"] = id
        if lid is not unset:
            kwargs["lid"] = lid
        if links is not unset:
            kwargs["links"] = links
        if meta is not unset:
            kwargs["meta"] = meta
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
