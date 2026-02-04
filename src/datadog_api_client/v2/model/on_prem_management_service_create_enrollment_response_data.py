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
    from datadog_api_client.v2.model.on_prem_management_service_create_enrollment_response_attributes import (
        OnPremManagementServiceCreateEnrollmentResponseAttributes,
    )
    from datadog_api_client.v2.model.on_prem_management_service_create_enrollment_response_type import (
        OnPremManagementServiceCreateEnrollmentResponseType,
    )


class OnPremManagementServiceCreateEnrollmentResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.on_prem_management_service_create_enrollment_response_attributes import (
            OnPremManagementServiceCreateEnrollmentResponseAttributes,
        )
        from datadog_api_client.v2.model.on_prem_management_service_create_enrollment_response_type import (
            OnPremManagementServiceCreateEnrollmentResponseType,
        )

        return {
            "attributes": (OnPremManagementServiceCreateEnrollmentResponseAttributes,),
            "id": (str,),
            "type": (OnPremManagementServiceCreateEnrollmentResponseType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: OnPremManagementServiceCreateEnrollmentResponseAttributes,
        id: str,
        type: OnPremManagementServiceCreateEnrollmentResponseType,
        **kwargs,
    ):
        """
        Data for the created enrollment.

        :param attributes: Attributes for the created enrollment.
        :type attributes: OnPremManagementServiceCreateEnrollmentResponseAttributes

        :param id: The token hash identifier.
        :type id: str

        :param type: The type of the resource. The value should always be createEnrollmentResponse.
        :type type: OnPremManagementServiceCreateEnrollmentResponseType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
