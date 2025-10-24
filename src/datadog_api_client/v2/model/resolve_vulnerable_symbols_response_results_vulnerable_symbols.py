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
    from datadog_api_client.v2.model.resolve_vulnerable_symbols_response_results_vulnerable_symbols_symbols import (
        ResolveVulnerableSymbolsResponseResultsVulnerableSymbolsSymbols,
    )


class ResolveVulnerableSymbolsResponseResultsVulnerableSymbols(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.resolve_vulnerable_symbols_response_results_vulnerable_symbols_symbols import (
            ResolveVulnerableSymbolsResponseResultsVulnerableSymbolsSymbols,
        )

        return {
            "advisory_id": (str,),
            "symbols": ([ResolveVulnerableSymbolsResponseResultsVulnerableSymbolsSymbols],),
        }

    attribute_map = {
        "advisory_id": "advisory_id",
        "symbols": "symbols",
    }

    def __init__(
        self_,
        advisory_id: Union[str, UnsetType] = unset,
        symbols: Union[List[ResolveVulnerableSymbolsResponseResultsVulnerableSymbolsSymbols], UnsetType] = unset,
        **kwargs,
    ):
        """


        :param advisory_id:
        :type advisory_id: str, optional

        :param symbols:
        :type symbols: [ResolveVulnerableSymbolsResponseResultsVulnerableSymbolsSymbols], optional
        """
        if advisory_id is not unset:
            kwargs["advisory_id"] = advisory_id
        if symbols is not unset:
            kwargs["symbols"] = symbols
        super().__init__(kwargs)
