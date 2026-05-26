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
    from datadog_api_client.v2.model.application_security_policy_create_data import ApplicationSecurityPolicyCreateData


class ApplicationSecurityPolicyCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.application_security_policy_create_data import (
            ApplicationSecurityPolicyCreateData,
        )

        return {
            "data": (ApplicationSecurityPolicyCreateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ApplicationSecurityPolicyCreateData, **kwargs):
        """
        Request object that includes the policy to create.

        :param data: Object for a single WAF policy.
        :type data: ApplicationSecurityPolicyCreateData
        """
        super().__init__(kwargs)

        self_.data = data
