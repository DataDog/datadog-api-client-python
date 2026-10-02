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
    from datadog_api_client.v2.model.experiments_update_exposure_sql_model_v2_request_data_attributes import (
        ExperimentsUpdateExposureSQLModelV2RequestDataAttributes,
    )
    from datadog_api_client.v2.model.experiments_update_exposure_sql_model_v2_request_data_type import (
        ExperimentsUpdateExposureSQLModelV2RequestDataType,
    )


class ExperimentsCreateExposureSQLModelV2RequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_update_exposure_sql_model_v2_request_data_attributes import (
            ExperimentsUpdateExposureSQLModelV2RequestDataAttributes,
        )
        from datadog_api_client.v2.model.experiments_update_exposure_sql_model_v2_request_data_type import (
            ExperimentsUpdateExposureSQLModelV2RequestDataType,
        )

        return {
            "attributes": (ExperimentsUpdateExposureSQLModelV2RequestDataAttributes,),
            "id": (str,),
            "type": (ExperimentsUpdateExposureSQLModelV2RequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ExperimentsUpdateExposureSQLModelV2RequestDataAttributes,
        type: ExperimentsUpdateExposureSQLModelV2RequestDataType,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Exposure SQL model resource to create.

        :param attributes: Complete column mappings and query used to replace the exposure SQL model.
        :type attributes: ExperimentsUpdateExposureSQLModelV2RequestDataAttributes

        :param id: Optional JSON:API resource identifier field.
        :type id: str, optional

        :param type: Exposure SQL models resource type.
        :type type: ExperimentsUpdateExposureSQLModelV2RequestDataType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
