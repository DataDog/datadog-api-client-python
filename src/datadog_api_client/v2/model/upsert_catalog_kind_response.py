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
    from datadog_api_client.v2.model.kind_data import KindData
    from datadog_api_client.v2.model.kind_response_meta import KindResponseMeta


class UpsertCatalogKindResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.kind_data import KindData
        from datadog_api_client.v2.model.kind_response_meta import KindResponseMeta

        return {
            "data": ([KindData],),
            "meta": (KindResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[List[KindData], UnsetType] = unset,
        meta: Union[KindResponseMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Upsert kind response.

        :param data: List of kind responses.
        :type data: [KindData], optional

        :param meta: Kind response metadata.
        :type meta: KindResponseMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
