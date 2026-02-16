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


class IntegrationCounts(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "filtered_count": (int,),
            "integration_type": (str,),
            "total_count": (int,),
        }

    attribute_map = {
        "filtered_count": "filtered_count",
        "integration_type": "integration_type",
        "total_count": "total_count",
    }

    def __init__(
        self_,
        filtered_count: Union[int, UnsetType] = unset,
        integration_type: Union[str, UnsetType] = unset,
        total_count: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Count of integrations by type.

        :param filtered_count: The filtered count of integrations.
        :type filtered_count: int, optional

        :param integration_type: The integration type.
        :type integration_type: str, optional

        :param total_count: The total count of integrations.
        :type total_count: int, optional
        """
        if filtered_count is not unset:
            kwargs["filtered_count"] = filtered_count
        if integration_type is not unset:
            kwargs["integration_type"] = integration_type
        if total_count is not unset:
            kwargs["total_count"] = total_count
        super().__init__(kwargs)
