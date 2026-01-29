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


class SyncProperty(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "sync_type": (str,),
        }

    attribute_map = {
        "sync_type": "sync_type",
    }

    def __init__(self_, sync_type: Union[str, UnsetType] = unset, **kwargs):
        """
        Sync property configuration

        :param sync_type:
        :type sync_type: str, optional
        """
        if sync_type is not unset:
            kwargs["sync_type"] = sync_type
        super().__init__(kwargs)
