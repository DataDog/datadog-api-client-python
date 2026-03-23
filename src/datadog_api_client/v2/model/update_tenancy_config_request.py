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
    from datadog_api_client.v2.model.update_tenancy_config_data import UpdateTenancyConfigData


class UpdateTenancyConfigRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.update_tenancy_config_data import UpdateTenancyConfigData

        return {
            "data": (UpdateTenancyConfigData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: UpdateTenancyConfigData, **kwargs):
        """
        Request body for updating an existing OCI tenancy integration configuration.

        :param data: The data object for updating an existing OCI tenancy integration configuration, including the tenancy ID, type, and updated attributes.
        :type data: UpdateTenancyConfigData
        """
        super().__init__(kwargs)

        self_.data = data
