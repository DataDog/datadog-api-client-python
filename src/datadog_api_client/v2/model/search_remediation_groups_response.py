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
    from datadog_api_client.v2.model.remediation_group_data import RemediationGroupData
    from datadog_api_client.v2.model.finding_case_response_data import FindingCaseResponseData
    from datadog_api_client.v2.model.remediation_groups_meta import RemediationGroupsMeta


class SearchRemediationGroupsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.remediation_group_data import RemediationGroupData
        from datadog_api_client.v2.model.finding_case_response_data import FindingCaseResponseData
        from datadog_api_client.v2.model.remediation_groups_meta import RemediationGroupsMeta

        return {
            "data": ([RemediationGroupData],),
            "included": ([FindingCaseResponseData],),
            "meta": (RemediationGroupsMeta,),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: List[RemediationGroupData],
        meta: RemediationGroupsMeta,
        included: Union[List[FindingCaseResponseData], UnsetType] = unset,
        **kwargs,
    ):
        """
        A page of remediation groups.

        :param data: Remediation groups of the page.
        :type data: [RemediationGroupData]

        :param included: Cases of the page's groups, when the request has ``include=case``.
        :type included: [FindingCaseResponseData], optional

        :param meta: Metadata of the search.
        :type meta: RemediationGroupsMeta
        """
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)

        self_.data = data
        self_.meta = meta
