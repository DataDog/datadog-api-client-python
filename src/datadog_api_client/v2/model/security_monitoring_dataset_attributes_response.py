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
    from datadog_api_client.v2.model.security_monitoring_dataset_definition import SecurityMonitoringDatasetDefinition


class SecurityMonitoringDatasetAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_dataset_definition import (
            SecurityMonitoringDatasetDefinition,
        )

        return {
            "created_at": (datetime,),
            "created_by_handle": (str,),
            "created_by_name": (str,),
            "definition": (SecurityMonitoringDatasetDefinition,),
            "description": (str,),
            "modified_at": (datetime,),
            "name": (str,),
            "org_id": (int,),
            "updated_by_handle": (str,),
            "updated_by_name": (str,),
            "version": (int,),
        }

    attribute_map = {
        "created_at": "createdAt",
        "created_by_handle": "createdByHandle",
        "created_by_name": "createdByName",
        "definition": "definition",
        "description": "description",
        "modified_at": "modifiedAt",
        "name": "name",
        "org_id": "orgId",
        "updated_by_handle": "updatedByHandle",
        "updated_by_name": "updatedByName",
        "version": "version",
    }

    def __init__(
        self_,
        created_at: datetime,
        definition: SecurityMonitoringDatasetDefinition,
        description: str,
        name: str,
        org_id: int,
        version: int,
        created_by_handle: Union[str, UnsetType] = unset,
        created_by_name: Union[str, UnsetType] = unset,
        modified_at: Union[datetime, UnsetType] = unset,
        updated_by_handle: Union[str, UnsetType] = unset,
        updated_by_name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a security monitoring dataset.

        :param created_at: The creation timestamp of the dataset.
        :type created_at: datetime

        :param created_by_handle: The handle of the user who created the dataset.
        :type created_by_handle: str, optional

        :param created_by_name: The name of the user who created the dataset.
        :type created_by_name: str, optional

        :param definition: The definition of a dataset, including its data source, name, indexes, and columns.
        :type definition: SecurityMonitoringDatasetDefinition

        :param description: A description of the dataset.
        :type description: str

        :param modified_at: The last modification timestamp of the dataset.
        :type modified_at: datetime, optional

        :param name: The name of the dataset.
        :type name: str

        :param org_id: The organization ID.
        :type org_id: int

        :param updated_by_handle: The handle of the user who last updated the dataset.
        :type updated_by_handle: str, optional

        :param updated_by_name: The name of the user who last updated the dataset.
        :type updated_by_name: str, optional

        :param version: The version of the dataset.
        :type version: int
        """
        if created_by_handle is not unset:
            kwargs["created_by_handle"] = created_by_handle
        if created_by_name is not unset:
            kwargs["created_by_name"] = created_by_name
        if modified_at is not unset:
            kwargs["modified_at"] = modified_at
        if updated_by_handle is not unset:
            kwargs["updated_by_handle"] = updated_by_handle
        if updated_by_name is not unset:
            kwargs["updated_by_name"] = updated_by_name
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.definition = definition
        self_.description = description
        self_.name = name
        self_.org_id = org_id
        self_.version = version
