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
    from datadog_api_client.v2.model.jira_account_data import JiraAccountData
    from datadog_api_client.v2.model.jira_accounts_meta import JiraAccountsMeta


class JiraAccountsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.jira_account_data import JiraAccountData
        from datadog_api_client.v2.model.jira_accounts_meta import JiraAccountsMeta

        return {
            "data": ([JiraAccountData],),
            "meta": (JiraAccountsMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(self_, data: List[JiraAccountData], meta: Union[JiraAccountsMeta, UnsetType] = unset, **kwargs):
        """
        Response containing Jira accounts

        :param data: Array of Jira account data objects
        :type data: [JiraAccountData]

        :param meta: Metadata for Jira accounts response
        :type meta: JiraAccountsMeta, optional
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data
