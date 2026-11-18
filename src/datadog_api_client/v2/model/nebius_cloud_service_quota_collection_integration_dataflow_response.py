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


class NebiusCloudServiceQuotaCollectionIntegrationDataflowResponse(ModelNormal):
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
        Usage metrics tracked against your Nebius service quotas, such as ``nebius_cloud.servicequota.percentage_used`` and ``nebius_cloud.servicequota.limit``.

        :param enabled: Whether Datadog collects this data. Absent when the dataflow has never been configured.
        :type enabled: bool, optional
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        super().__init__(kwargs)
