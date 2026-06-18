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
    from datadog_api_client.v2.model.intake_api_key_data import IntakeAPIKeyData


class IntakeAPIKeyResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.intake_api_key_data import IntakeAPIKeyData

        return {
            "data": (IntakeAPIKeyData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: IntakeAPIKeyData, **kwargs):
        """
        Response containing an intake API key for the authenticated cloud workload.

        :param data: An intake API key resource.
        :type data: IntakeAPIKeyData
        """
        super().__init__(kwargs)

        self_.data = data
