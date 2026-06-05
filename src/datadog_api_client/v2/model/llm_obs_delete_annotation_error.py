# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LLMObsDeleteAnnotationError(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "annotation_id": (str,),
            "error": (str,),
        }

    attribute_map = {
        "annotation_id": "annotation_id",
        "error": "error",
    }

    def __init__(self_, annotation_id: str, error: str, **kwargs):
        """
        A partial error for a single annotation that could not be deleted.

        :param annotation_id: ID of the annotation that could not be deleted.
        :type annotation_id: str

        :param error: Error message.
        :type error: str
        """
        super().__init__(kwargs)

        self_.annotation_id = annotation_id
        self_.error = error
