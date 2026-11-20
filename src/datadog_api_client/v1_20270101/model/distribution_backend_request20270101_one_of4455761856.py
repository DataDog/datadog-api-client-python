# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.dashboard_inline_schema7 import DashboardInlineSchema7
    from datadog_api_client.v1_20270101.model.request_style import RequestStyle


class DistributionBackendRequest20270101OneOf4455761856(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.dashboard_inline_schema7 import DashboardInlineSchema7
        from datadog_api_client.v1_20270101.model.request_style import RequestStyle

        return {
            "_query_options": (
                {
                    str: (
                        DashboardInlineSchema7,
                        none_type,
                    )
                },
            ),
            "q": (str,),
            "style": (RequestStyle,),
        }

    attribute_map = {
        "_query_options": "_query_options",
        "q": "q",
        "style": "style",
    }

    def __init__(
        self_,
        q: str,
        _query_options: Union[Dict[str, Union[DashboardInlineSchema7, str, float, bool]], UnsetType] = unset,
        style: Union[RequestStyle, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param _query_options: Test-only generated schema for the dashboard versioning proof of concept.
        :type _query_options: {str: (DashboardInlineSchema7, none_type,)}, optional

        :param q: Test-only generated schema for the dashboard versioning proof of concept.
        :type q: str

        :param style: Test-only generated schema for the dashboard versioning proof of concept.
        :type style: RequestStyle, optional
        """
        if _query_options is not unset:
            kwargs["_query_options"] = _query_options
        if style is not unset:
            kwargs["style"] = style
        super().__init__(kwargs)

        self_.q = q
