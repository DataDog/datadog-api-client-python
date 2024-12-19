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
    from datadog_api_client.v2.model.list_apps_response_data_items_attributes import ListAppsResponseDataItemsAttributes
    from datadog_api_client.v2.model.app_meta import AppMeta
    from datadog_api_client.v2.model.list_apps_response_data_items_relationships import (
        ListAppsResponseDataItemsRelationships,
    )
    from datadog_api_client.v2.model.list_apps_response_data_items_type import ListAppsResponseDataItemsType


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
        from datadog_api_client.v2.model.list_apps_response_data_items_type import ListAppsResponseDataItemsType

        return {
            "attributes": (ListAppsResponseDataItemsAttributes,),
            "id": (str,),
            "meta": (AppMeta,),
            "relationships": (ListAppsResponseDataItemsRelationships,),
            "type": (ListAppsResponseDataItemsType,),
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
        id: str,
        type: ListAppsResponseDataItemsType,
        meta: Union[AppMeta, UnsetType] = unset,
        relationships: Union[ListAppsResponseDataItemsRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``ListAppsResponseDataItems`` object.

        :param attributes: The definition of ``ListAppsResponseDataItemsAttributes`` object.
        :type attributes: ListAppsResponseDataItemsAttributes

        :param id: The ``items`` ``id``.
        :type id: str

        :param meta: The definition of ``AppMeta`` object.
        :type meta: AppMeta, optional

        :param relationships: The definition of ``ListAppsResponseDataItemsRelationships`` object.
        :type relationships: ListAppsResponseDataItemsRelationships, optional

        :param type: The definition of ``ListAppsResponseDataItemsType`` object.
        :type type: ListAppsResponseDataItemsType
        """
        if meta is not unset:
            kwargs["meta"] = meta
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
