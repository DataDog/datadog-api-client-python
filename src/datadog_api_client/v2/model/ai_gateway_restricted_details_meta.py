# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AiGatewayRestrictedDetailsMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "restricted_details": (bool,),
        }

    attribute_map = {
        "restricted_details": "restricted_details",
    }

    def __init__(self_, restricted_details: bool, **kwargs):
        """
        Visibility information for identifying instance details.

        :param restricted_details: Whether identifying rows were withheld from the returned page. Pagination uses the underlying rows.
        :type restricted_details: bool
        """
        super().__init__(kwargs)

        self_.restricted_details = restricted_details
