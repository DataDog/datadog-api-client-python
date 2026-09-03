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
    from datadog_api_client.v2.model.databricks_integration_account_update_data import (
        DatabricksIntegrationAccountUpdateData,
    )


class DatabricksIntegrationAccountUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.databricks_integration_account_update_data import (
            DatabricksIntegrationAccountUpdateData,
        )

        return {
            "data": (DatabricksIntegrationAccountUpdateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: DatabricksIntegrationAccountUpdateData, **kwargs):
        """
        Request payload to update a Databricks integration account.

        :param data: Data envelope for updating a Databricks integration account.
        :type data: DatabricksIntegrationAccountUpdateData
        """
        super().__init__(kwargs)

        self_.data = data
