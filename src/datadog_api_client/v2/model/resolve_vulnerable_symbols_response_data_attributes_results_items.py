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
    from datadog_api_client.v2.model.resolve_vulnerable_symbols_response_data_attributes_results_items_vulnerable_symbols_items import (
        ResolveVulnerableSymbolsResponseDataAttributesResultsItemsVulnerableSymbolsItems,
    )


class ResolveVulnerableSymbolsResponseDataAttributesResultsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.resolve_vulnerable_symbols_response_data_attributes_results_items_vulnerable_symbols_items import (
            ResolveVulnerableSymbolsResponseDataAttributesResultsItemsVulnerableSymbolsItems,
        )

        return {
            "purl": (str,),
            "vulnerable_symbols": ([ResolveVulnerableSymbolsResponseDataAttributesResultsItemsVulnerableSymbolsItems],),
        }

    attribute_map = {
        "purl": "purl",
        "vulnerable_symbols": "vulnerable_symbols",
    }

    def __init__(
        self_,
        purl: Union[str, UnsetType] = unset,
        vulnerable_symbols: Union[
            List[ResolveVulnerableSymbolsResponseDataAttributesResultsItemsVulnerableSymbolsItems], UnsetType
        ] = unset,
        **kwargs,
    ):
        """
        The definition of ``ResolveVulnerableSymbolsResponseDataAttributesResultsItems`` object.

        :param purl: The ``items`` ``purl``.
        :type purl: str, optional

        :param vulnerable_symbols: The ``items`` ``vulnerable_symbols``.
        :type vulnerable_symbols: [ResolveVulnerableSymbolsResponseDataAttributesResultsItemsVulnerableSymbolsItems], optional
        """
        if purl is not unset:
            kwargs["purl"] = purl
        if vulnerable_symbols is not unset:
            kwargs["vulnerable_symbols"] = vulnerable_symbols
        super().__init__(kwargs)
