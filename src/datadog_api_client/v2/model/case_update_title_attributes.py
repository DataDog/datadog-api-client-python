# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CaseUpdateTitleAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "title": (str,),
        }

    attribute_map = {
        "title": "title",
    }

    def __init__(self_, title: str, **kwargs):
        """
        Case update title attributes

        :param title: Case new title
        :type title: str
        """
        super().__init__(kwargs)

        self_.title = title
