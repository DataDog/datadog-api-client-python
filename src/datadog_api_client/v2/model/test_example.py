# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


class TestExample(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (datetime,),
            "id": (str,),
            "name": (str,),
        }

    attribute_map = {
        "created_at": "created_at",
        "id": "id",
        "name": "name",
    }
    read_only_vars = {
        "created_at",
    }

    def __init__(self_, id: str, name: str, created_at: Union[datetime, UnsetType] = unset, **kwargs):
        """
        A test example resource.

        :param created_at: Creation time of the test example.
        :type created_at: datetime, optional

        :param id: The ID of the test example.
        :type id: str

        :param name: The name of the test example.
        :type name: str
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        super().__init__(kwargs)

        self_.id = id
        self_.name = name
