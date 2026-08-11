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
    from datadog_api_client.v2.model.stix_indicator_object import STIXIndicatorObject
    from datadog_api_client.v2.model.stix_spec_version import STIXSpecVersion
    from datadog_api_client.v2.model.stix_bundle_type import STIXBundleType


class STIXBundleRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.stix_indicator_object import STIXIndicatorObject
        from datadog_api_client.v2.model.stix_spec_version import STIXSpecVersion
        from datadog_api_client.v2.model.stix_bundle_type import STIXBundleType

        return {
            "id": (str,),
            "objects": ([STIXIndicatorObject],),
            "spec_version": (STIXSpecVersion,),
            "type": (STIXBundleType,),
        }

    attribute_map = {
        "id": "id",
        "objects": "objects",
        "spec_version": "spec_version",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        objects: List[STIXIndicatorObject],
        type: STIXBundleType,
        spec_version: Union[STIXSpecVersion, UnsetType] = unset,
        **kwargs,
    ):
        """
        A STIX 2.1 bundle containing threat intelligence indicator objects.

        :param id: The STIX bundle identifier.
        :type id: str

        :param objects: The indicator objects included in the bundle.
        :type objects: [STIXIndicatorObject]

        :param spec_version: The supported STIX specification version.
        :type spec_version: STIXSpecVersion, optional

        :param type: The STIX object type for a bundle.
        :type type: STIXBundleType
        """
        if spec_version is not unset:
            kwargs["spec_version"] = spec_version
        super().__init__(kwargs)

        self_.id = id
        self_.objects = objects
        self_.type = type
