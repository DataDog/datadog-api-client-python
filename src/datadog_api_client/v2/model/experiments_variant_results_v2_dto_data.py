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
    from datadog_api_client.v2.model.experiments_variant_results_v2_dto_data_attributes import (
        ExperimentsVariantResultsV2DTODataAttributes,
    )
    from datadog_api_client.v2.model.experiments_variant_results_v2_dto_data_type import (
        ExperimentsVariantResultsV2DTODataType,
    )


class ExperimentsVariantResultsV2DTOData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_variant_results_v2_dto_data_attributes import (
            ExperimentsVariantResultsV2DTODataAttributes,
        )
        from datadog_api_client.v2.model.experiments_variant_results_v2_dto_data_type import (
            ExperimentsVariantResultsV2DTODataType,
        )

        return {
            "attributes": (ExperimentsVariantResultsV2DTODataAttributes,),
            "id": (str,),
            "type": (ExperimentsVariantResultsV2DTODataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        type: ExperimentsVariantResultsV2DTODataType,
        attributes: Union[ExperimentsVariantResultsV2DTODataAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        JSON:API resource containing the variant result identity and fields.

        :param attributes: Details of the variant result.
        :type attributes: ExperimentsVariantResultsV2DTODataAttributes, optional

        :param id: ID of the variant result.
        :type id: str

        :param type: Experiment variant results resource type.
        :type type: ExperimentsVariantResultsV2DTODataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
