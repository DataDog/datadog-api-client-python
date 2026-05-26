# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_monitoring_dataset_definition import SecurityMonitoringDatasetDefinition


class SecurityMonitoringDatasetAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_dataset_definition import (
            SecurityMonitoringDatasetDefinition,
        )

        return {
            "created_at": (str,),
            "created_by_handle": (str,),
            "created_by_name": (str,),
            "definition": (SecurityMonitoringDatasetDefinition,),
            "description": (str,),
            "id": (str,),
            "is_default": (bool,),
            "is_deprecated": (bool,),
            "modified_at": (str,),
            "name": (str,),
            "updated_by_handle": (str, none_type),
            "updated_by_name": (str, none_type),
            "version": (int,),
        }

    attribute_map = {
        "created_at": "createdAt",
        "created_by_handle": "createdByHandle",
        "created_by_name": "createdByName",
        "definition": "definition",
        "description": "description",
        "id": "id",
        "is_default": "isDefault",
        "is_deprecated": "isDeprecated",
        "modified_at": "modifiedAt",
        "name": "name",
        "updated_by_handle": "updatedByHandle",
        "updated_by_name": "updatedByName",
        "version": "version",
    }

    def __init__(
        self_,
        created_at: str,
        created_by_handle: str,
        created_by_name: str,
        definition: SecurityMonitoringDatasetDefinition,
        description: str,
        id: str,
        is_default: bool,
        is_deprecated: bool,
        modified_at: str,
        name: str,
        updated_by_handle: Union[str, none_type],
        updated_by_name: Union[str, none_type],
        version: int,
        **kwargs,
    ):
        """
        The attributes of a Cloud SIEM dataset.

        :param created_at: The creation timestamp of the dataset, in ISO 8601 format.
        :type created_at: str

        :param created_by_handle: The Datadog handle of the user who created the dataset.
        :type created_by_handle: str

        :param created_by_name: The display name of the user who created the dataset.
        :type created_by_name: str

        :param definition: The definition of the dataset. The shape depends on the value of ``data_source``.
            Use ``reference_table`` or ``managed_resource`` for a referential dataset, or one of the
            event platform sources (for example ``logs`` , ``audit`` , ``events`` , ``spans`` , ``rum`` ) for
            an event platform dataset.
        :type definition: SecurityMonitoringDatasetDefinition

        :param description: The description of the dataset.
        :type description: str

        :param id: The UUID of the dataset.
        :type id: str

        :param is_default: Whether the dataset is an out-of-the-box dataset provided by Datadog.
        :type is_default: bool

        :param is_deprecated: Whether the dataset is marked as deprecated.
        :type is_deprecated: bool

        :param modified_at: The timestamp of the last modification of the dataset, in ISO 8601 format.
        :type modified_at: str

        :param name: The unique name of the dataset.
        :type name: str

        :param updated_by_handle: The Datadog handle of the user who last updated the dataset.
        :type updated_by_handle: str, none_type

        :param updated_by_name: The display name of the user who last updated the dataset.
        :type updated_by_name: str, none_type

        :param version: The current version of the dataset.
        :type version: int
        """
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.created_by_handle = created_by_handle
        self_.created_by_name = created_by_name
        self_.definition = definition
        self_.description = description
        self_.id = id
        self_.is_default = is_default
        self_.is_deprecated = is_deprecated
        self_.modified_at = modified_at
        self_.name = name
        self_.updated_by_handle = updated_by_handle
        self_.updated_by_name = updated_by_name
        self_.version = version
