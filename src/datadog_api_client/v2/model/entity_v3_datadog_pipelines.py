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


class EntityV3DatadogPipelines(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "fingerprints": ([str],),
        }

    attribute_map = {
        "fingerprints": "fingerprints",
    }

    def __init__(self_, fingerprints: Union[List[str], UnsetType] = unset, **kwargs):
        """
        CI Pipelines association

        :param fingerprints: A list of CI Fingerprints that associate CI Pipelines with the entity
        :type fingerprints: [str], optional
        """
        if fingerprints is not unset:
            kwargs["fingerprints"] = fingerprints
        super().__init__(kwargs)
