# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class ScatterplotBackendTableRequest20270101OneOf4461523200(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "_query_options": (
                {
                    str: (
                        DashboardInlineSchema2,
                        none_type,
                    )
                },
            ),
            "q": (str,),
        }

    attribute_map = {
        "_query_options": "_query_options",
        "q": "q",
    }

    def __init__(
        self_,
        q: str,
        _query_options: Union[Dict[str, Union[DashboardInlineSchema2, str, float, bool]], UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param _query_options: Test-only generated schema for the dashboard versioning proof of concept.
        :type _query_options: {str: (DashboardInlineSchema2, none_type,)}, optional

        :param q: Test-only generated schema for the dashboard versioning proof of concept.
        :type q: str
        """
        if _query_options is not unset:
            kwargs["_query_options"] = _query_options
        super().__init__(kwargs)

        self_.q = q
