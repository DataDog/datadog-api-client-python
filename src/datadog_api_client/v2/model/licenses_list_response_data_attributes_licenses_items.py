# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LicensesListResponseDataAttributesLicensesItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "display_name": (str,),
            "identifier": (str,),
            "short_name": (str,),
        }

    attribute_map = {
        "display_name": "display_name",
        "identifier": "identifier",
        "short_name": "short_name",
    }

    def __init__(self_, display_name: str, identifier: str, short_name: str, **kwargs):
        """
        An SPDX license entry returned by the licenses list endpoint.

        :param display_name: The human-readable name of the license.
        :type display_name: str

        :param identifier: The SPDX identifier of the license.
        :type identifier: str

        :param short_name: The short name of the license, typically matching the SPDX identifier.
        :type short_name: str
        """
        super().__init__(kwargs)

        self_.display_name = display_name
        self_.identifier = identifier
        self_.short_name = short_name
