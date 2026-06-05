# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class SAMLConfigurationUpdateAttributes(ModelNormal):
    validations = {
        "jit_domains": {
            "max_items": 50,
            "min_items": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "idp_initiated": (bool,),
            "jit_domains": ([str],),
        }

    attribute_map = {
        "idp_initiated": "idp_initiated",
        "jit_domains": "jit_domains",
    }

    def __init__(
        self_, idp_initiated: Union[bool, UnsetType] = unset, jit_domains: Union[List[str], UnsetType] = unset, **kwargs
    ):
        """
        Attributes for updating a SAML configuration.

        :param idp_initiated: Whether identity-provider-initiated login is enabled for the organization.
        :type idp_initiated: bool, optional

        :param jit_domains: Email domains for which users are automatically provisioned on first SAML login
            (just-in-time provisioning). A default role is required to enable just-in-time provisioning.
        :type jit_domains: [str], optional
        """
        if idp_initiated is not unset:
            kwargs["idp_initiated"] = idp_initiated
        if jit_domains is not unset:
            kwargs["jit_domains"] = jit_domains
        super().__init__(kwargs)
