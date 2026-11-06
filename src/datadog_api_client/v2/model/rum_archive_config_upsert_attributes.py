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


class RumArchiveConfigUpsertAttributes(ModelNormal):
    validations = {
        "retention_days": {
            "inclusive_maximum": 180,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "enabled": (bool,),
            "retention_days": (int,),
        }

    attribute_map = {
        "enabled": "enabled",
        "retention_days": "retention_days",
    }

    def __init__(self_, enabled: bool, retention_days: Union[int, UnsetType] = unset, **kwargs):
        """
        Archive configuration to save. When enabled is true, retention_days is required and must be 30, 90, or 180. When disabled, retention_days can be omitted.

        :param enabled: Whether archiving is enabled.
        :type enabled: bool

        :param retention_days: Retention in days. When enabled is true, required and restricted to 30, 90, or 180. When enabled is false, this field can be omitted.
        :type retention_days: int, optional
        """
        if retention_days is not unset:
            kwargs["retention_days"] = retention_days
        super().__init__(kwargs)

        self_.enabled = enabled
