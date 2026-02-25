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
    from datadog_api_client.v2.model.saml_configurations_update_attributes import SamlConfigurationsUpdateAttributes
    from datadog_api_client.v2.model.saml_configurations_update_request_data_type import (
        SamlConfigurationsUpdateRequestDataType,
    )


class SamlConfigurationsUpdateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.saml_configurations_update_attributes import SamlConfigurationsUpdateAttributes
        from datadog_api_client.v2.model.saml_configurations_update_request_data_type import (
            SamlConfigurationsUpdateRequestDataType,
        )

        return {
            "attributes": (SamlConfigurationsUpdateAttributes,),
            "type": (SamlConfigurationsUpdateRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: SamlConfigurationsUpdateAttributes, type: SamlConfigurationsUpdateRequestDataType, **kwargs
    ):
        """
        Data wrapper for SAML preferences update.

        :param attributes: Attributes for updating SAML preferences.
        :type attributes: SamlConfigurationsUpdateAttributes

        :param type: Type of the resource.
        :type type: SamlConfigurationsUpdateRequestDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
