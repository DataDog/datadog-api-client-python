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
    from datadog_api_client.v2.model.validate_api_key_status import ValidateAPIKeyStatus


class ValidateAPIKeyResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.validate_api_key_status import ValidateAPIKeyStatus

        return {
            "status": (ValidateAPIKeyStatus,),
        }

    attribute_map = {
        "status": "status",
    }

    def __init__(self_, status: ValidateAPIKeyStatus, **kwargs):
        """
        Response object for the API and application key validation status check.

        :param status: Status of the validation. Always ``ok`` when both the API key and the application key are valid.
        :type status: ValidateAPIKeyStatus
        """
        super().__init__(kwargs)

        self_.status = status
