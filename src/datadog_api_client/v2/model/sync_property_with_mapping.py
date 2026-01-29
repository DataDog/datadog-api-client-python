# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class SyncPropertyWithMapping(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "mapping": ({str: (str,)},),
            "name_mapping": ({str: (str,)},),
            "sync_type": (str,),
        }

    attribute_map = {
        "mapping": "mapping",
        "name_mapping": "name_mapping",
        "sync_type": "sync_type",
    }

    def __init__(
        self_,
        mapping: Union[Dict[str, str], UnsetType] = unset,
        name_mapping: Union[Dict[str, str], UnsetType] = unset,
        sync_type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Sync property with mapping configuration

        :param mapping:
        :type mapping: {str: (str,)}, optional

        :param name_mapping:
        :type name_mapping: {str: (str,)}, optional

        :param sync_type:
        :type sync_type: str, optional
        """
        if mapping is not unset:
            kwargs["mapping"] = mapping
        if name_mapping is not unset:
            kwargs["name_mapping"] = name_mapping
        if sync_type is not unset:
            kwargs["sync_type"] = sync_type
        super().__init__(kwargs)
