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
    from datadog_api_client.v2.model.custom_destination_google_security_operations_destination_auth import (
        CustomDestinationGoogleSecurityOperationsDestinationAuth,
    )
    from datadog_api_client.v2.model.custom_destination_forward_destination_google_security_operations_type import (
        CustomDestinationForwardDestinationGoogleSecurityOperationsType,
    )


class CustomDestinationForwardDestinationGoogleSecurityOperations(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_destination_google_security_operations_destination_auth import (
            CustomDestinationGoogleSecurityOperationsDestinationAuth,
        )
        from datadog_api_client.v2.model.custom_destination_forward_destination_google_security_operations_type import (
            CustomDestinationForwardDestinationGoogleSecurityOperationsType,
        )

        return {
            "auth": (CustomDestinationGoogleSecurityOperationsDestinationAuth,),
            "customer_id": (str,),
            "namespace": (str,),
            "regional_endpoint": (str,),
            "type": (CustomDestinationForwardDestinationGoogleSecurityOperationsType,),
        }

    attribute_map = {
        "auth": "auth",
        "customer_id": "customer_id",
        "namespace": "namespace",
        "regional_endpoint": "regional_endpoint",
        "type": "type",
    }

    def __init__(
        self_,
        auth: CustomDestinationGoogleSecurityOperationsDestinationAuth,
        customer_id: str,
        namespace: str,
        regional_endpoint: str,
        type: CustomDestinationForwardDestinationGoogleSecurityOperationsType,
        **kwargs,
    ):
        """
        The Google Security Operations destination.

        :param auth: Google Security Operations destination authentication.
        :type auth: CustomDestinationGoogleSecurityOperationsDestinationAuth

        :param customer_id: The customer ID of the Google Security Operations account.
        :type customer_id: str

        :param namespace: The namespace of the Google Security Operations account.
        :type namespace: str

        :param regional_endpoint: The ``CustomDestinationForwardDestinationGoogleSecurityOperations`` ``regional_endpoint``.
        :type regional_endpoint: str

        :param type: Type of the Google Security Operations destination.
        :type type: CustomDestinationForwardDestinationGoogleSecurityOperationsType
        """
        super().__init__(kwargs)

        self_.auth = auth
        self_.customer_id = customer_id
        self_.namespace = namespace
        self_.regional_endpoint = regional_endpoint
        self_.type = type
