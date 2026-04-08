# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringSignalSuggestedActionType(ModelSimple):
    """
    The type of the suggested action resource.

    :param value: Must be one of ["investigation_log_queries", "recommended_blog_posts"].
    :type value: str
    """

    allowed_values = {
        "investigation_log_queries",
        "recommended_blog_posts",
    }
    INVESTIGATION_LOG_QUERIES: ClassVar["SecurityMonitoringSignalSuggestedActionType"]
    RECOMMENDED_BLOG_POSTS: ClassVar["SecurityMonitoringSignalSuggestedActionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringSignalSuggestedActionType.INVESTIGATION_LOG_QUERIES = SecurityMonitoringSignalSuggestedActionType(
    "investigation_log_queries"
)
SecurityMonitoringSignalSuggestedActionType.RECOMMENDED_BLOG_POSTS = SecurityMonitoringSignalSuggestedActionType(
    "recommended_blog_posts"
)
