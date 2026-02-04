# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class FormSubmissionAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "submission_data": (dict,),
        }

    attribute_map = {
        "submission_data": "submission_data",
    }

    def __init__(self_, submission_data: dict, **kwargs):
        """


        :param submission_data: The data submitted with the form.
        :type submission_data: dict
        """
        super().__init__(kwargs)

        self_.submission_data = submission_data
