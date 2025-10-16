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


class ScannedAssetMetadataLastSuccess(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "env": (str,),
            "origin": ([str],),
            "timestamp": (str,),
        }

    attribute_map = {
        "env": "env",
        "origin": "origin",
        "timestamp": "timestamp",
    }

    def __init__(
        self_, timestamp: str, env: Union[str, UnsetType] = unset, origin: Union[List[str], UnsetType] = unset, **kwargs
    ):
        """
        Metadata for the last successful scan of an asset.

        :param env: The environment of the last success scan of the asset.
        :type env: str, optional

        :param origin: The list of origins of the last success scan of the asset.
        :type origin: [str], optional

        :param timestamp: The timestamp of the last success scan of the asset.
        :type timestamp: str
        """
        if env is not unset:
            kwargs["env"] = env
        if origin is not unset:
            kwargs["origin"] = origin
        super().__init__(kwargs)

        self_.timestamp = timestamp
