# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.form_submission_type import FormSubmissionType


class FormSubmissionDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.form_submission_type import FormSubmissionType

        return {
            "id": (UUID,),
            "type": (FormSubmissionType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: UUID, type: FormSubmissionType, **kwargs):
        """


        :param id: The submission identifier.
        :type id: UUID

        :param type: Type for form submissions.
        :type type: FormSubmissionType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
