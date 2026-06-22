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
    from datadog_api_client.v2.model.remediation_investigation import RemediationInvestigation


class RemediationListInvestigationsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.remediation_investigation import RemediationInvestigation

        return {
            "investigations": ([RemediationInvestigation],),
            "next_page_token": (str,),
        }

    attribute_map = {
        "investigations": "investigations",
        "next_page_token": "next_page_token",
    }

    def __init__(
        self_,
        investigations: Union[List[RemediationInvestigation], UnsetType] = unset,
        next_page_token: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response payload for listing investigations.

        :param investigations: The matching investigations.
        :type investigations: [RemediationInvestigation], optional

        :param next_page_token: Token to pass as page_token on the next call. Empty when there are no further pages.
        :type next_page_token: str, optional
        """
        if investigations is not unset:
            kwargs["investigations"] = investigations
        if next_page_token is not unset:
            kwargs["next_page_token"] = next_page_token
        super().__init__(kwargs)
