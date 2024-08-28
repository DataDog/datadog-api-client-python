# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class EntityMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (str,),
            "ingestion_source": (str,),
            "modified_at": (str,),
            "origin": (str,),
        }

    attribute_map = {
        "created_at": "createdAt",
        "ingestion_source": "ingestionSource",
        "modified_at": "modifiedAt",
        "origin": "origin",
    }

    def __init__(
        self_,
        created_at: Union[str, UnsetType] = unset,
        ingestion_source: Union[str, UnsetType] = unset,
        modified_at: Union[str, UnsetType] = unset,
        origin: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Entity metadata.

        :param created_at: The creation time.
        :type created_at: str, optional

        :param ingestion_source: The ingestion source.
        :type ingestion_source: str, optional

        :param modified_at: The modification time.
        :type modified_at: str, optional

        :param origin: The origin.
        :type origin: str, optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if ingestion_source is not unset:
            kwargs["ingestion_source"] = ingestion_source
        if modified_at is not unset:
            kwargs["modified_at"] = modified_at
        if origin is not unset:
            kwargs["origin"] = origin
        super().__init__(kwargs)
