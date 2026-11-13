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
    from datadog_api_client.v2.model.experiments_bandit_v2_warning_dto import ExperimentsBanditV2WarningDTO


class ExperimentsBanditV2ReadMetaDTO(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_bandit_v2_warning_dto import ExperimentsBanditV2WarningDTO

        return {
            "warnings": ([ExperimentsBanditV2WarningDTO],),
        }

    attribute_map = {
        "warnings": "warnings",
    }

    def __init__(self_, warnings: Union[List[ExperimentsBanditV2WarningDTO], UnsetType] = unset, **kwargs):
        """
        Information about the bandit response.

        :param warnings: Things the caller should know about the response. Absent when there are none.
        :type warnings: [ExperimentsBanditV2WarningDTO], optional
        """
        if warnings is not unset:
            kwargs["warnings"] = warnings
        super().__init__(kwargs)
