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
    from datadog_api_client.v2.model.commitments_query_definition import CommitmentsQueryDefinition


class CommitmentsOnDemandHotspotsScalarResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.commitments_scalar_column import CommitmentsScalarColumn
        from datadog_api_client.v2.model.commitments_query_definition import CommitmentsQueryDefinition

        return {
            "columns": ([CommitmentsScalarColumn],),
            "query_definition": (CommitmentsQueryDefinition,),
            "total": ([CommitmentsScalarColumn],),
        }

    attribute_map = {
        "columns": "columns",
        "query_definition": "query_definition",
        "total": "total",
    }

    def __init__(
        self_,
        columns: List[CommitmentsScalarColumn],
        total: List[CommitmentsScalarColumn],
        query_definition: Union[CommitmentsQueryDefinition, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a scalar on-demand hot-spots response.

        :param columns: Array of scalar columns in the response.
        :type columns: [CommitmentsScalarColumn]

        :param query_definition: The query that produces the response values, in the same format as dashboard and notebook widget
            requests, so a client can graph the values in a widget. Each formula's ``id`` names the response value
            that it produces.
        :type query_definition: CommitmentsQueryDefinition, optional

        :param total: Array of scalar columns in the response.
        :type total: [CommitmentsScalarColumn]
        """
        if query_definition is not unset:
            kwargs["query_definition"] = query_definition
        super().__init__(kwargs)

        self_.columns = columns
        self_.total = total
