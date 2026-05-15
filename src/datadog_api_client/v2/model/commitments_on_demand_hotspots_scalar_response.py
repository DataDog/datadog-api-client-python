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
    from datadog_api_client.v2.model.commitments_on_demand_hotspots_scalar_meta import (
        CommitmentsOnDemandHotspotsScalarMeta,
    )


class CommitmentsOnDemandHotspotsScalarResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.commitments_scalar_column import CommitmentsScalarColumn
        from datadog_api_client.v2.model.commitments_on_demand_hotspots_scalar_meta import (
            CommitmentsOnDemandHotspotsScalarMeta,
        )

        return {
            "columns": ([CommitmentsScalarColumn],),
            "meta": (CommitmentsOnDemandHotspotsScalarMeta,),
            "total": ([CommitmentsScalarColumn],),
        }

    attribute_map = {
        "columns": "columns",
        "meta": "meta",
        "total": "total",
    }

    def __init__(
        self_,
        columns: List[CommitmentsScalarColumn],
        total: List[CommitmentsScalarColumn],
        meta: Union[CommitmentsOnDemandHotspotsScalarMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response containing scalar on-demand hot-spots data for cloud commitment programs.

        :param columns: Array of scalar columns in the response.
        :type columns: [CommitmentsScalarColumn]

        :param meta: Metadata for the on-demand hot-spots scalar response.
        :type meta: CommitmentsOnDemandHotspotsScalarMeta, optional

        :param total: Array of scalar columns in the response.
        :type total: [CommitmentsScalarColumn]
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.columns = columns
        self_.total = total
