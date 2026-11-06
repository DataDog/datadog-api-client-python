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
    from datadog_api_client.v2.model.create_status_page_email_access_policy_request_data import (
        CreateStatusPageEmailAccessPolicyRequestData,
    )


class CreateStatusPageEmailAccessPolicyRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_status_page_email_access_policy_request_data import (
            CreateStatusPageEmailAccessPolicyRequestData,
        )

        return {
            "data": (CreateStatusPageEmailAccessPolicyRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: CreateStatusPageEmailAccessPolicyRequestData, **kwargs):
        """
        Request object for creating a status page email access policy.

        :param data: The data object for creating a status page email access policy.
        :type data: CreateStatusPageEmailAccessPolicyRequestData
        """
        super().__init__(kwargs)

        self_.data = data
