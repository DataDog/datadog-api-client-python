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
    from datadog_api_client.v2.model.custom_destination_google_security_operations_destination_auth_type import (
        CustomDestinationGoogleSecurityOperationsDestinationAuthType,
    )


class CustomDestinationGoogleSecurityOperationsDestinationAuth(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_destination_google_security_operations_destination_auth_type import (
            CustomDestinationGoogleSecurityOperationsDestinationAuthType,
        )

        return {
            "client_email": (str,),
            "client_id": (str,),
            "private_key": (str,),
            "private_key_id": (str,),
            "project_id": (str,),
            "type": (CustomDestinationGoogleSecurityOperationsDestinationAuthType,),
        }

    attribute_map = {
        "client_email": "client_email",
        "client_id": "client_id",
        "private_key": "private_key",
        "private_key_id": "private_key_id",
        "project_id": "project_id",
        "type": "type",
    }

    def __init__(
        self_,
        client_email: str,
        client_id: str,
        private_key: str,
        private_key_id: str,
        project_id: str,
        type: CustomDestinationGoogleSecurityOperationsDestinationAuthType,
        **kwargs,
    ):
        """
        Google Security Operations destination authentication.

        :param client_email: The Google Security Operations client email.
        :type client_email: str

        :param client_id: The Google Security Operations client ID. This field is not returned by the API.
        :type client_id: str

        :param private_key: The Google Security Operations private key. This field is not returned by the API.
        :type private_key: str

        :param private_key_id: The Google Security Operations private key ID. This field is not returned by the API.
        :type private_key_id: str

        :param project_id: Google Security Operations project ID.
        :type project_id: str

        :param type: Type of the Google Security Operations destination authentication.
        :type type: CustomDestinationGoogleSecurityOperationsDestinationAuthType
        """
        super().__init__(kwargs)

        self_.client_email = client_email
        self_.client_id = client_id
        self_.private_key = private_key
        self_.private_key_id = private_key_id
        self_.project_id = project_id
        self_.type = type
