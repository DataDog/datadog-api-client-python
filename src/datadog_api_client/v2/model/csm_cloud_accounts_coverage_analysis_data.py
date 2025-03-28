# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.csm_cloud_accounts_coverage_analysis_attributes import (
        CsmCloudAccountsCoverageAnalysisAttributes,
    )


class CsmCloudAccountsCoverageAnalysisData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.csm_cloud_accounts_coverage_analysis_attributes import (
            CsmCloudAccountsCoverageAnalysisAttributes,
        )

        return {
            "attributes": (CsmCloudAccountsCoverageAnalysisAttributes,),
            "id": (str,),
            "type": (str,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[CsmCloudAccountsCoverageAnalysisAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        CSM Cloud Accounts Coverage Analysis data.

        :param attributes: CSM Cloud Accounts Coverage Analysis attributes.
        :type attributes: CsmCloudAccountsCoverageAnalysisAttributes, optional

        :param id: The ID of your organization.
        :type id: str, optional

        :param type: The type of the resource. The value should always be ``get_cloud_accounts_coverage_analysis_response_public_v0``.
        :type type: str, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
