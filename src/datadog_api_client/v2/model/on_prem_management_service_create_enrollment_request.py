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
    from datadog_api_client.v2.model.on_prem_management_service_enrollment_data_request import (
        OnPremManagementServiceEnrollmentDataRequest,
    )


class OnPremManagementServiceCreateEnrollmentRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.on_prem_management_service_enrollment_data_request import (
            OnPremManagementServiceEnrollmentDataRequest,
        )

        return {
            "data": (OnPremManagementServiceEnrollmentDataRequest,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: OnPremManagementServiceEnrollmentDataRequest, **kwargs):
        """
        Request to create an enrollment for an on-prem runner.

        :param data: Data for creating an enrollment.
        :type data: OnPremManagementServiceEnrollmentDataRequest
        """
        super().__init__(kwargs)

        self_.data = data
