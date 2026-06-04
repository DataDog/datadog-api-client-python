# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class OAuth2WellKnownSitesAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "sites": ([str],),
        }

    attribute_map = {
        "sites": "sites",
    }

    def __init__(self_, sites: List[str], **kwargs):
        """
        Attributes containing the list of public OAuth2 sites.

        :param sites: Array of public OAuth2 site URLs for the environment.
        :type sites: [str]
        """
        super().__init__(kwargs)

        self_.sites = sites
