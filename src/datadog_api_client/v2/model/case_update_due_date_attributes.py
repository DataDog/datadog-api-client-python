# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CaseUpdateDueDateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "due_date": (str,),
        }

    attribute_map = {
        "due_date": "due_date",
    }

    def __init__(self_, due_date: str, **kwargs):
        """
        Attributes for setting or clearing a case's due date.

        :param due_date: The target resolution date for the case, in ``YYYY-MM-DD`` format. Set to ``null`` to clear the due date.
        :type due_date: str
        """
        super().__init__(kwargs)

        self_.due_date = due_date
