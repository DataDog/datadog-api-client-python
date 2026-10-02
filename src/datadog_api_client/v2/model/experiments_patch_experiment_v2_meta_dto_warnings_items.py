# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ExperimentsPatchExperimentV2MetaDTOWarningsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "code": (str,),
            "detail": (str,),
        }

    attribute_map = {
        "code": "code",
        "detail": "detail",
    }

    def __init__(self_, code: str, detail: str, **kwargs):
        """
        A warning returned after an experiment update.

        :param code: Code that identifies the warning.
        :type code: str

        :param detail: Explanation of the warning and its effect on the update.
        :type detail: str
        """
        super().__init__(kwargs)

        self_.code = code
        self_.detail = detail
