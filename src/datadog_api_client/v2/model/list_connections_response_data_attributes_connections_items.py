# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.create_connection_request_data_attributes_fields_items import (
        CreateConnectionRequestDataAttributesFieldsItems,
    )
    from datadog_api_client.v2.model.list_connections_response_data_attributes_connections_items_join import (
        ListConnectionsResponseDataAttributesConnectionsItemsJoin,
    )


class ListConnectionsResponseDataAttributesConnectionsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_connection_request_data_attributes_fields_items import (
            CreateConnectionRequestDataAttributesFieldsItems,
        )
        from datadog_api_client.v2.model.list_connections_response_data_attributes_connections_items_join import (
            ListConnectionsResponseDataAttributesConnectionsItemsJoin,
        )

        return {
            "created_at": (datetime,),
            "created_by": (str,),
            "fields": ([CreateConnectionRequestDataAttributesFieldsItems],),
            "id": (str,),
            "join": (ListConnectionsResponseDataAttributesConnectionsItemsJoin,),
            "metadata": ({str: (str,)},),
            "type": (str,),
            "updated_at": (datetime,),
            "updated_by": (str,),
        }

    attribute_map = {
        "created_at": "created_at",
        "created_by": "created_by",
        "fields": "fields",
        "id": "id",
        "join": "join",
        "metadata": "metadata",
        "type": "type",
        "updated_at": "updated_at",
        "updated_by": "updated_by",
    }

    def __init__(
        self_,
        created_at: Union[datetime, UnsetType] = unset,
        created_by: Union[str, UnsetType] = unset,
        fields: Union[List[CreateConnectionRequestDataAttributesFieldsItems], UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        join: Union[ListConnectionsResponseDataAttributesConnectionsItemsJoin, UnsetType] = unset,
        metadata: Union[Dict[str, str], UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        updated_at: Union[datetime, UnsetType] = unset,
        updated_by: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param created_at:
        :type created_at: datetime, optional

        :param created_by:
        :type created_by: str, optional

        :param fields:
        :type fields: [CreateConnectionRequestDataAttributesFieldsItems], optional

        :param id:
        :type id: str, optional

        :param join:
        :type join: ListConnectionsResponseDataAttributesConnectionsItemsJoin, optional

        :param metadata:
        :type metadata: {str: (str,)}, optional

        :param type:
        :type type: str, optional

        :param updated_at:
        :type updated_at: datetime, optional

        :param updated_by:
        :type updated_by: str, optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if created_by is not unset:
            kwargs["created_by"] = created_by
        if fields is not unset:
            kwargs["fields"] = fields
        if id is not unset:
            kwargs["id"] = id
        if join is not unset:
            kwargs["join"] = join
        if metadata is not unset:
            kwargs["metadata"] = metadata
        if type is not unset:
            kwargs["type"] = type
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        if updated_by is not unset:
            kwargs["updated_by"] = updated_by
        super().__init__(kwargs)
