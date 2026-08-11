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
    from datadog_api_client.v2.model.create_degradation_request_data import CreateDegradationRequestData
    from datadog_api_client.v2.model.degradation_request_meta import DegradationRequestMeta


class CreateDegradationRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_degradation_request_data import CreateDegradationRequestData
        from datadog_api_client.v2.model.degradation_request_meta import DegradationRequestMeta

        return {
            "data": (CreateDegradationRequestData,),
            "meta": (DegradationRequestMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[CreateDegradationRequestData, UnsetType] = unset,
        meta: Union[DegradationRequestMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Request object for creating a degradation.

        :param data: The data object for creating a degradation.
        :type data: CreateDegradationRequestData, optional

        :param meta: The supported metadata for a degradation request.
        :type meta: DegradationRequestMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
