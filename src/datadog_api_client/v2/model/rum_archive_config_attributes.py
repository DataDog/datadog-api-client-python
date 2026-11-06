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


class RumArchiveConfigAttributes(ModelNormal):
    validations = {
        "retention_days": {
            "inclusive_maximum": 180,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "enabled": (bool,),
            "org_id": (int,),
            "retention_days": (int,),
            "updated_at": (datetime,),
            "updated_by": (str,),
        }

    attribute_map = {
        "enabled": "enabled",
        "org_id": "org_id",
        "retention_days": "retention_days",
        "updated_at": "updated_at",
        "updated_by": "updated_by",
    }

    def __init__(
        self_,
        enabled: bool,
        org_id: int,
        retention_days: Union[int, UnsetType] = unset,
        updated_at: Union[datetime, UnsetType] = unset,
        updated_by: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Archive configuration.

        :param enabled: Whether archiving is enabled.
        :type enabled: bool

        :param org_id: Organization ID.
        :type org_id: int

        :param retention_days: Configured retention in days; omitted when unset. When archiving is enabled, this is 30, 90, or 180.
        :type retention_days: int, optional

        :param updated_at: Last update time.
        :type updated_at: datetime, optional

        :param updated_by: Handle of the user who last updated the configuration.
        :type updated_by: str, optional
        """
        if retention_days is not unset:
            kwargs["retention_days"] = retention_days
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        if updated_by is not unset:
            kwargs["updated_by"] = updated_by
        super().__init__(kwargs)

        self_.enabled = enabled
        self_.org_id = org_id
