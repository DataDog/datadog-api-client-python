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
    from datadog_api_client.v2.model.account_filtering_config import AccountFilteringConfig


class AccountFiltersPatchRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.account_filtering_config import AccountFilteringConfig

        return {
            "account_filters": (AccountFilteringConfig,),
        }

    attribute_map = {
        "account_filters": "account_filters",
    }

    def __init__(self_, account_filters: AccountFilteringConfig, **kwargs):
        """
        Attributes for an account filters patch request.

        :param account_filters: The account filtering configuration.
        :type account_filters: AccountFilteringConfig
        """
        super().__init__(kwargs)

        self_.account_filters = account_filters
