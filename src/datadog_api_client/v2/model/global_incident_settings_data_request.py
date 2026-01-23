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
    from datadog_api_client.v2.model.global_incident_settings_attributes_request import (
        GlobalIncidentSettingsAttributesRequest,
    )
    from datadog_api_client.v2.model.global_incident_settings_type import GlobalIncidentSettingsType


class GlobalIncidentSettingsDataRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.global_incident_settings_attributes_request import (
            GlobalIncidentSettingsAttributesRequest,
        )
        from datadog_api_client.v2.model.global_incident_settings_type import GlobalIncidentSettingsType

        return {
            "attributes": (GlobalIncidentSettingsAttributesRequest,),
            "type": (GlobalIncidentSettingsType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        type: GlobalIncidentSettingsType,
        attributes: Union[GlobalIncidentSettingsAttributesRequest, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param attributes: Global incident settings attributes
        :type attributes: GlobalIncidentSettingsAttributesRequest, optional

        :param type: Global incident settings resource type
        :type type: GlobalIncidentSettingsType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.type = type
