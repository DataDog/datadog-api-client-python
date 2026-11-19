# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_bandit_policy_history_v2_dto_data import (
        ExperimentsBanditPolicyHistoryV2DTOData,
    )
    from datadog_api_client.v2.model.experiments_offset_links import ExperimentsOffsetLinks
    from datadog_api_client.v2.model.experiments_offset_meta import ExperimentsOffsetMeta


class ExperimentsBanditPolicyHistoryV2DTOArray(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_bandit_policy_history_v2_dto_data import (
            ExperimentsBanditPolicyHistoryV2DTOData,
        )
        from datadog_api_client.v2.model.experiments_offset_links import ExperimentsOffsetLinks
        from datadog_api_client.v2.model.experiments_offset_meta import ExperimentsOffsetMeta

        return {
            "data": ([ExperimentsBanditPolicyHistoryV2DTOData],),
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
        data: List[ExperimentsBanditPolicyHistoryV2DTOData],
        links: ExperimentsOffsetLinks,
        meta: ExperimentsOffsetMeta,
        **kwargs,
    ):
        """
        Response containing a page of a bandit's policy history.

        :param data: Policies on this page.
        :type data: [ExperimentsBanditPolicyHistoryV2DTOData]

        :param links: Links for navigating a paginated result set.
        :type links: ExperimentsOffsetLinks

        :param meta: Pagination information for a list response.
        :type meta: ExperimentsOffsetMeta
        """
        super().__init__(kwargs)

        self_.data = data
        self_.links = links
        self_.meta = meta
