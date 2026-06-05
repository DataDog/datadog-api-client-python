# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


class SAMLConfigurationAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "assertion_consumer_service": ([str],),
            "created_at": (datetime,),
            "entity_id": (str,),
            "expires_at": (datetime, none_type),
            "idp_initiated": (bool,),
            "jit_domains": ([str],),
            "modified_at": (datetime,),
            "sso_url": (str, none_type),
        }

    attribute_map = {
        "assertion_consumer_service": "assertion_consumer_service",
        "created_at": "created_at",
        "entity_id": "entity_id",
        "expires_at": "expires_at",
        "idp_initiated": "idp_initiated",
        "jit_domains": "jit_domains",
        "modified_at": "modified_at",
        "sso_url": "sso_url",
    }
    read_only_vars = {
        "created_at",
        "modified_at",
    }

    def __init__(
        self_,
        assertion_consumer_service: Union[List[str], UnsetType] = unset,
        created_at: Union[datetime, UnsetType] = unset,
        entity_id: Union[str, UnsetType] = unset,
        expires_at: Union[datetime, none_type, UnsetType] = unset,
        idp_initiated: Union[bool, UnsetType] = unset,
        jit_domains: Union[List[str], UnsetType] = unset,
        modified_at: Union[datetime, UnsetType] = unset,
        sso_url: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a SAML configuration.

        :param assertion_consumer_service: The assertion consumer service (ACS) URLs that the identity provider posts SAML responses to.
        :type assertion_consumer_service: [str], optional

        :param created_at: Creation time of the SAML configuration.
        :type created_at: datetime, optional

        :param entity_id: The service provider entity ID Datadog presents to the identity provider.
        :type entity_id: str, optional

        :param expires_at: Expiration time of the uploaded identity provider metadata.
        :type expires_at: datetime, none_type, optional

        :param idp_initiated: Whether identity-provider-initiated login is enabled for the organization.
        :type idp_initiated: bool, optional

        :param jit_domains: Email domains for which users are automatically provisioned on first SAML login
            (just-in-time provisioning).
        :type jit_domains: [str], optional

        :param modified_at: Time of the last SAML configuration modification.
        :type modified_at: datetime, optional

        :param sso_url: The single sign-on URL users can visit to start a SAML login.
            Returns ``null`` when the organization is identity-provider-initiated and has no subdomain.
        :type sso_url: str, none_type, optional
        """
        if assertion_consumer_service is not unset:
            kwargs["assertion_consumer_service"] = assertion_consumer_service
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if entity_id is not unset:
            kwargs["entity_id"] = entity_id
        if expires_at is not unset:
            kwargs["expires_at"] = expires_at
        if idp_initiated is not unset:
            kwargs["idp_initiated"] = idp_initiated
        if jit_domains is not unset:
            kwargs["jit_domains"] = jit_domains
        if modified_at is not unset:
            kwargs["modified_at"] = modified_at
        if sso_url is not unset:
            kwargs["sso_url"] = sso_url
        super().__init__(kwargs)
