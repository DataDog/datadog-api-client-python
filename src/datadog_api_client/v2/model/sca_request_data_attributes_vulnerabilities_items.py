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
    from datadog_api_client.v2.model.sca_request_data_attributes_vulnerabilities_items_affects_items import (
        ScaRequestDataAttributesVulnerabilitiesItemsAffectsItems,
    )


class ScaRequestDataAttributesVulnerabilitiesItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sca_request_data_attributes_vulnerabilities_items_affects_items import (
            ScaRequestDataAttributesVulnerabilitiesItemsAffectsItems,
        )

        return {
            "affects": ([ScaRequestDataAttributesVulnerabilitiesItemsAffectsItems],),
            "bom_ref": (str,),
            "id": (str,),
        }

    attribute_map = {
        "affects": "affects",
        "bom_ref": "bom_ref",
        "id": "id",
    }

    def __init__(
        self_,
        affects: Union[List[ScaRequestDataAttributesVulnerabilitiesItemsAffectsItems], UnsetType] = unset,
        bom_ref: Union[str, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A vulnerability entry from the Software Bill of Materials (SBOM), describing a known security issue and the components it affects.

        :param affects: The list of components affected by this vulnerability.
        :type affects: [ScaRequestDataAttributesVulnerabilitiesItemsAffectsItems], optional

        :param bom_ref: The unique BOM reference identifier for this vulnerability entry.
        :type bom_ref: str, optional

        :param id: The vulnerability identifier (e.g., CVE ID or similar).
        :type id: str, optional
        """
        if affects is not unset:
            kwargs["affects"] = affects
        if bom_ref is not unset:
            kwargs["bom_ref"] = bom_ref
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)
