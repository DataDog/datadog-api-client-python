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


class AzureAccountMetricsConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "excluded_resource_providers": ([str],),
        }

    attribute_map = {
        "excluded_resource_providers": "excluded_resource_providers",
    }

    def __init__(self_, excluded_resource_providers: Union[List[str], UnsetType] = unset, **kwargs):
        """
        Dictionary containing the key ``excluded_resource_providers`` which has to be a list of Microsoft Azure Resource Provider names.
        This feature is currently being beta tested.
        In order to enable all resource providers for metric collection, pass:
        ``metrics_config: {"excluded_resource_providers": []}`` (i.e., an empty list for ``excluded_resource_providers`` ).

        :param excluded_resource_providers: List of Microsoft Azure Resource Providers to exclude from metric collection.
        :type excluded_resource_providers: [str], optional
        """
        if excluded_resource_providers is not unset:
            kwargs["excluded_resource_providers"] = excluded_resource_providers
        super().__init__(kwargs)
