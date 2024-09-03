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


class EntityResponseIncludedRelatedEntityMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (datetime,),
            "defined_by": (str,),
            "modified_at": (datetime,),
            "source": (str,),
        }

    attribute_map = {
        "created_at": "createdAt",
        "defined_by": "defined_by",
        "modified_at": "modifiedAt",
        "source": "source",
    }

    def __init__(
        self_,
        created_at: Union[datetime, UnsetType] = unset,
        defined_by: Union[str, UnsetType] = unset,
        modified_at: Union[datetime, UnsetType] = unset,
        source: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Included related entity meta.

        :param created_at: Entity creation time.
        :type created_at: datetime, optional

        :param defined_by: Entity relation defined by.
        :type defined_by: str, optional

        :param modified_at: Entity modification time.
        :type modified_at: datetime, optional

        :param source: Entity relation source.
        :type source: str, optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if defined_by is not unset:
            kwargs["defined_by"] = defined_by
        if modified_at is not unset:
            kwargs["modified_at"] = modified_at
        if source is not unset:
            kwargs["source"] = source
        super().__init__(kwargs)
