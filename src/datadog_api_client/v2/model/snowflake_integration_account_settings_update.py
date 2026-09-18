# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class SnowflakeIntegrationAccountSettingsUpdate(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

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

    def __init__(
        self_,
        snowflake_account_identifier: Union[str, UnsetType] = unset,
        username: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Settings for updating the Snowflake integration account. Only the fields provided are changed.

        :param snowflake_account_identifier: Identifier of the Snowflake account to monitor, either as ``organization-account`` or as the legacy ``account_name.region_id.cloud_provider`` account locator. An account identifier can be configured once per Datadog organization; reusing one is rejected with a ``422`` response. Accounts reached through AWS PrivateLink are not supported.
        :type snowflake_account_identifier: str, optional

        :param username: Snowflake user Datadog authenticates as. Create a dedicated user for Datadog and grant it a role with access to the data you want to collect.
        :type username: str, optional
        """
        if snowflake_account_identifier is not unset:
            kwargs["snowflake_account_identifier"] = snowflake_account_identifier
        if username is not unset:
            kwargs["username"] = username
        super().__init__(kwargs)
