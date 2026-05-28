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
    from datadog_api_client.v2.model.statuspage_account_create_data import StatuspageAccountCreateData


class StatuspageAccountCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.statuspage_account_create_data import StatuspageAccountCreateData

        return {
            "data": (StatuspageAccountCreateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: StatuspageAccountCreateData, **kwargs):
        """
        Create request for a Statuspage account.

        :param data: Statuspage account data for a create request.
        :type data: StatuspageAccountCreateData
        """
        super().__init__(kwargs)

        self_.data = data
