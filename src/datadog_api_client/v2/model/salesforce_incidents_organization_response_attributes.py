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


class SalesforceIncidentsOrganizationResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "instance_url": (str,),
            "name": (str,),
            "sfdc_org_id": (str,),
            "sfdc_org_type": (str,),
        }

    attribute_map = {
        "instance_url": "instance_url",
        "name": "name",
        "sfdc_org_id": "sfdc_org_id",
        "sfdc_org_type": "sfdc_org_type",
    }

    def __init__(
        self_,
        instance_url: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        sfdc_org_id: Union[str, UnsetType] = unset,
        sfdc_org_type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a Salesforce organization connected to the Datadog Salesforce integration.

        :param instance_url: The Salesforce instance URL used to call this organization's APIs.
        :type instance_url: str, optional

        :param name: Human-readable name of the Salesforce organization.
        :type name: str, optional

        :param sfdc_org_id: The Salesforce organization identifier (15- or 18-character Salesforce org ID).
        :type sfdc_org_id: str, optional

        :param sfdc_org_type: The Salesforce organization type (for example, ``Production`` or ``Sandbox`` ).
        :type sfdc_org_type: str, optional
        """
        if instance_url is not unset:
            kwargs["instance_url"] = instance_url
        if name is not unset:
            kwargs["name"] = name
        if sfdc_org_id is not unset:
            kwargs["sfdc_org_id"] = sfdc_org_id
        if sfdc_org_type is not unset:
            kwargs["sfdc_org_type"] = sfdc_org_type
        super().__init__(kwargs)
