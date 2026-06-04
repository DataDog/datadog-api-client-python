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
    from datadog_api_client.v2.model.o_auth2_well_known_sites_data import OAuth2WellKnownSitesData


class OAuth2WellKnownSitesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.o_auth2_well_known_sites_data import OAuth2WellKnownSitesData

        return {
            "data": (OAuth2WellKnownSitesData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: OAuth2WellKnownSitesData, **kwargs):
        """
        Response payload containing the list of public OAuth2 sites for discovery.

        :param data: Data object containing OAuth2 well-known sites information.
        :type data: OAuth2WellKnownSitesData
        """
        super().__init__(kwargs)

        self_.data = data
