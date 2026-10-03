# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.fleet_integration_schema_file_spec_v2 import FleetIntegrationSchemaFileSpecV2


class FleetIntegrationSchemaDetailV2Attributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_integration_schema_file_spec_v2 import FleetIntegrationSchemaFileSpecV2

        return {
            "files": ([FleetIntegrationSchemaFileSpecV2],),
            "folder": (str,),
            "name": (str,),
            "version": (str,),
        }

    attribute_map = {
        "files": "files",
        "folder": "folder",
        "name": "name",
        "version": "version",
    }

    def __init__(
        self_,
        files: List[FleetIntegrationSchemaFileSpecV2],
        folder: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        version: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for a single integration's configuration schema.

        :param files: The configuration file specifications for the integration. Always present, returned as an empty array when there are none.
        :type files: [FleetIntegrationSchemaFileSpecV2]

        :param folder: The integration folder key. Absent from the response when empty.
        :type folder: str, optional

        :param name: The display name of the integration. Absent from the response when empty.
        :type name: str, optional

        :param version: The integration version. Absent from the response when empty.
        :type version: str, optional
        """
        if folder is not unset:
            kwargs["folder"] = folder
        if name is not unset:
            kwargs["name"] = name
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)

        self_.files = files
