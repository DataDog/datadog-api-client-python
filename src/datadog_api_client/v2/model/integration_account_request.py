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
    from datadog_api_client.v2.model.integration_account_create_data import IntegrationAccountCreateData


class IntegrationAccountRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.integration_account_create_data import IntegrationAccountCreateData

        return {
            "data": (IntegrationAccountCreateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: IntegrationAccountCreateData, **kwargs):
        """
        Request payload to create an integration account.

        :param data: Data envelope for creating an integration account.
        :type data: IntegrationAccountCreateData
        """
        super().__init__(kwargs)

        self_.data = data
