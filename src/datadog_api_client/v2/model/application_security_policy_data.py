# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.application_security_policy_attributes import ApplicationSecurityPolicyAttributes
    from datadog_api_client.v2.model.application_security_policy_metadata import ApplicationSecurityPolicyMetadata
    from datadog_api_client.v2.model.application_security_policy_type import ApplicationSecurityPolicyType


class ApplicationSecurityPolicyData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.application_security_policy_attributes import (
            ApplicationSecurityPolicyAttributes,
        )
        from datadog_api_client.v2.model.application_security_policy_metadata import ApplicationSecurityPolicyMetadata
        from datadog_api_client.v2.model.application_security_policy_type import ApplicationSecurityPolicyType

        return {
            "attributes": (ApplicationSecurityPolicyAttributes,),
            "id": (str,),
            "metadata": (ApplicationSecurityPolicyMetadata,),
            "type": (ApplicationSecurityPolicyType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "metadata": "metadata",
        "type": "type",
    }
    read_only_vars = {
        "id",
        "metadata",
    }

    def __init__(
        self_,
        attributes: Union[ApplicationSecurityPolicyAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        metadata: Union[ApplicationSecurityPolicyMetadata, UnsetType] = unset,
        type: Union[ApplicationSecurityPolicyType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object for a single WAF policy.

        :param attributes: A WAF policy.
        :type attributes: ApplicationSecurityPolicyAttributes, optional

        :param id: The ID of the policy.
        :type id: str, optional

        :param metadata: Metadata associated with the WAF policy.
        :type metadata: ApplicationSecurityPolicyMetadata, optional

        :param type: The type of the resource. The value should always be ``policy``.
        :type type: ApplicationSecurityPolicyType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if metadata is not unset:
            kwargs["metadata"] = metadata
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
