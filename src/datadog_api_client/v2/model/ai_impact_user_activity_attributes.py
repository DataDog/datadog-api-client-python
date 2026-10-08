# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class AIImpactUserActivityAttributes(ModelNormal):
    validations = {
        "day": {},
        "tools": {
            "min_items": 1,
        },
        "user_email": {},
    }

    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "day": (str,),
            "is_active": (bool,),
            "models": ([str],),
            "tools": ([str],),
            "user_email": (str,),
        }

    attribute_map = {
        "day": "day",
        "is_active": "is_active",
        "models": "models",
        "tools": "tools",
        "user_email": "user_email",
    }

    def __init__(
        self_,
        day: str,
        is_active: bool,
        tools: List[str],
        user_email: str,
        models: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Daily AI coding tool activity for a single user. Each entry reports whether the user was
        active on a given day and which AI tools and models they used.

        :param day: The day the activity refers to, in ``YYYY-MM-DD`` format.
        :type day: str

        :param is_active: Whether the user actively used the listed AI tools on that day.
        :type is_active: bool

        :param models: The AI models the user used on that day, for example ``claude-sonnet-4.5`` or ``gpt-5``.
            Values are lowercased and duplicates are removed.
        :type models: [str], optional

        :param tools: The AI coding tools the user used on that day, for example ``Claude Code`` , ``Cursor`` , or
            ``GitHub Copilot``. Known tools are normalized to a canonical name ( ``claude_code`` , ``cursor`` ,
            ``copilot`` ), and other values are converted to snake case. Entries must not be empty.
        :type tools: [str]

        :param user_email: The email address of the user. It is case-insensitive and is matched against the
            email addresses of commit authors.
        :type user_email: str
        """
        if models is not unset:
            kwargs["models"] = models
        super().__init__(kwargs)

        self_.day = day
        self_.is_active = is_active
        self_.tools = tools
        self_.user_email = user_email
