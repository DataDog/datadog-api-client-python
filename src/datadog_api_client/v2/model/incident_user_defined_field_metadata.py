# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    UUID,
)


class IncidentUserDefinedFieldMetadata(ModelNormal):
    _nullable = True

    @cached_property
    def openapi_types(_):
        return {
            "category": (str,),
            "search_limit_param": (str,),
            "search_params": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
            "search_query_param": (str,),
            "search_result_path": (str,),
            "search_url": (str,),
        }

    attribute_map = {
        "category": "category",
        "search_limit_param": "search_limit_param",
        "search_params": "search_params",
        "search_query_param": "search_query_param",
        "search_result_path": "search_result_path",
        "search_url": "search_url",
    }

    def __init__(
        self_,
        category: str,
        search_limit_param: str,
        search_params: Dict[str, Any],
        search_query_param: str,
        search_result_path: str,
        search_url: str,
        **kwargs,
    ):
        """
        Metadata for autocomplete-type user-defined fields, describing how to populate autocomplete options.

        :param category: The category of the autocomplete source.
        :type category: str

        :param search_limit_param: The query parameter used to limit the number of autocomplete results.
        :type search_limit_param: str

        :param search_params: Additional query parameters to include in the search URL.
        :type search_params: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}

        :param search_query_param: The query parameter used to pass typed input to the search URL.
        :type search_query_param: str

        :param search_result_path: The JSON path to the results in the response body.
        :type search_result_path: str

        :param search_url: The URL used to populate autocomplete options.
        :type search_url: str
        """
        super().__init__(kwargs)

        self_.category = category
        self_.search_limit_param = search_limit_param
        self_.search_params = search_params
        self_.search_query_param = search_query_param
        self_.search_result_path = search_result_path
        self_.search_url = search_url
