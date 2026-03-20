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
    UUID,
)


class Variant(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (datetime,),
            "id": (UUID,),
            "key": (str,),
            "name": (str,),
            "updated_at": (datetime,),
            "value": (str,),
        }

    attribute_map = {
        "created_at": "created_at",
        "id": "id",
        "key": "key",
        "name": "name",
        "updated_at": "updated_at",
        "value": "value",
    }

    def __init__(
        self_,
        id: UUID,
        key: str,
        name: str,
        value: str,
        created_at: Union[datetime, UnsetType] = unset,
        updated_at: Union[datetime, UnsetType] = unset,
        **kwargs,
    ):
        """
        A variant of a feature flag.

        :param created_at: The timestamp when the variant was created.
        :type created_at: datetime, optional

        :param id: The unique identifier of the variant.
        :type id: UUID

        :param key: The unique key of the variant.
        :type key: str

        :param name: The name of the variant.
        :type name: str

        :param updated_at: The timestamp when the variant was last updated.
        :type updated_at: datetime, optional

        :param value: The value of the variant as a string.
        :type value: str
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        super().__init__(kwargs)

        self_.id = id
        self_.key = key
        self_.name = name
        self_.value = value
