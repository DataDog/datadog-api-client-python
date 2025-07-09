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
    from datadog_api_client.v2.model.custom_destination_response_google_security_operations_destination_auth_type import (
        CustomDestinationResponseGoogleSecurityOperationsDestinationAuthType,
    )


class CustomDestinationResponseGoogleSecurityOperationsDestinationAuth(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_destination_response_google_security_operations_destination_auth_type import (
            CustomDestinationResponseGoogleSecurityOperationsDestinationAuthType,
        )

        return {
            "client_email": (str,),
            "project_id": (str,),
            "type": (CustomDestinationResponseGoogleSecurityOperationsDestinationAuthType,),
        }

    attribute_map = {
        "client_email": "client_email",
        "project_id": "project_id",
        "type": "type",
    }

    def __init__(
        self_,
        client_email: str,
        project_id: str,
        type: CustomDestinationResponseGoogleSecurityOperationsDestinationAuthType,
        **kwargs,
    ):
        """
        Google Security Operations destination authentication.

        :param client_email: The Google Security Operations client email.
        :type client_email: str

        :param project_id: Google Security Operations project ID.
        :type project_id: str

        :param type: Type of the Google Security Operations destination authentication.
        :type type: CustomDestinationResponseGoogleSecurityOperationsDestinationAuthType
        """
        super().__init__(kwargs)

        self_.client_email = client_email
        self_.project_id = project_id
        self_.type = type
