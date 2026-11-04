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
    from datadog_api_client.v2.model.list_connections_response_data_attributes_connections_items_details_ref_table import (
        ListConnectionsResponseDataAttributesConnectionsItemsDetailsRefTable,
    )
    from datadog_api_client.v2.model.list_connections_response_data_attributes_connections_items_details_snowflake import (
        ListConnectionsResponseDataAttributesConnectionsItemsDetailsSnowflake,
    )


class ListConnectionsResponseDataAttributesConnectionsItemsDetails(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.list_connections_response_data_attributes_connections_items_details_ref_table import (
            ListConnectionsResponseDataAttributesConnectionsItemsDetailsRefTable,
        )
        from datadog_api_client.v2.model.list_connections_response_data_attributes_connections_items_details_snowflake import (
            ListConnectionsResponseDataAttributesConnectionsItemsDetailsSnowflake,
        )

        return {
            "ref_table": (ListConnectionsResponseDataAttributesConnectionsItemsDetailsRefTable,),
            "snowflake": (ListConnectionsResponseDataAttributesConnectionsItemsDetailsSnowflake,),
        }

    attribute_map = {
        "ref_table": "ref_table",
        "snowflake": "snowflake",
    }

    def __init__(
        self_,
        ref_table: Union[ListConnectionsResponseDataAttributesConnectionsItemsDetailsRefTable, UnsetType] = unset,
        snowflake: Union[ListConnectionsResponseDataAttributesConnectionsItemsDetailsSnowflake, UnsetType] = unset,
        **kwargs,
    ):
        """
        Type-specific configuration of the connection. Only the field matching the connection type is set.

        :param ref_table: Configuration of a reference table connection.
        :type ref_table: ListConnectionsResponseDataAttributesConnectionsItemsDetailsRefTable, optional

        :param snowflake: Configuration of a Snowflake connection.
        :type snowflake: ListConnectionsResponseDataAttributesConnectionsItemsDetailsSnowflake, optional
        """
        if ref_table is not unset:
            kwargs["ref_table"] = ref_table
        if snowflake is not unset:
            kwargs["snowflake"] = snowflake
        super().__init__(kwargs)
