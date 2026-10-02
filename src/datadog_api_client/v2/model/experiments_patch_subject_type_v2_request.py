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
    from datadog_api_client.v2.model.experiments_patch_subject_type_v2_request_data import (
        ExperimentsPatchSubjectTypeV2RequestData,
    )


class ExperimentsPatchSubjectTypeV2Request(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_patch_subject_type_v2_request_data import (
            ExperimentsPatchSubjectTypeV2RequestData,
        )

        return {
            "data": (ExperimentsPatchSubjectTypeV2RequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ExperimentsPatchSubjectTypeV2RequestData, **kwargs):
        """
        Request to update the subject type.

        :param data: JSON:API resource containing the subject type identity and fields.
        :type data: ExperimentsPatchSubjectTypeV2RequestData
        """
        super().__init__(kwargs)

        self_.data = data
