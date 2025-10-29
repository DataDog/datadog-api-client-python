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
    from datadog_api_client.v2.model.funnel_suggestion_request_data_attributes_search import (
        FunnelSuggestionRequestDataAttributesSearch,
    )
    from datadog_api_client.v2.model.funnel_suggestion_request_data_attributes_term_search import (
        FunnelSuggestionRequestDataAttributesTermSearch,
    )
    from datadog_api_client.v2.model.funnel_suggestion_request_data_attributes_time import (
        FunnelSuggestionRequestDataAttributesTime,
    )


class FunnelSuggestionRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.funnel_suggestion_request_data_attributes_search import (
            FunnelSuggestionRequestDataAttributesSearch,
        )
        from datadog_api_client.v2.model.funnel_suggestion_request_data_attributes_term_search import (
            FunnelSuggestionRequestDataAttributesTermSearch,
        )
        from datadog_api_client.v2.model.funnel_suggestion_request_data_attributes_time import (
            FunnelSuggestionRequestDataAttributesTime,
        )

        return {
            "data_source": (str,),
            "search": (FunnelSuggestionRequestDataAttributesSearch,),
            "term_search": (FunnelSuggestionRequestDataAttributesTermSearch,),
            "time": (FunnelSuggestionRequestDataAttributesTime,),
        }

    attribute_map = {
        "data_source": "data_source",
        "search": "search",
        "term_search": "term_search",
        "time": "time",
    }

    def __init__(
        self_,
        data_source: Union[str, UnsetType] = unset,
        search: Union[FunnelSuggestionRequestDataAttributesSearch, UnsetType] = unset,
        term_search: Union[FunnelSuggestionRequestDataAttributesTermSearch, UnsetType] = unset,
        time: Union[FunnelSuggestionRequestDataAttributesTime, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param data_source:
        :type data_source: str, optional

        :param search:
        :type search: FunnelSuggestionRequestDataAttributesSearch, optional

        :param term_search:
        :type term_search: FunnelSuggestionRequestDataAttributesTermSearch, optional

        :param time:
        :type time: FunnelSuggestionRequestDataAttributesTime, optional
        """
        if data_source is not unset:
            kwargs["data_source"] = data_source
        if search is not unset:
            kwargs["search"] = search
        if term_search is not unset:
            kwargs["term_search"] = term_search
        if time is not unset:
            kwargs["time"] = time
        super().__init__(kwargs)
