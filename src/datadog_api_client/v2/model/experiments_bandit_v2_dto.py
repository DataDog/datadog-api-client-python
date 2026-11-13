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
    from datadog_api_client.v2.model.experiments_bandit_v2_dto_data import ExperimentsBanditV2DTOData
    from datadog_api_client.v2.model.experiments_bandit_v2_read_meta_dto import ExperimentsBanditV2ReadMetaDTO


class ExperimentsBanditV2DTO(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_bandit_v2_dto_data import ExperimentsBanditV2DTOData
        from datadog_api_client.v2.model.experiments_bandit_v2_read_meta_dto import ExperimentsBanditV2ReadMetaDTO

        return {
            "data": (ExperimentsBanditV2DTOData,),
            "meta": (ExperimentsBanditV2ReadMetaDTO,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: ExperimentsBanditV2DTOData,
        meta: Union[ExperimentsBanditV2ReadMetaDTO, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response containing a bandit.

        :param data: JSON:API resource containing a bandit.
        :type data: ExperimentsBanditV2DTOData

        :param meta: Information about the bandit response.
        :type meta: ExperimentsBanditV2ReadMetaDTO, optional
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data
