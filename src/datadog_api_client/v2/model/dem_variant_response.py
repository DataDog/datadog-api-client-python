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
    from datadog_api_client.v2.model.dem_variant_response_data import DemVariantResponseData


class DemVariantResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dem_variant_response_data import DemVariantResponseData

        return {
            "data": (DemVariantResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: DemVariantResponseData, **kwargs):
        """
        Response containing a DEM journey variant.

        :param data: Data object returned for a DEM journey variant.
        :type data: DemVariantResponseData
        """
        super().__init__(kwargs)

        self_.data = data
