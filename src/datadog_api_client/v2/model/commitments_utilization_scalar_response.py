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
    from datadog_api_client.v2.model.commitments_scalar_column import CommitmentsScalarColumn
    from datadog_api_client.v2.model.commitments_utilization_scalar_product_breakdown_entry import (
        CommitmentsUtilizationScalarProductBreakdownEntry,
    )


class CommitmentsUtilizationScalarResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.commitments_scalar_column import CommitmentsScalarColumn
        from datadog_api_client.v2.model.commitments_utilization_scalar_product_breakdown_entry import (
            CommitmentsUtilizationScalarProductBreakdownEntry,
        )

        return {
            "columns": ([CommitmentsScalarColumn],),
            "product_breakdown": ([CommitmentsUtilizationScalarProductBreakdownEntry],),
        }

    attribute_map = {
        "columns": "columns",
        "product_breakdown": "product_breakdown",
    }

    def __init__(
        self_,
        columns: List[CommitmentsScalarColumn],
        product_breakdown: Union[List[CommitmentsUtilizationScalarProductBreakdownEntry], UnsetType] = unset,
        **kwargs,
    ):
        """
        Response containing scalar utilization metrics for cloud commitment programs.

        :param columns: Array of scalar columns in the response.
        :type columns: [CommitmentsScalarColumn]

        :param product_breakdown: Array of per-product utilization breakdown entries.
        :type product_breakdown: [CommitmentsUtilizationScalarProductBreakdownEntry], optional
        """
        if product_breakdown is not unset:
            kwargs["product_breakdown"] = product_breakdown
        super().__init__(kwargs)

        self_.columns = columns
