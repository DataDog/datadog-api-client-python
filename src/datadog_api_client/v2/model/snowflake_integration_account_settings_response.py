# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SnowflakeIntegrationAccountSettingsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "snowflake_account_identifier": (str,),
            "username": (str,),
        }

    attribute_map = {
        "snowflake_account_identifier": "snowflake_account_identifier",
        "username": "username",
    }

    def __init__(self_, snowflake_account_identifier: str, username: str, **kwargs):
        """
        Settings configured on the Snowflake integration account.

        :param snowflake_account_identifier: Identifier of the Snowflake account being monitored.
        :type snowflake_account_identifier: str

        :param username: Snowflake user Datadog authenticates as.
        :type username: str
        """
        super().__init__(kwargs)

        self_.snowflake_account_identifier = snowflake_account_identifier
        self_.username = username
