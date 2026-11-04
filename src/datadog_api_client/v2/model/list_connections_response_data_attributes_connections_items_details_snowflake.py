# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class ListConnectionsResponseDataAttributesConnectionsItemsDetailsSnowflake(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "account_id": (str,),
            "database_name": (str,),
            "schema": (str,),
            "table_name": (str,),
        }

    attribute_map = {
        "account_id": "account_id",
        "database_name": "database_name",
        "schema": "schema",
        "table_name": "table_name",
    }

    def __init__(
        self_,
        account_id: Union[str, UnsetType] = unset,
        database_name: Union[str, UnsetType] = unset,
        schema: Union[str, UnsetType] = unset,
        table_name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Configuration of a Snowflake connection.

        :param account_id: Identifier of the Snowflake account.
        :type account_id: str, optional

        :param database_name: Name of the Snowflake database.
        :type database_name: str, optional

        :param schema: Name of the Snowflake schema.
        :type schema: str, optional

        :param table_name: Name of the Snowflake table.
        :type table_name: str, optional
        """
        if account_id is not unset:
            kwargs["account_id"] = account_id
        if database_name is not unset:
            kwargs["database_name"] = database_name
        if schema is not unset:
            kwargs["schema"] = schema
        if table_name is not unset:
            kwargs["table_name"] = table_name
        super().__init__(kwargs)
