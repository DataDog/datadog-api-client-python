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
    from datadog_api_client.v2.model.list_rules_response_data_item import ListRulesResponseDataItem
    from datadog_api_client.v2.model.list_rules_response_links import ListRulesResponseLinks


class ListRulesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.list_rules_response_data_item import ListRulesResponseDataItem
        from datadog_api_client.v2.model.list_rules_response_links import ListRulesResponseLinks

        return {
            "data": ([ListRulesResponseDataItem],),
            "links": (ListRulesResponseLinks,),
        }

    attribute_map = {
        "data": "data",
        "links": "links",
    }

    def __init__(
        self_,
        data: Union[List[ListRulesResponseDataItem], UnsetType] = unset,
        links: Union[ListRulesResponseLinks, UnsetType] = unset,
        **kwargs,
    ):
        """
        Scorecard rules response.

        :param data: Array of rule details.
        :type data: [ListRulesResponseDataItem], optional

        :param links: Links attributes.
        :type links: ListRulesResponseLinks, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if links is not unset:
            kwargs["links"] = links
        super().__init__(kwargs)
