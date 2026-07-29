# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_configuration_data_attributes_request import (
        IncidentConfigurationDataAttributesRequest,
    )
    from datadog_api_client.v2.model.incident_configuration_type import IncidentConfigurationType


class IncidentConfigurationDataRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_configuration_data_attributes_request import (
            IncidentConfigurationDataAttributesRequest,
        )
        from datadog_api_client.v2.model.incident_configuration_type import IncidentConfigurationType

        return {
            "attributes": (IncidentConfigurationDataAttributesRequest,),
            "type": (IncidentConfigurationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        type: IncidentConfigurationType,
        attributes: Union[IncidentConfigurationDataAttributesRequest, UnsetType] = unset,
        **kwargs,
    ):
        """
        Incident configuration data in a create request.

        :param attributes: Attributes for creating an incident configuration.
        :type attributes: IncidentConfigurationDataAttributesRequest, optional

        :param type: Incident configuration resource type.
        :type type: IncidentConfigurationType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.type = type
