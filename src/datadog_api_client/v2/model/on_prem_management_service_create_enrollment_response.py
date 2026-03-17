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
    from datadog_api_client.v2.model.on_prem_management_service_create_enrollment_response_data import (
        OnPremManagementServiceCreateEnrollmentResponseData,
    )


class OnPremManagementServiceCreateEnrollmentResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.on_prem_management_service_create_enrollment_response_data import (
            OnPremManagementServiceCreateEnrollmentResponseData,
        )

        return {
            "data": (OnPremManagementServiceCreateEnrollmentResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: OnPremManagementServiceCreateEnrollmentResponseData, **kwargs):
        """
        Response for creating an enrollment.

        :param data: Data for the created enrollment.
        :type data: OnPremManagementServiceCreateEnrollmentResponseData
        """
        super().__init__(kwargs)

        self_.data = data
