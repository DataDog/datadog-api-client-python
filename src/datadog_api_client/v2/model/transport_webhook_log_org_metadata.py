# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class TransportWebhookLogOrgMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "billing_country": (str,),
            "billing_plan": (str,),
            "customer_tier": (str,),
            "domain": (str,),
            "industry": (str,),
            "is_bugbounty": (str,),
            "is_msp": (str,),
            "name": (str,),
            "org_uuid": (str,),
            "parent_org_id": (str,),
            "premium_support": (str,),
            "root_org_id": (str,),
            "root_org_name": (str,),
            "shipping_country": (str,),
            "website": (str,),
            "when_created": (str,),
        }

    attribute_map = {
        "billing_country": "billing_country",
        "billing_plan": "billing_plan",
        "customer_tier": "customer_tier",
        "domain": "domain",
        "industry": "industry",
        "is_bugbounty": "is_bugbounty",
        "is_msp": "is_msp",
        "name": "name",
        "org_uuid": "org_uuid",
        "parent_org_id": "parent_org_id",
        "premium_support": "premium_support",
        "root_org_id": "root_org_id",
        "root_org_name": "root_org_name",
        "shipping_country": "shipping_country",
        "website": "website",
        "when_created": "when_created",
    }

    def __init__(
        self_,
        billing_country: Union[str, UnsetType] = unset,
        billing_plan: Union[str, UnsetType] = unset,
        customer_tier: Union[str, UnsetType] = unset,
        domain: Union[str, UnsetType] = unset,
        industry: Union[str, UnsetType] = unset,
        is_bugbounty: Union[str, UnsetType] = unset,
        is_msp: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        org_uuid: Union[str, UnsetType] = unset,
        parent_org_id: Union[str, UnsetType] = unset,
        premium_support: Union[str, UnsetType] = unset,
        root_org_id: Union[str, UnsetType] = unset,
        root_org_name: Union[str, UnsetType] = unset,
        shipping_country: Union[str, UnsetType] = unset,
        website: Union[str, UnsetType] = unset,
        when_created: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Metadata about the organization that sent the email.

        :param billing_country: Country code or name used for billing purposes.
        :type billing_country: str, optional

        :param billing_plan: The Datadog billing plan for the organization (for example, "pro", "enterprise").
        :type billing_plan: str, optional

        :param customer_tier: Support or account tier assigned to the organization (for example, "tier-1").
        :type customer_tier: str, optional

        :param domain: Primary email domain associated with the organization (for example, "example.com").
        :type domain: str, optional

        :param industry: Industry classification of the organization (for example, "technology", "finance").
        :type industry: str, optional

        :param is_bugbounty: Whether the organization is enrolled in the Datadog bug bounty program.
        :type is_bugbounty: str, optional

        :param is_msp: Whether the organization operates as a Managed Service Provider managing child orgs.
        :type is_msp: str, optional

        :param name: Display name of the organization as configured in Datadog account settings.
        :type name: str, optional

        :param org_uuid: Globally unique identifier for the Datadog organization (UUID v1 format).
        :type org_uuid: str, optional

        :param parent_org_id: Identifier of the immediate parent organization, if this is a child org.
        :type parent_org_id: str, optional

        :param premium_support: Whether the organization has a premium support plan with Datadog.
        :type premium_support: str, optional

        :param root_org_id: Identifier of the top-level parent organization in a multi-org account hierarchy.
        :type root_org_id: str, optional

        :param root_org_name: Display name of the top-level parent organization in a multi-org account hierarchy.
        :type root_org_name: str, optional

        :param shipping_country: Country code or name used for shipping or regional assignment.
        :type shipping_country: str, optional

        :param website: Website URL provided during organization registration.
        :type website: str, optional

        :param when_created: ISO 8601 timestamp of when the Datadog organization was created.
        :type when_created: str, optional
        """
        if billing_country is not unset:
            kwargs["billing_country"] = billing_country
        if billing_plan is not unset:
            kwargs["billing_plan"] = billing_plan
        if customer_tier is not unset:
            kwargs["customer_tier"] = customer_tier
        if domain is not unset:
            kwargs["domain"] = domain
        if industry is not unset:
            kwargs["industry"] = industry
        if is_bugbounty is not unset:
            kwargs["is_bugbounty"] = is_bugbounty
        if is_msp is not unset:
            kwargs["is_msp"] = is_msp
        if name is not unset:
            kwargs["name"] = name
        if org_uuid is not unset:
            kwargs["org_uuid"] = org_uuid
        if parent_org_id is not unset:
            kwargs["parent_org_id"] = parent_org_id
        if premium_support is not unset:
            kwargs["premium_support"] = premium_support
        if root_org_id is not unset:
            kwargs["root_org_id"] = root_org_id
        if root_org_name is not unset:
            kwargs["root_org_name"] = root_org_name
        if shipping_country is not unset:
            kwargs["shipping_country"] = shipping_country
        if website is not unset:
            kwargs["website"] = website
        if when_created is not unset:
            kwargs["when_created"] = when_created
        super().__init__(kwargs)
