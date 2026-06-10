# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.csm_host_facet_info_data import CsmHostFacetInfoData


class CsmHostFacetInfoResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.csm_host_facet_info_data import CsmHostFacetInfoData

        return {
            "data": (CsmHostFacetInfoData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: CsmHostFacetInfoData, **kwargs):
        """
        The response returned when requesting value distribution for a specific facet.

        :param data: The data wrapper for a facet info response.
        :type data: CsmHostFacetInfoData
        """
        super().__init__(kwargs)

        self_.data = data
