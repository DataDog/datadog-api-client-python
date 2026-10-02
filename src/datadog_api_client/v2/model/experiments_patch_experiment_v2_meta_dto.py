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
    from datadog_api_client.v2.model.experiments_patch_experiment_v2_meta_dto_warnings_items import (
        ExperimentsPatchExperimentV2MetaDTOWarningsItems,
    )


class ExperimentsPatchExperimentV2MetaDTO(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_patch_experiment_v2_meta_dto_warnings_items import (
            ExperimentsPatchExperimentV2MetaDTOWarningsItems,
        )

        return {
            "needs_pipeline_refresh": (bool,),
            "refresh_endpoint": (str,),
            "warnings": ([ExperimentsPatchExperimentV2MetaDTOWarningsItems],),
        }

    attribute_map = {
        "needs_pipeline_refresh": "needs_pipeline_refresh",
        "refresh_endpoint": "refresh_endpoint",
        "warnings": "warnings",
    }

    def __init__(
        self_,
        needs_pipeline_refresh: bool,
        refresh_endpoint: Union[str, UnsetType] = unset,
        warnings: Union[List[ExperimentsPatchExperimentV2MetaDTOWarningsItems], UnsetType] = unset,
        **kwargs,
    ):
        """
        Refresh requirements and warnings returned by an experiment update.

        :param needs_pipeline_refresh: Whether this edit needs a full or non-full pipeline run. This operation does not start the run. A later false value does not clear a refresh required by an earlier edit.
        :type needs_pipeline_refresh: bool

        :param refresh_endpoint: POST to this endpoint after finishing your edits. The full_refresh query parameter selects the required run type. Across multiple edits any full_refresh=true requirement takes priority.
        :type refresh_endpoint: str, optional

        :param warnings: Warnings returned after the experiment update.
        :type warnings: [ExperimentsPatchExperimentV2MetaDTOWarningsItems], optional
        """
        if refresh_endpoint is not unset:
            kwargs["refresh_endpoint"] = refresh_endpoint
        if warnings is not unset:
            kwargs["warnings"] = warnings
        super().__init__(kwargs)

        self_.needs_pipeline_refresh = needs_pipeline_refresh
