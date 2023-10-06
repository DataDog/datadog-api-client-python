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
    from datadog_api_client.v2.model.powerpack_data import PowerpackData
    from datadog_api_client.v2.model.user import User
    from datadog_api_client.v2.model.powerpack_response_links import PowerpackResponseLinks
    from datadog_api_client.v2.model.powerpacks_response_meta import PowerpacksResponseMeta


class ListPowerpacksResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.powerpack_data import PowerpackData
        from datadog_api_client.v2.model.user import User
        from datadog_api_client.v2.model.powerpack_response_links import PowerpackResponseLinks
        from datadog_api_client.v2.model.powerpacks_response_meta import PowerpacksResponseMeta

        return {
            "data": ([PowerpackData],),
            "included": ([User],),
            "links": (PowerpackResponseLinks,),
            "meta": (PowerpacksResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
        "links": "links",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[List[PowerpackData], UnsetType] = unset,
        included: Union[List[User], UnsetType] = unset,
        links: Union[PowerpackResponseLinks, UnsetType] = unset,
        meta: Union[PowerpacksResponseMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response object which includes all powerpack configurations.

        :param data: List of powerpack definitions.
        :type data: [PowerpackData], optional

        :param included: Array of objects related to the users.
        :type included: [User], optional

        :param links: Links attributes.
        :type links: PowerpackResponseLinks, optional

        :param meta: Powerpack response metadata.
        :type meta: PowerpacksResponseMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if included is not unset:
            kwargs["included"] = included
        if links is not unset:
            kwargs["links"] = links
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
