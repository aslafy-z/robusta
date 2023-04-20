from robusta.core.sinks.sink_base_params import SinkBaseParams
from robusta.core.sinks.sink_config import SinkConfigBase


class GChatSinkParams(SinkBaseParams):
    gchat_webhook: str


class GChatSinkConfigWrapper(SinkConfigBase):
    gchat_sink: GChatSinkParams

    def get_params(self) -> SinkBaseParams:
        return self.gchat_sink
