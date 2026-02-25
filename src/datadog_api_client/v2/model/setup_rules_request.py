# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.setup_rules_request_data import SetupRulesRequestData


class SetupRulesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.setup_rules_request_data import SetupRulesRequestData

        return {
            "data": (SetupRulesRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: SetupRulesRequestData, **kwargs):
        """
        Request to set up rules for an organization.

        :param data: Data for setting up rules.
        :type data: SetupRulesRequestData
        """
        super().__init__(kwargs)

        self_.data = data
