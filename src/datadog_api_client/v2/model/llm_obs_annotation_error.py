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
    from datadog_api_client.v2.model.llm_obs_annotation_error_code import LLMObsAnnotationErrorCode


class LLMObsAnnotationError(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_annotation_error_code import LLMObsAnnotationErrorCode

        return {
            "annotation_id": (str,),
            "code": (LLMObsAnnotationErrorCode,),
            "error": (str,),
            "interaction_id": (str,),
        }

    attribute_map = {
        "annotation_id": "annotation_id",
        "code": "code",
        "error": "error",
        "interaction_id": "interaction_id",
    }

    def __init__(
        self_,
        error: str,
        interaction_id: str,
        annotation_id: Union[str, UnsetType] = unset,
        code: Union[LLMObsAnnotationErrorCode, UnsetType] = unset,
        **kwargs,
    ):
        """
        A partial error for a single annotation that could not be processed.

        :param annotation_id: ID of the annotation that failed, if applicable.
        :type annotation_id: str, optional

        :param code: Stable error code. ``permission_denied`` indicates the item was rejected by queue access rules.
        :type code: LLMObsAnnotationErrorCode, optional

        :param error: Error message.
        :type error: str

        :param interaction_id: ID of the interaction that failed.
        :type interaction_id: str
        """
        if annotation_id is not unset:
            kwargs["annotation_id"] = annotation_id
        if code is not unset:
            kwargs["code"] = code
        super().__init__(kwargs)

        self_.error = error
        self_.interaction_id = interaction_id
