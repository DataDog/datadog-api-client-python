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
    from datadog_api_client.v2.model.experiments_exposure_sql_model_v2_dto_data import (
        ExperimentsExposureSQLModelV2DTOData,
    )
    from datadog_api_client.v2.model.experiments_update_exposure_sql_model_v2_response_meta import (
        ExperimentsUpdateExposureSQLModelV2ResponseMeta,
    )


class ExperimentsUpdateExposureSQLModelV2Response(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_exposure_sql_model_v2_dto_data import (
            ExperimentsExposureSQLModelV2DTOData,
        )
        from datadog_api_client.v2.model.experiments_update_exposure_sql_model_v2_response_meta import (
            ExperimentsUpdateExposureSQLModelV2ResponseMeta,
        )

        return {
            "data": (ExperimentsExposureSQLModelV2DTOData,),
            "meta": (ExperimentsUpdateExposureSQLModelV2ResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: ExperimentsExposureSQLModelV2DTOData,
        meta: Union[ExperimentsUpdateExposureSQLModelV2ResponseMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Updated exposure SQL model and its removed entries.

        :param data: Exposure SQL model resource with its identifier and configuration.
        :type data: ExperimentsExposureSQLModelV2DTOData

        :param meta: Removed model entries. Present only when the update removes an entry.
        :type meta: ExperimentsUpdateExposureSQLModelV2ResponseMeta, optional
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data
