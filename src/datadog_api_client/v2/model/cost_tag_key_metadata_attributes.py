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
    from datadog_api_client.v2.model.cost_tag_key_metadata_cardinality_by_account import (
        CostTagKeyMetadataCardinalityByAccount,
    )
    from datadog_api_client.v2.model.cost_tag_key_metadata_top_values_by_account import (
        CostTagKeyMetadataTopValuesByAccount,
    )


class CostTagKeyMetadataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cost_tag_key_metadata_cardinality_by_account import (
            CostTagKeyMetadataCardinalityByAccount,
        )
        from datadog_api_client.v2.model.cost_tag_key_metadata_top_values_by_account import (
            CostTagKeyMetadataTopValuesByAccount,
        )

        return {
            "cardinality_by_account": (CostTagKeyMetadataCardinalityByAccount,),
            "cost_covered": (float,),
            "date": (str,),
            "metric": (str,),
            "row_count": (int,),
            "tag_sources": ([str],),
            "top_values_by_account": (CostTagKeyMetadataTopValuesByAccount,),
        }

    attribute_map = {
        "cardinality_by_account": "cardinality_by_account",
        "cost_covered": "cost_covered",
        "date": "date",
        "metric": "metric",
        "row_count": "row_count",
        "tag_sources": "tag_sources",
        "top_values_by_account": "top_values_by_account",
    }

    def __init__(
        self_,
        cardinality_by_account: CostTagKeyMetadataCardinalityByAccount,
        cost_covered: float,
        metric: str,
        row_count: int,
        tag_sources: List[str],
        top_values_by_account: CostTagKeyMetadataTopValuesByAccount,
        date: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a Cloud Cost Management tag key metadata entry.

        :param cardinality_by_account: Number of unique tag values observed for this tag key, keyed by cloud account ID.
        :type cardinality_by_account: CostTagKeyMetadataCardinalityByAccount

        :param cost_covered: Total cost (in the report currency) of cost line items that carry this tag key for the requested period.
        :type cost_covered: float

        :param date: The day this row corresponds to, in ``YYYY-MM-DD`` format. Present only when ``filter[daily]=true`` ; omitted for the monthly roll-up returned by default.
        :type date: str, optional

        :param metric: The Cloud Cost Management metric this row aggregates, for example ``aws.cost.net.amortized``.
        :type metric: str

        :param row_count: Number of cost rows that carry this tag key over the requested period.
        :type row_count: int

        :param tag_sources: Origins where this tag key was observed (for example, ``aws-user-defined`` ).
        :type tag_sources: [str]

        :param top_values_by_account: A sample of the most frequent tag values observed for this tag key, keyed by cloud account ID.
        :type top_values_by_account: CostTagKeyMetadataTopValuesByAccount
        """
        if date is not unset:
            kwargs["date"] = date
        super().__init__(kwargs)

        self_.cardinality_by_account = cardinality_by_account
        self_.cost_covered = cost_covered
        self_.metric = metric
        self_.row_count = row_count
        self_.tag_sources = tag_sources
        self_.top_values_by_account = top_values_by_account
