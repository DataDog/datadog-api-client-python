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
    from datadog_api_client.v2.model.opsgenie_account_create_data import OpsgenieAccountCreateData


class OpsgenieAccountCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.opsgenie_account_create_data import OpsgenieAccountCreateData

        return {
            "data": (OpsgenieAccountCreateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: OpsgenieAccountCreateData, **kwargs):
        """
        Create request for an Opsgenie account.

        :param data: Opsgenie account data for a create request.
        :type data: OpsgenieAccountCreateData
        """
        super().__init__(kwargs)

        self_.data = data
