# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class LLMObsAnnotationError(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "annotation_id": (str,),
            "error": (str,),
            "interaction_id": (str,),
        }

    attribute_map = {
        "annotation_id": "annotation_id",
        "error": "error",
        "interaction_id": "interaction_id",
    }

    def __init__(self_, error: str, interaction_id: str, annotation_id: Union[str, UnsetType] = unset, **kwargs):
        """
        A partial error for a single annotation that could not be processed.

        :param annotation_id: ID of the annotation that failed, if applicable.
        :type annotation_id: str, optional

        :param error: Error message.
        :type error: str

        :param interaction_id: ID of the interaction that failed.
        :type interaction_id: str
        """
        if annotation_id is not unset:
            kwargs["annotation_id"] = annotation_id
        super().__init__(kwargs)

        self_.error = error
        self_.interaction_id = interaction_id
