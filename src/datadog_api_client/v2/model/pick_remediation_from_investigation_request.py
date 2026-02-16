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
    from datadog_api_client.v2.model.client_type import ClientType
    from datadog_api_client.v2.model.stability_level import StabilityLevel


class PickRemediationFromInvestigationRequest(ModelNormal):
    validations = {
        "number_of_relevant_actions": {
            "inclusive_maximum": 100,
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.client_type import ClientType
        from datadog_api_client.v2.model.stability_level import StabilityLevel

        return {
            "client": (ClientType,),
            "integrations": ([str],),
            "investigation": (str,),
            "number_of_keyword_variants": (int,),
            "number_of_relevant_actions": (int,),
            "stability": (StabilityLevel,),
        }

    attribute_map = {
        "client": "client",
        "integrations": "integrations",
        "investigation": "investigation",
        "number_of_keyword_variants": "number_of_keyword_variants",
        "number_of_relevant_actions": "number_of_relevant_actions",
        "stability": "stability",
    }

    def __init__(
        self_,
        investigation: str,
        number_of_relevant_actions: int,
        client: Union[ClientType, UnsetType] = unset,
        integrations: Union[List[str], UnsetType] = unset,
        number_of_keyword_variants: Union[int, UnsetType] = unset,
        stability: Union[StabilityLevel, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param client: The client type for action filtering.
        :type client: ClientType, optional

        :param integrations: List of integrations to filter actions by.
        :type integrations: [str], optional

        :param investigation: The investigation text to extract remediation keywords from.
        :type investigation: str

        :param number_of_keyword_variants: The number of keyword variants to generate.
        :type number_of_keyword_variants: int, optional

        :param number_of_relevant_actions: The number of relevant actions to return per keyword.
        :type number_of_relevant_actions: int

        :param stability: The stability level for action filtering.
        :type stability: StabilityLevel, optional
        """
        if client is not unset:
            kwargs["client"] = client
        if integrations is not unset:
            kwargs["integrations"] = integrations
        if number_of_keyword_variants is not unset:
            kwargs["number_of_keyword_variants"] = number_of_keyword_variants
        if stability is not unset:
            kwargs["stability"] = stability
        super().__init__(kwargs)

        self_.investigation = investigation
        self_.number_of_relevant_actions = number_of_relevant_actions
