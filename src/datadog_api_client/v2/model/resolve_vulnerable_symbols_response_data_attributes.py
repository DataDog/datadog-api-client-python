# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.resolve_vulnerable_symbols_response_results import (
        ResolveVulnerableSymbolsResponseResults,
    )


class ResolveVulnerableSymbolsResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.resolve_vulnerable_symbols_response_results import (
            ResolveVulnerableSymbolsResponseResults,
        )

        return {
            "results": ([ResolveVulnerableSymbolsResponseResults],),
        }

    attribute_map = {
        "results": "results",
    }

    def __init__(self_, results: Union[List[ResolveVulnerableSymbolsResponseResults], UnsetType] = unset, **kwargs):
        """


        :param results:
        :type results: [ResolveVulnerableSymbolsResponseResults], optional
        """
        if results is not unset:
            kwargs["results"] = results
        super().__init__(kwargs)
