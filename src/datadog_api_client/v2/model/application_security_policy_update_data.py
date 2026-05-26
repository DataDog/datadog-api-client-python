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
    from datadog_api_client.v2.model.application_security_policy_update_attributes import (
        ApplicationSecurityPolicyUpdateAttributes,
    )
    from datadog_api_client.v2.model.application_security_policy_type import ApplicationSecurityPolicyType


class ApplicationSecurityPolicyUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.application_security_policy_update_attributes import (
            ApplicationSecurityPolicyUpdateAttributes,
        )
        from datadog_api_client.v2.model.application_security_policy_type import ApplicationSecurityPolicyType

        return {
            "attributes": (ApplicationSecurityPolicyUpdateAttributes,),
            "type": (ApplicationSecurityPolicyType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: ApplicationSecurityPolicyUpdateAttributes, type: ApplicationSecurityPolicyType, **kwargs
    ):
        """
        Object for a single WAF policy.

        :param attributes: Update a WAF policy.
        :type attributes: ApplicationSecurityPolicyUpdateAttributes

        :param type: The type of the resource. The value should always be ``policy``.
        :type type: ApplicationSecurityPolicyType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
