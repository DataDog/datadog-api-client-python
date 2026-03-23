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
    from datadog_api_client.v2.model.facet_info_request_data import FacetInfoRequestData


class FacetInfoRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.facet_info_request_data import FacetInfoRequestData

        return {
            "data": (FacetInfoRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[FacetInfoRequestData, UnsetType] = unset, **kwargs):
        """
        Request body for retrieving facet value information for a specified attribute with optional filtering.

        :param data: The data object containing the resource type and attributes for the facet info request.
        :type data: FacetInfoRequestData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
