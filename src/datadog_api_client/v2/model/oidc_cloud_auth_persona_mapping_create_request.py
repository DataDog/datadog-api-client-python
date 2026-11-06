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
    from datadog_api_client.v2.model.oidc_cloud_auth_persona_mapping_create_data import (
        OIDCCloudAuthPersonaMappingCreateData,
    )


class OIDCCloudAuthPersonaMappingCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.oidc_cloud_auth_persona_mapping_create_data import (
            OIDCCloudAuthPersonaMappingCreateData,
        )

        return {
            "data": (OIDCCloudAuthPersonaMappingCreateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: OIDCCloudAuthPersonaMappingCreateData, **kwargs):
        """
        Request to create a Custom OIDC persona mapping.

        :param data: Custom OIDC persona mapping creation data.
        :type data: OIDCCloudAuthPersonaMappingCreateData
        """
        super().__init__(kwargs)

        self_.data = data
