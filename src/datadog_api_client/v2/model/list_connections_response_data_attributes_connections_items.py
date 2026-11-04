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
    from datadog_api_client.v2.model.list_connections_response_data_attributes_connections_items_details import (
        ListConnectionsResponseDataAttributesConnectionsItemsDetails,
    )
    from datadog_api_client.v2.model.create_connection_request_data_attributes_fields_items import (
        CreateConnectionRequestDataAttributesFieldsItems,
    )
    from datadog_api_client.v2.model.list_connections_response_data_attributes_connections_items_join import (
        ListConnectionsResponseDataAttributesConnectionsItemsJoin,
    )


class ListConnectionsResponseDataAttributesConnectionsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.list_connections_response_data_attributes_connections_items_details import (
            ListConnectionsResponseDataAttributesConnectionsItemsDetails,
        )
        from datadog_api_client.v2.model.create_connection_request_data_attributes_fields_items import (
            CreateConnectionRequestDataAttributesFieldsItems,
        )
        from datadog_api_client.v2.model.list_connections_response_data_attributes_connections_items_join import (
            ListConnectionsResponseDataAttributesConnectionsItemsJoin,
        )

        return {
            "created_at": (datetime,),
            "created_by": (str,),
            "details": (ListConnectionsResponseDataAttributesConnectionsItemsDetails,),
            "fields": ([CreateConnectionRequestDataAttributesFieldsItems],),
            "id": (str,),
            "join": (ListConnectionsResponseDataAttributesConnectionsItemsJoin,),
            "metadata": ({str: (str,)},),
            "name": (str,),
            "type": (str,),
            "updated_at": (datetime,),
            "updated_by": (str,),
        }

    attribute_map = {
        "created_at": "created_at",
        "created_by": "created_by",
        "details": "details",
        "fields": "fields",
        "id": "id",
        "join": "join",
        "metadata": "metadata",
        "name": "name",
        "type": "type",
        "updated_at": "updated_at",
        "updated_by": "updated_by",
    }

    def __init__(
        self_,
        created_at: Union[datetime, UnsetType] = unset,
        created_by: Union[str, UnsetType] = unset,
        details: Union[ListConnectionsResponseDataAttributesConnectionsItemsDetails, UnsetType] = unset,
        fields: Union[List[CreateConnectionRequestDataAttributesFieldsItems], UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        join: Union[ListConnectionsResponseDataAttributesConnectionsItemsJoin, UnsetType] = unset,
        metadata: Union[Dict[str, str], UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        updated_at: Union[datetime, UnsetType] = unset,
        updated_by: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Details of a single data source connection, including its fields, join configuration, and audit metadata.

        :param created_at: Timestamp indicating when the connection was created.
        :type created_at: datetime, optional

        :param created_by: Identifier of the user who created the connection.
        :type created_by: str, optional

        :param details: Type-specific configuration of the connection. Only the field matching the connection type is set.
        :type details: ListConnectionsResponseDataAttributesConnectionsItemsDetails, optional

        :param fields: List of custom attribute fields imported from the data source.
        :type fields: [CreateConnectionRequestDataAttributesFieldsItems], optional

        :param id: Unique identifier of the connection.
        :type id: str, optional

        :param join: The join configuration describing how the data source is linked to the entity.
        :type join: ListConnectionsResponseDataAttributesConnectionsItemsJoin, optional

        :param metadata: Additional key-value metadata associated with the connection.
        :type metadata: {str: (str,)}, optional

        :param name: Display name of the connection.
        :type name: str, optional

        :param type: The type of data source connection (for example, ref_table).
        :type type: str, optional

        :param updated_at: Timestamp indicating when the connection was last updated.
        :type updated_at: datetime, optional

        :param updated_by: Identifier of the user who last updated the connection.
        :type updated_by: str, optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if created_by is not unset:
            kwargs["created_by"] = created_by
        if details is not unset:
            kwargs["details"] = details
        if fields is not unset:
            kwargs["fields"] = fields
        if id is not unset:
            kwargs["id"] = id
        if join is not unset:
            kwargs["join"] = join
        if metadata is not unset:
            kwargs["metadata"] = metadata
        if name is not unset:
            kwargs["name"] = name
        if type is not unset:
            kwargs["type"] = type
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        if updated_by is not unset:
            kwargs["updated_by"] = updated_by
        super().__init__(kwargs)
