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
    from datadog_api_client.v2.model.snowflake_integration_account_response_data import (
        SnowflakeIntegrationAccountResponseData,
    )


class SnowflakeIntegrationAccountsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.snowflake_integration_account_response_data import (
            SnowflakeIntegrationAccountResponseData,
        )

        return {
            "data": ([SnowflakeIntegrationAccountResponseData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[SnowflakeIntegrationAccountResponseData], **kwargs):
        """
        Response payload for a list of Snowflake integration accounts.

        :param data: List of Snowflake integration accounts.
        :type data: [SnowflakeIntegrationAccountResponseData]
        """
        super().__init__(kwargs)

        self_.data = data
