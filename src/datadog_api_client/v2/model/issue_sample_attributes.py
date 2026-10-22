# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.issue_sample_bias import IssueSampleBias
    from datadog_api_client.v2.model.issue_sample_data_source import IssueSampleDataSource
    from datadog_api_client.v2.model.issue_sample_error_stack import IssueSampleErrorStack
    from datadog_api_client.v2.model.issue_sample_event import IssueSampleEvent
    from datadog_api_client.v2.model.issue_sample_frame_link import IssueSampleFrameLink


class IssueSampleAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.issue_sample_bias import IssueSampleBias
        from datadog_api_client.v2.model.issue_sample_data_source import IssueSampleDataSource
        from datadog_api_client.v2.model.issue_sample_error_stack import IssueSampleErrorStack
        from datadog_api_client.v2.model.issue_sample_event import IssueSampleEvent
        from datadog_api_client.v2.model.issue_sample_frame_link import IssueSampleFrameLink

        return {
            "application_id": (str,),
            "biases": ([IssueSampleBias],),
            "build_id": (str,),
            "bundle_version": (str,),
            "data_source": (IssueSampleDataSource,),
            "debug_id": (str,),
            "debug_info_captured": (bool,),
            "error_source_type": (str,),
            "error_stack": (IssueSampleErrorStack,),
            "event": (IssueSampleEvent,),
            "git_commit_sha": (str,),
            "git_repository_id": (str,),
            "git_repository_url": (str,),
            "has_session_replay": (bool,),
            "language": (str,),
            "links": ([IssueSampleFrameLink],),
            "os_name": (str,),
            "service": (str,),
            "session_id": (str,),
            "session_replay_url": (str,),
            "snapshot_id": (str,),
            "span_id": (str,),
            "timestamp": (datetime,),
            "trace_id": (str,),
            "variant": (str,),
            "version": (str,),
            "view_id": (str,),
        }

    attribute_map = {
        "application_id": "application_id",
        "biases": "biases",
        "build_id": "build_id",
        "bundle_version": "bundle_version",
        "data_source": "data_source",
        "debug_id": "debug_id",
        "debug_info_captured": "debug_info_captured",
        "error_source_type": "error_source_type",
        "error_stack": "error_stack",
        "event": "event",
        "git_commit_sha": "git_commit_sha",
        "git_repository_id": "git_repository_id",
        "git_repository_url": "git_repository_url",
        "has_session_replay": "has_session_replay",
        "language": "language",
        "links": "links",
        "os_name": "os_name",
        "service": "service",
        "session_id": "session_id",
        "session_replay_url": "session_replay_url",
        "snapshot_id": "snapshot_id",
        "span_id": "span_id",
        "timestamp": "timestamp",
        "trace_id": "trace_id",
        "variant": "variant",
        "version": "version",
        "view_id": "view_id",
    }

    def __init__(
        self_,
        error_stack: IssueSampleErrorStack,
        timestamp: datetime,
        application_id: Union[str, UnsetType] = unset,
        biases: Union[List[IssueSampleBias], UnsetType] = unset,
        build_id: Union[str, UnsetType] = unset,
        bundle_version: Union[str, UnsetType] = unset,
        data_source: Union[IssueSampleDataSource, UnsetType] = unset,
        debug_id: Union[str, UnsetType] = unset,
        debug_info_captured: Union[bool, UnsetType] = unset,
        error_source_type: Union[str, UnsetType] = unset,
        event: Union[IssueSampleEvent, UnsetType] = unset,
        git_commit_sha: Union[str, UnsetType] = unset,
        git_repository_id: Union[str, UnsetType] = unset,
        git_repository_url: Union[str, UnsetType] = unset,
        has_session_replay: Union[bool, UnsetType] = unset,
        language: Union[str, UnsetType] = unset,
        links: Union[List[IssueSampleFrameLink], UnsetType] = unset,
        os_name: Union[str, UnsetType] = unset,
        service: Union[str, UnsetType] = unset,
        session_id: Union[str, UnsetType] = unset,
        session_replay_url: Union[str, UnsetType] = unset,
        snapshot_id: Union[str, UnsetType] = unset,
        span_id: Union[str, UnsetType] = unset,
        trace_id: Union[str, UnsetType] = unset,
        variant: Union[str, UnsetType] = unset,
        version: Union[str, UnsetType] = unset,
        view_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object containing the information of a sample.

        :param application_id: RUM application identifier of the error.
        :type application_id: str, optional

        :param biases: Biases the sample satisfies. A single error can satisfy several biases.
        :type biases: [IssueSampleBias], optional

        :param build_id: Build identifier of the mobile application.
        :type build_id: str, optional

        :param bundle_version: Bundle version of the mobile application.
        :type bundle_version: str, optional

        :param data_source: Product that reported the error. ``NONE`` when the error has no known origin.
        :type data_source: IssueSampleDataSource, optional

        :param debug_id: Debug identifier used to resolve the stack trace of the error to source code.
        :type debug_id: str, optional

        :param debug_info_captured: Whether an Exception Replay snapshot was captured for the error.
        :type debug_info_captured: bool, optional

        :param error_source_type: Source type set by the SDK or tracer that reported the error, such as ``browser`` for RUM browser errors or ``Crashtracking`` for backend crash reports. Usually not set for APM and logs errors.
        :type error_source_type: str, optional

        :param error_stack: Parsed stack trace of the error. Only the sample picked by the ``git_metadata`` bias has frames.
        :type error_stack: IssueSampleErrorStack

        :param event: Raw error event, as stored by its data source. Its fields differ between APM, logs, and RUM.
        :type event: IssueSampleEvent, optional

        :param git_commit_sha: Git commit SHA of the service version.
        :type git_commit_sha: str, optional

        :param git_repository_id: Git repository identifier of the service.
        :type git_repository_id: str, optional

        :param git_repository_url: Git repository URL of the service.
        :type git_repository_url: str, optional

        :param has_session_replay: Whether a RUM session replay is available for the error.
        :type has_session_replay: bool, optional

        :param language: Programming language of the service.
        :type language: str, optional

        :param links: Source code locations of the stack frames that resolve to a repository file.
        :type links: [IssueSampleFrameLink], optional

        :param os_name: Operating system of the device that reported the error.
        :type os_name: str, optional

        :param service: Service name.
        :type service: str, optional

        :param session_id: RUM session identifier of the error.
        :type session_id: str, optional

        :param session_replay_url: URL of the RUM session replay of the error.
        :type session_replay_url: str, optional

        :param snapshot_id: Identifier of the Exception Replay snapshot of the error.
        :type snapshot_id: str, optional

        :param span_id: APM span identifier of the error.
        :type span_id: str, optional

        :param timestamp: Timestamp of the error.
        :type timestamp: datetime

        :param trace_id: APM trace identifier of the error.
        :type trace_id: str, optional

        :param variant: Build variant of the mobile application.
        :type variant: str, optional

        :param version: Version of the service.
        :type version: str, optional

        :param view_id: RUM view identifier of the error.
        :type view_id: str, optional
        """
        if application_id is not unset:
            kwargs["application_id"] = application_id
        if biases is not unset:
            kwargs["biases"] = biases
        if build_id is not unset:
            kwargs["build_id"] = build_id
        if bundle_version is not unset:
            kwargs["bundle_version"] = bundle_version
        if data_source is not unset:
            kwargs["data_source"] = data_source
        if debug_id is not unset:
            kwargs["debug_id"] = debug_id
        if debug_info_captured is not unset:
            kwargs["debug_info_captured"] = debug_info_captured
        if error_source_type is not unset:
            kwargs["error_source_type"] = error_source_type
        if event is not unset:
            kwargs["event"] = event
        if git_commit_sha is not unset:
            kwargs["git_commit_sha"] = git_commit_sha
        if git_repository_id is not unset:
            kwargs["git_repository_id"] = git_repository_id
        if git_repository_url is not unset:
            kwargs["git_repository_url"] = git_repository_url
        if has_session_replay is not unset:
            kwargs["has_session_replay"] = has_session_replay
        if language is not unset:
            kwargs["language"] = language
        if links is not unset:
            kwargs["links"] = links
        if os_name is not unset:
            kwargs["os_name"] = os_name
        if service is not unset:
            kwargs["service"] = service
        if session_id is not unset:
            kwargs["session_id"] = session_id
        if session_replay_url is not unset:
            kwargs["session_replay_url"] = session_replay_url
        if snapshot_id is not unset:
            kwargs["snapshot_id"] = snapshot_id
        if span_id is not unset:
            kwargs["span_id"] = span_id
        if trace_id is not unset:
            kwargs["trace_id"] = trace_id
        if variant is not unset:
            kwargs["variant"] = variant
        if version is not unset:
            kwargs["version"] = version
        if view_id is not unset:
            kwargs["view_id"] = view_id
        super().__init__(kwargs)

        self_.error_stack = error_stack
        self_.timestamp = timestamp
