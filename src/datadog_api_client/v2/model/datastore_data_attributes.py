# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.datastore_primary_key_generation_strategy import (
        DatastorePrimaryKeyGenerationStrategy,
    )


class DatastoreDataAttributes(ModelNormal):
    validations = {
        "primary_column_name": {
            "max_length": 63,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.datastore_primary_key_generation_strategy import (
            DatastorePrimaryKeyGenerationStrategy,
        )

        return {
            "created_at": (datetime,),
            "creator_user_id": (int,),
            "creator_user_uuid": (str,),
            "description": (str,),
            "modified_at": (datetime,),
            "name": (str,),
            "org_id": (int,),
            "primary_column_name": (str,),
            "primary_key_generation_strategy": (DatastorePrimaryKeyGenerationStrategy,),
        }

    attribute_map = {
        "created_at": "created_at",
        "creator_user_id": "creator_user_id",
        "creator_user_uuid": "creator_user_uuid",
        "description": "description",
        "modified_at": "modified_at",
        "name": "name",
        "org_id": "org_id",
        "primary_column_name": "primary_column_name",
        "primary_key_generation_strategy": "primary_key_generation_strategy",
    }

    def __init__(
        self_,
        created_at: Union[datetime, UnsetType] = unset,
        creator_user_id: Union[int, UnsetType] = unset,
        creator_user_uuid: Union[str, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        modified_at: Union[datetime, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        org_id: Union[int, UnsetType] = unset,
        primary_column_name: Union[str, UnsetType] = unset,
        primary_key_generation_strategy: Union[DatastorePrimaryKeyGenerationStrategy, UnsetType] = unset,
        **kwargs,
    ):
        """
        Detailed information about a datastore.

        :param created_at: Timestamp when the datastore was created.
        :type created_at: datetime, optional

        :param creator_user_id: The numeric ID of the user who created the datastore.
        :type creator_user_id: int, optional

        :param creator_user_uuid: The UUID of the user who created the datastore.
        :type creator_user_uuid: str, optional

        :param description: A human-readable description about the datastore.
        :type description: str, optional

        :param modified_at: Timestamp when the datastore was last modified.
        :type modified_at: datetime, optional

        :param name: The display name of the datastore.
        :type name: str, optional

        :param org_id: The ID of the organization that owns this datastore.
        :type org_id: int, optional

        :param primary_column_name: The name of the primary key column for this datastore. Primary column names:

            * Must abide by both `PostgreSQL naming conventions <https://www.postgresql.org/docs/7.0/syntax525.htm>`_
            * Cannot exceed 63 characters
        :type primary_column_name: str, optional

        :param primary_key_generation_strategy: Can be set to ``uuid`` to automatically generate primary keys when new items are added. Default value is ``none`` , which requires you to supply a primary key for each new item.
        :type primary_key_generation_strategy: DatastorePrimaryKeyGenerationStrategy, optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if creator_user_id is not unset:
            kwargs["creator_user_id"] = creator_user_id
        if creator_user_uuid is not unset:
            kwargs["creator_user_uuid"] = creator_user_uuid
        if description is not unset:
            kwargs["description"] = description
        if modified_at is not unset:
            kwargs["modified_at"] = modified_at
        if name is not unset:
            kwargs["name"] = name
        if org_id is not unset:
            kwargs["org_id"] = org_id
        if primary_column_name is not unset:
            kwargs["primary_column_name"] = primary_column_name
        if primary_key_generation_strategy is not unset:
            kwargs["primary_key_generation_strategy"] = primary_key_generation_strategy
        super().__init__(kwargs)
