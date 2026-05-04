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
    from datadog_api_client.v2.model.oci_config_attributes import OCIConfigAttributes
    from datadog_api_client.v2.model.oci_config_type import OCIConfigType


class OCIConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.oci_config_attributes import OCIConfigAttributes
        from datadog_api_client.v2.model.oci_config_type import OCIConfigType

        return {
            "attributes": (OCIConfigAttributes,),
            "id": (str,),
            "type": (OCIConfigType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: OCIConfigAttributes, id: str, type: OCIConfigType, **kwargs):
        """
        OCI config.

        :param attributes: Attributes for an OCI config.
        :type attributes: OCIConfigAttributes

        :param id: The ID of the OCI config.
        :type id: str

        :param type: Type of OCI config.
        :type type: OCIConfigType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
