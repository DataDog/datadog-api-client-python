# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ExperimentsCreateExposureSQLModelV2RequestDataAttributesSubjectTypesItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "column_name": (str,),
            "subject_type_id": (str,),
        }

    attribute_map = {
        "column_name": "column_name",
        "subject_type_id": "subject_type_id",
    }

    def __init__(self_, column_name: str, subject_type_id: str, **kwargs):
        """
        Mapping between a subject type and its identifier column in the SQL model.

        :param column_name: SQL result column that contains the subject identifier.
        :type column_name: str

        :param subject_type_id: Identifier of the subject type mapped to this column.
        :type subject_type_id: str
        """
        super().__init__(kwargs)

        self_.column_name = column_name
        self_.subject_type_id = subject_type_id
