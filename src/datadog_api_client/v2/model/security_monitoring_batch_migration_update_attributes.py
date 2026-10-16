# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class SecurityMonitoringBatchMigrationUpdateAttributes(ModelNormal):
    validations = {
        "description": {
            "max_length": 4096,
        },
        "name": {
            "max_length": 512,
        },
        "tags": {
            "max_items": 50,
        },
    }

    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "description": (str,),
            "name": (str,),
            "tags": ([str],),
        }

    attribute_map = {
        "description": "description",
        "name": "name",
        "tags": "tags",
    }

    def __init__(
        self_,
        description: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of the batch migration to update. At least one attribute is required.

        :param description: The description of the batch migration.
        :type description: str, optional

        :param name: The name of the batch migration.
        :type name: str, optional

        :param tags: Tags of the batch migration. Up to 50 tags, each up to 256 characters.
        :type tags: [str], optional
        """
        if description is not unset:
            kwargs["description"] = description
        if name is not unset:
            kwargs["name"] = name
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)
