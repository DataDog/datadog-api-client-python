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


class SecurityMonitoringTerraformExportAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "output": (str,),
            "resource_id": (str,),
            "type_name": (str,),
        }

    attribute_map = {
        "output": "output",
        "resource_id": "resource_id",
        "type_name": "type_name",
    }

    def __init__(self_, resource_id: str, type_name: str, output: Union[str, UnsetType] = unset, **kwargs):
        """
        Attributes of the Terraform export response.

        :param output: The Terraform configuration for the resource.
        :type output: str, optional

        :param resource_id: The ID of the exported resource.
        :type resource_id: str

        :param type_name: The Terraform resource type name.
        :type type_name: str
        """
        if output is not unset:
            kwargs["output"] = output
        super().__init__(kwargs)

        self_.resource_id = resource_id
        self_.type_name = type_name
