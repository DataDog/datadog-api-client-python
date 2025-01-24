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
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.list_apps_response_data_items_attributes import ListAppsResponseDataItemsAttributes
    from datadog_api_client.v2.model.app_meta import AppMeta
    from datadog_api_client.v2.model.list_apps_response_data_items_relationships import (
        ListAppsResponseDataItemsRelationships,
    )
    from datadog_api_client.v2.model.app_definition_type import AppDefinitionType


class ListAppsResponseDataItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.list_apps_response_data_items_attributes import (
            ListAppsResponseDataItemsAttributes,
        )
        from datadog_api_client.v2.model.app_meta import AppMeta
        from datadog_api_client.v2.model.list_apps_response_data_items_relationships import (
            ListAppsResponseDataItemsRelationships,
        )
        from datadog_api_client.v2.model.app_definition_type import AppDefinitionType

        return {
            "attributes": (ListAppsResponseDataItemsAttributes,),
            "id": (UUID,),
            "meta": (AppMeta,),
            "relationships": (ListAppsResponseDataItemsRelationships,),
            "type": (AppDefinitionType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "meta": "meta",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ListAppsResponseDataItemsAttributes,
        id: UUID,
        type: AppDefinitionType,
        meta: Union[AppMeta, UnsetType] = unset,
        relationships: Union[ListAppsResponseDataItemsRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        An app definition object. This contains only basic information about the app such as ID, name, and tags.

        :param attributes: Basic information about the app such as name, description, and tags.
        :type attributes: ListAppsResponseDataItemsAttributes

        :param id: The ID of the app.
        :type id: UUID

        :param meta: Metadata of an app.
        :type meta: AppMeta, optional

        :param relationships: The app's publication information.
        :type relationships: ListAppsResponseDataItemsRelationships, optional

        :param type: The app definition type.
        :type type: AppDefinitionType
        """
        if meta is not unset:
            kwargs["meta"] = meta
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
