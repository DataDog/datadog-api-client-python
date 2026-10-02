# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Union

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


class ExperimentsExposureSQLModelV2DTODataAttributesItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "column_name": (str,),
            "column_type": (str,),
            "description": (str,),
            "id": (str,),
            "migration_metadata": (
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
            ),
            "name": (str,),
            "pipeline_column_suffix": (str,),
        }

    attribute_map = {
        "column_name": "column_name",
        "column_type": "column_type",
        "description": "description",
        "id": "id",
        "migration_metadata": "migration_metadata",
        "name": "name",
        "pipeline_column_suffix": "pipeline_column_suffix",
    }

    def __init__(
        self_,
        column_name: Union[str, UnsetType] = unset,
        column_type: Union[str, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        migration_metadata: Union[Any, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        pipeline_column_suffix: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Property column available from the exposure SQL model.

        :param column_name: SQL result column that contains this property.
        :type column_name: str, optional

        :param column_type: Data type of the property column.
        :type column_type: str, optional

        :param description: Description of the exposure property.
        :type description: str, optional

        :param id: Identifier of the exposure property.
        :type id: str, optional

        :param migration_metadata: Metadata associated with migration of this resource.
        :type migration_metadata: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param name: Display name of the exposure property.
        :type name: str, optional

        :param pipeline_column_suffix: Suffix used for this property column in the analysis pipeline.
        :type pipeline_column_suffix: str, optional
        """
        if column_name is not unset:
            kwargs["column_name"] = column_name
        if column_type is not unset:
            kwargs["column_type"] = column_type
        if description is not unset:
            kwargs["description"] = description
        if id is not unset:
            kwargs["id"] = id
        if migration_metadata is not unset:
            kwargs["migration_metadata"] = migration_metadata
        if name is not unset:
            kwargs["name"] = name
        if pipeline_column_suffix is not unset:
            kwargs["pipeline_column_suffix"] = pipeline_column_suffix
        super().__init__(kwargs)
