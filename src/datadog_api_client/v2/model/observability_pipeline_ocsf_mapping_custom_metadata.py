# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class ObservabilityPipelineOcsfMappingCustomMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "_class": (str,),
            "profiles": ([str],),
            "version": (str,),
        }

    attribute_map = {
        "_class": "class",
        "profiles": "profiles",
        "version": "version",
    }

    def __init__(self_, _class: str, version: str, profiles: Union[List[str], UnsetType] = unset, **kwargs):
        """
        Metadata for the custom OCSF mapping.

        :param _class: The OCSF event class name.
        :type _class: str

        :param profiles: A list of OCSF profiles to apply.
        :type profiles: [str], optional

        :param version: The OCSF schema version.
        :type version: str
        """
        if profiles is not unset:
            kwargs["profiles"] = profiles
        super().__init__(kwargs)

        self_._class = _class
        self_.version = version
