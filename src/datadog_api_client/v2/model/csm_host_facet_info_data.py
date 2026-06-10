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
    from datadog_api_client.v2.model.csm_host_facet_info_attributes import CsmHostFacetInfoAttributes
    from datadog_api_client.v2.model.csm_host_facet_info_meta import CsmHostFacetInfoMeta
    from datadog_api_client.v2.model.csm_facet_info_type import CsmFacetInfoType


class CsmHostFacetInfoData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.csm_host_facet_info_attributes import CsmHostFacetInfoAttributes
        from datadog_api_client.v2.model.csm_host_facet_info_meta import CsmHostFacetInfoMeta
        from datadog_api_client.v2.model.csm_facet_info_type import CsmFacetInfoType

        return {
            "attributes": (CsmHostFacetInfoAttributes,),
            "id": (str,),
            "meta": (CsmHostFacetInfoMeta,),
            "type": (CsmFacetInfoType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "meta": "meta",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: CsmHostFacetInfoAttributes,
        id: str,
        meta: CsmHostFacetInfoMeta,
        type: CsmFacetInfoType,
        **kwargs,
    ):
        """
        The data wrapper for a facet info response.

        :param attributes: Attributes of a facet info response, containing the value distribution for the requested facet.
        :type attributes: CsmHostFacetInfoAttributes

        :param id: The identifier of the facet.
        :type id: str

        :param meta: Metadata for the facet info response.
        :type meta: CsmHostFacetInfoMeta

        :param type: The JSON:API type for facet info resources. The value should always be ``facet_info``.
        :type type: CsmFacetInfoType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.meta = meta
        self_.type = type
