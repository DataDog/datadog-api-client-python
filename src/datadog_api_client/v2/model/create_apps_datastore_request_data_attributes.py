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
    from datadog_api_client.v2.model.create_apps_datastore_request_data_attributes_org_access import (
        CreateAppsDatastoreRequestDataAttributesOrgAccess,
    )
    from datadog_api_client.v2.model.datastore_primary_key_generation_strategy import (
        DatastorePrimaryKeyGenerationStrategy,
    )


class CreateAppsDatastoreRequestDataAttributes(ModelNormal):
    validations = {
        "primary_column_name": {
            "max_length": 63,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_apps_datastore_request_data_attributes_org_access import (
            CreateAppsDatastoreRequestDataAttributesOrgAccess,
        )
        from datadog_api_client.v2.model.datastore_primary_key_generation_strategy import (
            DatastorePrimaryKeyGenerationStrategy,
        )

        return {
            "description": (str,),
            "name": (str,),
            "org_access": (CreateAppsDatastoreRequestDataAttributesOrgAccess,),
            "primary_column_name": (str,),
            "primary_key_generation_strategy": (DatastorePrimaryKeyGenerationStrategy,),
        }

    attribute_map = {
        "description": "description",
        "name": "name",
        "org_access": "org_access",
        "primary_column_name": "primary_column_name",
        "primary_key_generation_strategy": "primary_key_generation_strategy",
    }

    def __init__(
        self_,
        name: str,
        primary_column_name: str,
        description: Union[str, UnsetType] = unset,
        org_access: Union[CreateAppsDatastoreRequestDataAttributesOrgAccess, UnsetType] = unset,
        primary_key_generation_strategy: Union[DatastorePrimaryKeyGenerationStrategy, UnsetType] = unset,
        **kwargs,
    ):
        """
        Configuration and metadata to create a new datastore.

        :param description: A human-readable description about the datastore.
        :type description: str, optional

        :param name: The display name for the new datastore.
        :type name: str

        :param org_access: The organization access level for the datastore. For example, 'contributor'.
        :type org_access: CreateAppsDatastoreRequestDataAttributesOrgAccess, optional

        :param primary_column_name: The name of the primary key column for this datastore. Primary column names:

            * Must abide by both `PostgreSQL naming conventions <https://www.postgresql.org/docs/7.0/syntax525.htm>`_
            * Cannot exceed 63 characters
        :type primary_column_name: str

        :param primary_key_generation_strategy: Can be set to ``uuid`` to automatically generate primary keys when new items are added. Default value is ``none`` , which requires you to supply a primary key for each new item.
        :type primary_key_generation_strategy: DatastorePrimaryKeyGenerationStrategy, optional
        """
        if description is not unset:
            kwargs["description"] = description
        if org_access is not unset:
            kwargs["org_access"] = org_access
        if primary_key_generation_strategy is not unset:
            kwargs["primary_key_generation_strategy"] = primary_key_generation_strategy
        super().__init__(kwargs)

        self_.name = name
        self_.primary_column_name = primary_column_name
