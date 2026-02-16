# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.integration_counts import IntegrationCounts


class ListActionConnectionsResponseMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.integration_counts import IntegrationCounts

        return {
            "integration_counts": ([IntegrationCounts], none_type),
            "total": (int,),
            "total_filtered": (int,),
        }

    attribute_map = {
        "integration_counts": "integration_counts",
        "total": "total",
        "total_filtered": "total_filtered",
    }

    def __init__(
        self_,
        total: int,
        total_filtered: int,
        integration_counts: Union[List[IntegrationCounts], none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Metadata for the list connections response.

        :param integration_counts: Count of integrations by type.
        :type integration_counts: [IntegrationCounts], none_type, optional

        :param total: The total number of connections.
        :type total: int

        :param total_filtered: The total number of connections that match the specified filters.
        :type total_filtered: int
        """
        if integration_counts is not unset:
            kwargs["integration_counts"] = integration_counts
        super().__init__(kwargs)

        self_.total = total
        self_.total_filtered = total_filtered
