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
    from datadog_api_client.v2.model.o_auth2_well_known_sites_attributes import OAuth2WellKnownSitesAttributes
    from datadog_api_client.v2.model.o_auth2_well_known_sites_env_type import OAuth2WellKnownSitesEnvType


class OAuth2WellKnownSitesData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.o_auth2_well_known_sites_attributes import OAuth2WellKnownSitesAttributes
        from datadog_api_client.v2.model.o_auth2_well_known_sites_env_type import OAuth2WellKnownSitesEnvType

        return {
            "attributes": (OAuth2WellKnownSitesAttributes,),
            "id": (str,),
            "type": (OAuth2WellKnownSitesEnvType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: OAuth2WellKnownSitesAttributes, id: str, type: OAuth2WellKnownSitesEnvType, **kwargs
    ):
        """
        Data object containing OAuth2 well-known sites information.

        :param attributes: Attributes containing the list of public OAuth2 sites.
        :type attributes: OAuth2WellKnownSitesAttributes

        :param id: Environment identifier.
        :type id: str

        :param type: JSON:API resource type for OAuth2 well-known sites environment.
        :type type: OAuth2WellKnownSitesEnvType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
