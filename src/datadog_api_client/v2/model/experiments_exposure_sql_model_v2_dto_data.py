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
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_exposure_sql_model_v2_dto_data_attributes import (
        ExperimentsExposureSQLModelV2DTODataAttributes,
    )
    from datadog_api_client.v2.model.experiments_update_exposure_sql_model_v2_request_data_type import (
        ExperimentsUpdateExposureSQLModelV2RequestDataType,
    )


class ExperimentsExposureSQLModelV2DTOData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_exposure_sql_model_v2_dto_data_attributes import (
            ExperimentsExposureSQLModelV2DTODataAttributes,
        )
        from datadog_api_client.v2.model.experiments_update_exposure_sql_model_v2_request_data_type import (
            ExperimentsUpdateExposureSQLModelV2RequestDataType,
        )

        return {
            "attributes": (ExperimentsExposureSQLModelV2DTODataAttributes,),
            "id": (UUID,),
            "type": (ExperimentsUpdateExposureSQLModelV2RequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        id: UUID,
        type: ExperimentsUpdateExposureSQLModelV2RequestDataType,
        attributes: Union[ExperimentsExposureSQLModelV2DTODataAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        Exposure SQL model resource with its identifier and configuration.

        :param attributes: Query and column mappings used to read experiment assignment data.
        :type attributes: ExperimentsExposureSQLModelV2DTODataAttributes, optional

        :param id: Identifier of the exposure SQL model.
        :type id: UUID

        :param type: Exposure SQL models resource type.
        :type type: ExperimentsUpdateExposureSQLModelV2RequestDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
