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


class ElasticCloudPrimaryShardGracefulTimeoutIntegrationDataflowRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "enabled": (bool,),
        }

    attribute_map = {
        "enabled": "enabled",
    }

    def __init__(self_, enabled: Union[bool, UnsetType] = unset, **kwargs):
        """
        Tolerance for slow primary shard requests. Primary shard metrics can grow large enough for the request to time out; enabling this keeps the rest of the collection running when that happens instead of failing the run. Only has an effect alongside ``elastic-cloud-primary-shard-stats``.

        :param enabled: Whether this tolerance is applied. Defaults to ``false`` ; set to ``true`` to apply it.
        :type enabled: bool, optional
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        super().__init__(kwargs)
