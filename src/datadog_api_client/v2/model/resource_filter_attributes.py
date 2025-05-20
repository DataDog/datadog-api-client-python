# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class ResourceFilterAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "cloud_provider": ({str: ({str: ([str],)},)},),
            "uuid": (str,),
        }

    attribute_map = {
        "cloud_provider": "cloud_provider",
        "uuid": "uuid",
    }

    def __init__(self_, cloud_provider: Dict[str, Dict[str, List[str]]], uuid: Union[str, UnsetType] = unset, **kwargs):
        """
        Attributes of a resource filter.

        :param cloud_provider: A map of cloud provider names (e.g., "aws", "gcp", "azure") to a map of account/resource IDs and their associated tag filters.
        :type cloud_provider: {str: ({str: ([str],)},)}

        :param uuid: The UUID of the resource filter.
        :type uuid: str, optional
        """
        if uuid is not unset:
            kwargs["uuid"] = uuid
        super().__init__(kwargs)

        self_.cloud_provider = cloud_provider
