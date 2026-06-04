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
    from datadog_api_client.v2.model.org_saml_preferences_attributes import OrgSAMLPreferencesAttributes
    from datadog_api_client.v2.model.org_saml_preferences_type import OrgSAMLPreferencesType


class OrgSAMLPreferencesData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_saml_preferences_attributes import OrgSAMLPreferencesAttributes
        from datadog_api_client.v2.model.org_saml_preferences_type import OrgSAMLPreferencesType

        return {
            "attributes": (OrgSAMLPreferencesAttributes,),
            "id": (str,),
            "type": (OrgSAMLPreferencesType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: OrgSAMLPreferencesAttributes,
        type: OrgSAMLPreferencesType,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data for updating an organization's SAML preferences.

        :param attributes: Attributes for updating an organization's SAML preferences.
        :type attributes: OrgSAMLPreferencesAttributes

        :param id: The identifier of the SAML preferences resource.
        :type id: str, optional

        :param type: SAML preferences resource type.
        :type type: OrgSAMLPreferencesType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
