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


class AWSEventBridgeSource(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "region": (str,),
        }

    attribute_map = {
        "name": "name",
        "region": "region",
    }

    def __init__(self_, name: Union[str, UnsetType] = unset, region: Union[str, UnsetType] = unset, **kwargs):
        """
        An EventBridge source.

        :param name: The event source name.
        :type name: str, optional

        :param region: The event source's `AWS region <https://docs.aws.amazon.com/general/latest/gr/rande.html#regional-endpoints>`_.
        :type region: str, optional
        """
        if name is not unset:
            kwargs["name"] = name
        if region is not unset:
            kwargs["region"] = region
        super().__init__(kwargs)
