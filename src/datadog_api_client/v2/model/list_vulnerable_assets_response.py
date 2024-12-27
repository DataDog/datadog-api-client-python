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
    from datadog_api_client.v2.model.asset import Asset
    from datadog_api_client.v2.model.links import Links
    from datadog_api_client.v2.model.metadata import Metadata


class ListVulnerableAssetsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.asset import Asset
        from datadog_api_client.v2.model.links import Links
        from datadog_api_client.v2.model.metadata import Metadata

        return {
            "data": ([Asset],),
            "links": (Links,),
            "meta": (Metadata,),
        }

    attribute_map = {
        "data": "data",
        "links": "links",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: List[Asset],
        links: Union[Links, UnsetType] = unset,
        meta: Union[Metadata, UnsetType] = unset,
        **kwargs,
    ):
        """
        The expected response schema when listing vulnerable assets.

        :param data: List of vulnerable assets.
        :type data: [Asset]

        :param links: The JSON:API links related to pagination.
        :type links: Links, optional

        :param meta: The metadata related to this request.
        :type meta: Metadata, optional
        """
        if links is not unset:
            kwargs["links"] = links
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data
