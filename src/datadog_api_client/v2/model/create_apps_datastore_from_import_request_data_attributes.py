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
    from datadog_api_client.v2.model.create_apps_datastore_from_import_request_data_attributes_primary_key_generation_strategy import (
        CreateAppsDatastoreFromImportRequestDataAttributesPrimaryKeyGenerationStrategy,
    )


class CreateAppsDatastoreFromImportRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_apps_datastore_from_import_request_data_attributes_primary_key_generation_strategy import (
            CreateAppsDatastoreFromImportRequestDataAttributesPrimaryKeyGenerationStrategy,
        )

        return {
            "description": (str,),
            "name": (str,),
            "org_access": (str,),
            "primary_column_name": (str,),
            "primary_key_generation_strategy": (
                CreateAppsDatastoreFromImportRequestDataAttributesPrimaryKeyGenerationStrategy,
            ),
            "values": (
                [
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
                    }
                ],
            ),
        }

    attribute_map = {
        "description": "description",
        "name": "name",
        "org_access": "org_access",
        "primary_column_name": "primary_column_name",
        "primary_key_generation_strategy": "primary_key_generation_strategy",
        "values": "values",
    }

    def __init__(
        self_,
        name: str,
        primary_column_name: str,
        values: List[Dict[str, Any]],
        description: Union[str, UnsetType] = unset,
        org_access: Union[str, UnsetType] = unset,
        primary_key_generation_strategy: Union[
            CreateAppsDatastoreFromImportRequestDataAttributesPrimaryKeyGenerationStrategy, UnsetType
        ] = unset,
        **kwargs,
    ):
        """
        The definition of ``CreateAppsDatastoreFromImportRequestDataAttributes`` object.

        :param description: The ``attributes`` ``description``.
        :type description: str, optional

        :param name: The ``attributes`` ``name``.
        :type name: str

        :param org_access: The ``attributes`` ``org_access``.
        :type org_access: str, optional

        :param primary_column_name: The ``attributes`` ``primary_column_name``.
        :type primary_column_name: str

        :param primary_key_generation_strategy: The ``attributes`` ``primary_key_generation_strategy``.
        :type primary_key_generation_strategy: CreateAppsDatastoreFromImportRequestDataAttributesPrimaryKeyGenerationStrategy, optional

        :param values: The ``attributes`` ``values``.
        :type values: [{str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}]
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
        self_.values = values
