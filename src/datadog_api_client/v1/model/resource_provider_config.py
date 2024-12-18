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


class ResourceProviderConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "metrics_enabled": (bool,),
            "namespace": (str,),
        }

    attribute_map = {
        "metrics_enabled": "metrics_enabled",
        "namespace": "namespace",
    }

    def __init__(
        self_, metrics_enabled: Union[bool, UnsetType] = unset, namespace: Union[str, UnsetType] = unset, **kwargs
    ):
        """
        Configuration settings applied to resources from the specified Azure resource provider.

        :param metrics_enabled: Collect metrics for resources from this provider.
        :type metrics_enabled: bool, optional

        :param namespace: The provider namespace to apply this configuration to.
        :type namespace: str, optional
        """
        if metrics_enabled is not unset:
            kwargs["metrics_enabled"] = metrics_enabled
        if namespace is not unset:
            kwargs["namespace"] = namespace
        super().__init__(kwargs)
