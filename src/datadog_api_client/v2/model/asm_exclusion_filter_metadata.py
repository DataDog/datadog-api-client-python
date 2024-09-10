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


class ASMExclusionFilterMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "added_at": (datetime,),
            "added_by": (str,),
            "modified_at": (datetime,),
            "modified_by": (str,),
        }

    attribute_map = {
        "added_at": "added_at",
        "added_by": "added_by",
        "modified_at": "modified_at",
        "modified_by": "modified_by",
    }

    def __init__(
        self_,
        added_at: Union[datetime, UnsetType] = unset,
        added_by: Union[str, UnsetType] = unset,
        modified_at: Union[datetime, UnsetType] = unset,
        modified_by: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Metadata about the exclusion filter.

        :param added_at: The timestamp when the exclusion filter was added.
        :type added_at: datetime, optional

        :param added_by: The email address of the user who added the exclusion filter.
        :type added_by: str, optional

        :param modified_at: The timestamp when the exclusion filter was last modified.
        :type modified_at: datetime, optional

        :param modified_by: The email address of the user who last modified the exclusion filter.
        :type modified_by: str, optional
        """
        if added_at is not unset:
            kwargs["added_at"] = added_at
        if added_by is not unset:
            kwargs["added_by"] = added_by
        if modified_at is not unset:
            kwargs["modified_at"] = modified_at
        if modified_by is not unset:
            kwargs["modified_by"] = modified_by
        super().__init__(kwargs)
