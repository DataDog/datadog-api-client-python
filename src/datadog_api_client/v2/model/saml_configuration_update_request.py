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
    from datadog_api_client.v2.model.saml_configuration_update_data import SAMLConfigurationUpdateData


class SAMLConfigurationUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.saml_configuration_update_data import SAMLConfigurationUpdateData

        return {
            "data": (SAMLConfigurationUpdateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: SAMLConfigurationUpdateData, **kwargs):
        """
        Request to update a SAML configuration.

        :param data: Data for updating a SAML configuration.
        :type data: SAMLConfigurationUpdateData
        """
        super().__init__(kwargs)

        self_.data = data
