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
    from datadog_api_client.v2.model.saml_configuration_attributes import SAMLConfigurationAttributes
    from datadog_api_client.v2.model.saml_configuration_relationships import SAMLConfigurationRelationships
    from datadog_api_client.v2.model.saml_configurations_type import SAMLConfigurationsType


class SAMLConfiguration(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.saml_configuration_attributes import SAMLConfigurationAttributes
        from datadog_api_client.v2.model.saml_configuration_relationships import SAMLConfigurationRelationships
        from datadog_api_client.v2.model.saml_configurations_type import SAMLConfigurationsType

        return {
            "attributes": (SAMLConfigurationAttributes,),
            "id": (str,),
            "relationships": (SAMLConfigurationRelationships,),
            "type": (SAMLConfigurationsType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        type: SAMLConfigurationsType,
        attributes: Union[SAMLConfigurationAttributes, UnsetType] = unset,
        relationships: Union[SAMLConfigurationRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        A SAML configuration object.

        :param attributes: Attributes of a SAML configuration.
        :type attributes: SAMLConfigurationAttributes, optional

        :param id: The UUID of the SAML configuration.
        :type id: str

        :param relationships: Relationships of a SAML configuration.
        :type relationships: SAMLConfigurationRelationships, optional

        :param type: SAML configurations resource type.
        :type type: SAMLConfigurationsType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
