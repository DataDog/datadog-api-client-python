# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.resolve_vulnerable_symbols_request_data_attributes import (
        ResolveVulnerableSymbolsRequestDataAttributes,
    )
    from datadog_api_client.v2.model.resolve_vulnerable_symbols_request_data_type import (
        ResolveVulnerableSymbolsRequestDataType,
    )


class ResolveVulnerableSymbolsRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.resolve_vulnerable_symbols_request_data_attributes import (
            ResolveVulnerableSymbolsRequestDataAttributes,
        )
        from datadog_api_client.v2.model.resolve_vulnerable_symbols_request_data_type import (
            ResolveVulnerableSymbolsRequestDataType,
        )

        return {
            "attributes": (ResolveVulnerableSymbolsRequestDataAttributes,),
            "id": (str,),
            "type": (ResolveVulnerableSymbolsRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: ResolveVulnerableSymbolsRequestDataType,
        attributes: Union[ResolveVulnerableSymbolsRequestDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The data object in a request to resolve vulnerable symbols, containing the package PURLs and request type.

        :param attributes: The attributes of a request to resolve vulnerable symbols, containing the list of package PURLs to check.
        :type attributes: ResolveVulnerableSymbolsRequestDataAttributes, optional

        :param id: An optional identifier for this request data object.
        :type id: str, optional

        :param type: The type identifier for requests to resolve vulnerable symbols.
        :type type: ResolveVulnerableSymbolsRequestDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
