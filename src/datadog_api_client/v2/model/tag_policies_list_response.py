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
    from datadog_api_client.v2.model.tag_policy_data import TagPolicyData
    from datadog_api_client.v2.model.tag_policy_score_data import TagPolicyScoreData


class TagPoliciesListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.tag_policy_data import TagPolicyData
        from datadog_api_client.v2.model.tag_policy_score_data import TagPolicyScoreData

        return {
            "data": ([TagPolicyData],),
            "included": ([TagPolicyScoreData],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(
        self_, data: List[TagPolicyData], included: Union[List[TagPolicyScoreData], UnsetType] = unset, **kwargs
    ):
        """
        A page of tag policies.

        :param data: An array of tag policy data objects.
        :type data: [TagPolicyData]

        :param included: Related resources fetched alongside the primary tag policies. Populated when an ``include`` query parameter is supplied.
        :type included: [TagPolicyScoreData], optional
        """
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)

        self_.data = data
