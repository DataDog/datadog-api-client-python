# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_google_chat_configuration_data_response import (
        IncidentGoogleChatConfigurationDataResponse,
    )
    from datadog_api_client.v2.model.incident_user_data import IncidentUserData


class IncidentGoogleChatConfigurationResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_google_chat_configuration_data_response import (
            IncidentGoogleChatConfigurationDataResponse,
        )
        from datadog_api_client.v2.model.incident_user_data import IncidentUserData

        return {
            "data": (IncidentGoogleChatConfigurationDataResponse,),
            "included": ([IncidentUserData],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }
    read_only_vars = {
        "included",
    }

    def __init__(
        self_,
        data: IncidentGoogleChatConfigurationDataResponse,
        included: Union[List[IncidentUserData], UnsetType] = unset,
        **kwargs,
    ):
        """
        Response with a Google Chat configuration.

        :param data: Google Chat configuration data in a response.
        :type data: IncidentGoogleChatConfigurationDataResponse

        :param included: Included related resources.
        :type included: [IncidentUserData], optional
        """
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)

        self_.data = data
