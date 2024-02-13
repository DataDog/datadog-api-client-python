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
    from datadog_api_client.v2.model.case import Case
    from datadog_api_client.v2.model.cases_response_meta import CasesResponseMeta


class CasesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.case import Case
        from datadog_api_client.v2.model.cases_response_meta import CasesResponseMeta

        return {
            "data": ([Case],),
            "meta": (CasesResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_, data: Union[List[Case], UnsetType] = unset, meta: Union[CasesResponseMeta, UnsetType] = unset, **kwargs
    ):
        """
        Response with cases

        :param data: Cases response data
        :type data: [Case], optional

        :param meta: Cases response metadata
        :type meta: CasesResponseMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
