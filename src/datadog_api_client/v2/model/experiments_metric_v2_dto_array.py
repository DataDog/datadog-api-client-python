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
    from datadog_api_client.v2.model.experiments_metric_v2_dto_data import ExperimentsMetricV2DTOData
    from datadog_api_client.v2.model.experiments_offset_links import ExperimentsOffsetLinks
    from datadog_api_client.v2.model.experiments_offset_meta import ExperimentsOffsetMeta


class ExperimentsMetricV2DTOArray(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_metric_v2_dto_data import ExperimentsMetricV2DTOData
        from datadog_api_client.v2.model.experiments_offset_links import ExperimentsOffsetLinks
        from datadog_api_client.v2.model.experiments_offset_meta import ExperimentsOffsetMeta

        return {
            "data": ([ExperimentsMetricV2DTOData],),
            "links": (ExperimentsOffsetLinks,),
            "meta": (ExperimentsOffsetMeta,),
        }

    attribute_map = {
        "data": "data",
        "links": "links",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: List[ExperimentsMetricV2DTOData],
        links: Union[ExperimentsOffsetLinks, UnsetType] = unset,
        meta: Union[ExperimentsOffsetMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        List of metric resources with pagination information.

        :param data: Resources returned in this response.
        :type data: [ExperimentsMetricV2DTOData]

        :param links: Links for navigating a paginated result set.
        :type links: ExperimentsOffsetLinks, optional

        :param meta: Pagination information for a list response.
        :type meta: ExperimentsOffsetMeta, optional
        """
        if links is not unset:
            kwargs["links"] = links
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data
